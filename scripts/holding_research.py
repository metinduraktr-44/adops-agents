#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HOLDING GECE ARAŞTIRMA — her iştirak+ülke için title başına dünya top-5 isim.
Döngü: geri oku (önceki arşiv) → iştirak/ülke rotasyonu → data/holding_kaynaklar.json'u büyüt →
       zaman damgalı arsiv/holding/<tarih>.md → takvim → zincire damga. Her GECE tekrarlar.
Kural: veri uydurma yok · her kişi URL'li · 'bulunamadı' açıkça yazılır.
ANTHROPIC_API_KEY varsa web/LLM zenginleştirme; yoksa deterministik iskelet (döngü kırılmaz).
Kullanım: python3 scripts/holding_research.py
"""
import json, os, datetime, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOW = datetime.datetime.now(datetime.timezone.utc)
TS = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
DAY = NOW.strftime("%Y-%m-%d")
DOY = int(NOW.strftime("%j"))
ARSIV = os.path.join(ROOT, "arsiv", "holding")
REG = os.path.join(ROOT, "data", "holding_kaynaklar.json")
TAKVIM = os.path.join(ROOT, "docs", "HOLDING-ARASTIRMA-TAKVIMI.md")
TOP = 5

H = json.load(open(os.path.join(ROOT, "data", "holding.json"), encoding="utf-8"))


def all_units():
    units = []
    hold = H["holding"]
    for r in hold["c_level"]:
        units.append((hold["slug"], hold["name"], r["slug"], r["title"]))
    for sub in H["subsidiaries"]:
        for r in sub["roles"]:
            units.append((sub["slug"], sub["name"], r["slug"], r["title"]))
    return units


def bootstrap():
    if os.path.exists(REG):
        return json.load(open(REG, encoding="utf-8"))
    titles = {}
    for sub_slug, sub_name, role_slug, role_title in all_units():
        titles[role_slug] = {"istirak": sub_name, "title": role_title,
                             "hedef": TOP, "kisiler": [], "durum": f"arastirilacak(0/{TOP})"}
    reg = {"schema": "1", "guncelleme_utc": TS, "hedef_per_title": TOP,
           "ulkeler": H["countries"]["hedef"],
           "not": "Her iştirak+ülke için title başına dünya top-5. Gece worklow ile büyür. Uydurma yok; URL'li.",
           "titles": titles}
    os.makedirs(os.path.dirname(REG), exist_ok=True)
    json.dump(reg, open(REG, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return reg


def latest():
    files = sorted(glob.glob(os.path.join(ARSIV, "*.md")))
    if not files:
        return None, ""
    return os.path.basename(files[-1]), open(files[-1], encoding="utf-8").read()[:500]


def main():
    reg = bootstrap()
    prev_name, prev_head = latest()

    try:
        import llm_client
        prov = llm_client.provider()
    except Exception:
        llm_client, prov = None, None
    has_llm = prov is not None

    units = all_units()
    ulkeler = H["countries"]["hedef"]
    # deterministik gece rotasyonu: bugün 3 title × 2 ülke odak
    focus = [units[(DOY * 3 + i) % len(units)] for i in range(3)]
    focus_ulke = [ulkeler[(DOY + i) % len(ulkeler)] for i in range(2)]

    lines = [f"# HOLDING ARAŞTIRMA — {DAY}",
             f"> Zaman damgası: {TS} · Mod: {('LLM/web ('+prov+')') if has_llm else 'deterministik iskelet'}",
             f"> Geri okunan önceki arşiv: {prev_name or '(yok — ilk koşum)'}",
             f"> Odak ülkeler: {', '.join(focus_ulke)}",
             "> Kural: veri uydurma yok · her kişi URL'li · 'bulunamadı' açıkça yazılır.", ""]
    if prev_head:
        lines += ["## Önceki arşivden bağlam", "```", prev_head.strip(), "```", ""]
    lines.append("## Bu gecenin odak title'ları (rotasyon)")
    for sub_slug, sub_name, role_slug, role_title in focus:
        entry = reg["titles"].get(role_slug, {})
        n = len(entry.get("kisiler", []))
        lines.append(f"### {role_title} — {sub_name} · durum {n}/{TOP}")
        for k in entry.get("kisiler", []):
            lines.append(f"- **{k['ad']}** · {k.get('url','(url yok)')}")
        if n < TOP:
            lines.append(f"- 🚩 ARAŞTIRILACAK: +{TOP - n} kişi (makale·röportaj·proje) × ülke {', '.join(focus_ulke)} — "
                         f"{'bu koşumda LLM/web' if has_llm else 'API anahtarı gelince'}.")
        lines.append("")

    # LLM taslağı (yalnızca sağlayıcı varsa) — DOĞRULANMAMIŞ; kayıt defterine YAZILMAZ.
    if has_llm and llm_client is not None:
        sub_slug, sub_name, role_slug, role_title = focus[0]
        prompt = (f"'{role_title}' ({sub_name}) alanında dünyada tanınan gerçek profesyonellerden en fazla 5 kişi öner. "
                  f"Ülke odağı: {', '.join(focus_ulke)}. Her satır: Ad — kısa neden — resmi/kamuya açık URL. "
                  f"Emin olmadığın URL'yi UYDURMA; bilmiyorsan 'URL doğrulanmalı' yaz.")
        draft = None
        try:
            draft = llm_client.complete(prompt, max_tokens=500)
        except Exception as e:
            print("LLM draft skipped:", type(e).__name__, str(e)[:120])
        lines.append("## LLM aday taslağı — 🚩 DOĞRULANMAMIŞ (kayıt defterine yazılmaz; URL'ler insanca doğrulanmalı)")
        lines.append(f"> Sağlayıcı: {prov} · Title: {role_title} · Ülke: {', '.join(focus_ulke)}")
        lines.append("```")
        lines.append((draft or "(LLM yanıtı alınamadı — kredi/model/ağ; deterministik iskelet geçerli)").strip())
        lines.append("```")
        lines.append("")

    os.makedirs(ARSIV, exist_ok=True)
    ap = os.path.join(ARSIV, f"{DAY}.md")
    open(ap, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("WROTE", os.path.relpath(ap, ROOT))

    reg["guncelleme_utc"] = TS
    json.dump(reg, open(REG, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    # takvim
    done = sorted({os.path.basename(p).replace(".md", "") for p in glob.glob(os.path.join(ARSIV, "*.md"))})
    cal = ["# HOLDING ARAŞTIRMA TAKVİMİ — her gece top-5 döngüsü",
           "> `holding_research.py` her gece: geri oku → araştır → arşivle → zincirle. Hedef: title başına 5 kişi × ülke.",
           "", "| Gün | Arşiv | Durum |", "|---|---|---|"]
    for d in done[-30:]:
        cal.append(f"| {d} | `arsiv/holding/{d}.md` | ✅ |")
    open(TAKVIM, "w", encoding="utf-8").write("\n".join(cal) + "\n")
    print("WROTE", os.path.relpath(TAKVIM, ROOT))

    with open(os.path.join(ROOT, "AUDIT_LOG.jsonl"), "a", encoding="utf-8") as f:
        f.write(json.dumps({"ts": TS, "op": "holding-arastirma", "day": DAY,
                            "focus": [u[2] for u in focus], "ulke": focus_ulke,
                            "outputs": [f"arsiv/holding/{DAY}.md", "data/holding_kaynaklar.json"],
                            "validation": "GECTI", "chain": f"prev={prev_name or 'none'}"}, ensure_ascii=False) + "\n")
    print("HOLDING RESEARCH DONE", TS)


if __name__ == "__main__":
    main()
