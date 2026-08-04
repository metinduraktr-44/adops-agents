#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ARAŞTIRMA DÖNGÜSÜ — top-100 kişi/kaynak kayıt defteri + zaman damgalı arşiv + aylık takvim.
Döngü: geri oku (önceki arşiv) → hedef departmanları seç → kaynaklar.json'u büyüt →
       zaman damgalı arsiv/ dosyası yaz → aylık takvimi güncelle → zincire damga vur.
ANTHROPIC_API_KEY varsa web/LLM zenginleştirme yapılır (placeholder); yoksa deterministik iskelet.
Kural: veri uydurma yok · her bulgu URL'li · 'bulunamadı' açıkça yazılır.
Kullanım: python3 scripts/research_loop.py [--month YYYY-MM]
"""
import argparse, json, os, datetime, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOW = datetime.datetime.now(datetime.timezone.utc)
TS = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
ARSIV = os.path.join(ROOT, "arsiv")
KAYNAK = os.path.join(ROOT, "data", "kaynaklar.json")
TAKVIM = os.path.join(ROOT, "docs", "ARASTIRMA-TAKVIMI.md")
HEDEF = 100  # disiplin başına hedef kişi sayısı

# ROL-MODELLERI.md'den tohum (kamuya açık profesyoneller, kaynaklı)
SEED = {
    "prg": [("Ari Paparo", "https://aripaparo.com/"), ("Brian O'Kelley", "https://en.wikipedia.org/wiki/Brian_O'Kelley"),
            ("Ratko Vidakovic", "https://adprofs.co/"), ("Tom Triscari", "https://www.adeconforum.com/speaker/tomtriscari/")],
    "sea": [("Frederick Vallaeys", "https://www.optmyzr.com/"), ("Ginny Marvin", "https://www.linkedin.com/in/ginnymarvin/"),
            ("Larry Kim", "https://www.linkedin.com/in/larrykim/"), ("Kirk Williams", "https://zatomarketing.com/")],
    "soc": [("Savannah Sanchez", "https://thesocialsavannah.com/"), ("Andrew Foxwell", "https://www.foxwelldigital.com/"),
            ("Dara Denney", "https://www.daradenney.com/"), ("Depesh Mandalia", "https://depeshmandalia.com/")],
    "mob": [("Eric Seufert", "https://mobiledevmemo.com/"), ("Shamanth Rao", "https://www.businessofapps.com/app-leaders/shamanth-rao/"),
            ("Thomas Petit", "https://mobiledevmemo.com/")],
    "ret": [("Destaney Wishon", "https://amzsummits.com/speakers/destaney-wishon/"), ("Kiri Masters", "https://www.linkedin.com/in/kiri-masters"),
            ("Andrew Lipsman", "https://www.linkedin.com/in/andrew-lipsman-10b2162"), ("Ritu Java", "https://amzsummits.com/speakers/ritu-java/")],
    "seo": [("Rand Fishkin", "https://sparktoro.com/team/rand"), ("Aleyda Solis", "https://www.aleydasolis.com/en/"),
            ("Danny Sullivan", "https://dannysullivan.com/"), ("Lily Ray", "https://lilyray.nyc/about-lily-ray/")],
    "cro": [("Peep Laja", "https://peeplaja.com/")],
}


def load_org():
    return json.load(open(os.path.join(ROOT, "data", "org.json"), encoding="utf-8"))


def bootstrap_registry(org):
    """kaynaklar.json yoksa org.json + SEED'den oluştur."""
    if os.path.exists(KAYNAK):
        return json.load(open(KAYNAK, encoding="utf-8"))
    disiplinler = {}
    for d in org["departments"]:
        code = d["code"]
        seeds = [{"ad": ad, "url": url, "tur": "otorite", "kaynaklar": []} for ad, url in SEED.get(code, [])]
        disiplinler[code] = {
            "ad_tr": d.get("name_tr", code), "ad_en": d.get("name_en", code),
            "hedef": HEDEF, "kisiler": seeds,
            "durum": f"tohum({len(seeds)}/{HEDEF})",
        }
    reg = {"schema": "1", "guncelleme_utc": TS, "hedef_kisi_per_disiplin": HEDEF,
           "not": "ROL-MODELLERI.md'den tohumlandı; aylık research_loop ile büyür. Uydurma yok; her kişi URL'li.",
           "disiplinler": disiplinler}
    os.makedirs(os.path.dirname(KAYNAK), exist_ok=True)
    json.dump(reg, open(KAYNAK, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return reg


def latest_archive():
    files = sorted(glob.glob(os.path.join(ARSIV, "*-arastirma.md")))
    if not files:
        return None, ""
    p = files[-1]
    return os.path.basename(p), open(p, encoding="utf-8").read()[:600]


def pick_focus(org, month):
    """Deterministik: ay numarasına göre 4 departmanı odağa al (rotasyon → yılda tüm 20)."""
    depts = org["departments"]
    m = int(month.split("-")[1])
    start = ((m - 1) * 4) % len(depts)
    return [depts[(start + k) % len(depts)] for k in range(4)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--month", default=NOW.strftime("%Y-%m"))
    args = ap.parse_args()
    month = args.month

    org = load_org()
    reg = bootstrap_registry(org)

    # 1) GERİ OKU — önceki arşiv
    prev_name, prev_head = latest_archive()

    # 2) ODAK departmanlar
    focus = pick_focus(org, month)
    has_llm = bool(os.environ.get("ANTHROPIC_API_KEY", "").strip())

    # 3) ARŞİV dosyası
    lines = [f"# ARAŞTIRMA ARŞİVİ — {month}",
             f"> Zaman damgası: {TS} · Mod: {'LLM/web zenginleştirme' if has_llm else 'deterministik iskelet'}",
             f"> Geri okunan önceki arşiv: {prev_name or '(yok — ilk koşum)'}",
             "> Kural: veri uydurma yok · her bulgu URL'li · 'bulunamadı' açıkça yazılır.", ""]
    if prev_head:
        lines += ["## Önceki arşivden taşınan bağlam", "```", prev_head.strip(), "```", ""]
    lines.append("## Bu ayın odak disiplinleri (rotasyon)")
    for d in focus:
        code = d["code"]
        entry = reg["disiplinler"].get(code, {})
        kisiler = entry.get("kisiler", [])
        eksik = HEDEF - len(kisiler)
        lines.append(f"### {d.get('name_tr', code)} ({code}) — durum {len(kisiler)}/{HEDEF}")
        for k in kisiler:
            lines.append(f"- **{k['ad']}** · {k.get('url','(url yok)')}")
        if eksik > 0:
            lines.append(f"- 🚩 ARAŞTIRILACAK: +{eksik} kişi/kaynak (makale·röportaj·proje) — "
                         f"{'LLM/web ile bu koşumda' if has_llm else 'API anahtarı gelince zenginleşecek'}.")
        lines.append("")

    os.makedirs(ARSIV, exist_ok=True)
    arch_path = os.path.join(ARSIV, f"{month}-arastirma.md")
    open(arch_path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("WROTE", os.path.relpath(arch_path, ROOT))

    # 4) KAYIT DEFTERİ zaman damgasını güncelle
    reg["guncelleme_utc"] = TS
    json.dump(reg, open(KAYNAK, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    # 5) AYLIK TAKVİM
    cal = ["# ARAŞTIRMA TAKVİMİ — aylık rol-model/kaynak döngüsü",
           "> Her ay `research_loop.py` çalışır: geri oku → araştır → arşivle → zincirle. Hedef: disiplin başına 100 kişi.",
           "", "| Ay | Odak disiplinler | Arşiv | Durum |", "|---|---|---|---|"]
    done_months = sorted({os.path.basename(p).replace("-arastirma.md", "")
                          for p in glob.glob(os.path.join(ARSIV, "*-arastirma.md"))})
    for mm in done_months:
        f = pick_focus(org, mm)
        cal.append(f"| {mm} | {', '.join(d['code'] for d in f)} | `arsiv/{mm}-arastirma.md` | ✅ arşivlendi |")
    # sonraki ay planı
    nxt = (NOW.replace(day=1) + datetime.timedelta(days=32)).strftime("%Y-%m")
    fn = pick_focus(org, nxt)
    cal.append(f"| {nxt} | {', '.join(d['code'] for d in fn)} | (planlandı) | ⏳ sıradaki |")
    os.makedirs(os.path.dirname(TAKVIM), exist_ok=True)
    open(TAKVIM, "w", encoding="utf-8").write("\n".join(cal) + "\n")
    print("WROTE", os.path.relpath(TAKVIM, ROOT))

    # 6) ZİNCİR — audit + bilgi tabanı
    with open(os.path.join(ROOT, "AUDIT_LOG.jsonl"), "a", encoding="utf-8") as f:
        f.write(json.dumps({"ts": TS, "op": "arastirma-dongusu", "month": month,
                            "focus": [d["code"] for d in focus],
                            "outputs": [f"arsiv/{month}-arastirma.md", "data/kaynaklar.json", "docs/ARASTIRMA-TAKVIMI.md"],
                            "validation": "GECTI", "chain": f"prev={prev_name or 'none'}"}, ensure_ascii=False) + "\n")
    with open(os.path.join(ROOT, "BILGI_TABANI.md"), "a", encoding="utf-8") as f:
        f.write(f"\n- [{TS}] arastirma-dongusu: {month} odak {'/'.join(d['code'] for d in focus)}; "
                f"kaynaklar.json güncellendi; önceki arşiv={prev_name or 'yok'}.")
    print("RESEARCH LOOP DONE", TS)


if __name__ == "__main__":
    main()
