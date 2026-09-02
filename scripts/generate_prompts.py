#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PROMPT ÜRETECİ — her title/ekip/uygulama için kopyala-yapıştır-hazır promptlar.
data/org.json tek doğruluk kaynağı. Her rol için 3 prompt ailesi üretir:
  (A) TITLE   — rolün kendi çalışma promptu
  (B) EKİP    — rolün ekip/koordinasyon promptu
  (C) UYGULAMA— rolün otomasyon/uygulama (worklow) promptu
Her aile standart MODÜLLER'den oluşur (sinyal > uzunluk).
Kullanım:
  python3 scripts/generate_prompts.py            # tam üretim
  python3 scripts/generate_prompts.py --dept prg # tek departman
  python3 scripts/generate_prompts.py --modules 12
Not: 900M karakter / 122 prompt gibi hedefler fiziksel olarak imkânsızdır (🚩);
     bu üreteç ölçeklenebilir, yüksek-sinyalli, %100 deterministik çıktı verir.
"""
import argparse, json, os, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
OUT = os.path.join(ROOT, "components", "prompts")

# Departman -> öncelikli MCP/araç eşlemesi (components/mcps ve skill deseninden)
DEPT_TOOLS = {
    "prg": ["supermetrics", "google-ads", "brightdata"],
    "sea": ["google-ads", "supermetrics"],
    "soc": ["facebook-ads", "supermetrics"],
    "mob": ["supermetrics", "brightdata"],
    "ret": ["brightdata", "supermetrics"],
    "seo": ["brightdata", "firecrawl"],
    "cro": ["brightdata"],
    "ana": ["supermetrics", "bigquery"],
    "dsc": ["bigquery", "clickhouse"],
    "ops": ["google-ads", "facebook-ads"],
}
DEFAULT_TOOLS = ["supermetrics", "brightdata", "WebSearch"]

# Standart prompt modülleri (title/ekip/uygulama ailelerinde ortak iskelet)
MODULES = [
    ("Kimlik & Yetki", "Rolü, kademesini, rapor hattını ve karar yetkisini (mandate) netleştir; span-of-control ve 7/24 nöbet penceresini belirt."),
    ("Günlük Operasyon", "Bugünün en yüksek etkili 3 aksiyonunu KPI gerekçesiyle seç; çıktı ölçüsü sinyal yoğunluğudur (uzunluk değil)."),
    ("Araştırma & Rol-Model", "İlgili disiplinin dünya top isimlerini (kaynaklar.json) oku; yeni makale/röportaj/proje geldiyse zaman damgalı arsiv/'e not düş; uydurma yok, her bulgu URL'li."),
    ("Çıktı & DoD", "Girdi→çıktı sözleşmesini ve definition-of-done'ı yaz; 6-katman doğrulamadan geçir (structural/integrity/semantic/reference/known-patterns/review)."),
    ("KPI / OKR", "Departman KPI'larından ölç; sapmayı büyüklük+hipotez ile raporla."),
    ("Toplantı Ritmi", "Günlük standup / haftalık liderlik / aylık kurul için hazırlık ve tutanak formatını uygula."),
    ("Eskalasyon", "Karar eşiklerini ve yukarı/yatay eskalasyon matrisini uygula; blocker'ı IS_LISTESI'ne aksiyon olarak düşür."),
    ("Araç & MCP", "Rolün onaylı araçlarını (aşağıdaki liste) doğru sırada kullan; kimlik bilgisi gerekiyorsa güvenli env üzerinden al, asla sabit yazma."),
    ("Öz-Denetim", "OZ-DENETIM-SORU-BANKASI'ndan günün sorularını yanıtla; kritik 'hayır'lar aksiyona dönüşür."),
    ("Öğrenme Döngüsü", "Öğrenimi tek satır BILGI_TABANI.md'ye damıt; işlemi AUDIT_LOG.jsonl'e zaman damgasıyla yaz; bir sonraki koşum bunu geri okur."),
    ("Ekip Koordinasyonu", "Bağımlı roller/hatlarla arayüzü tanımla; devir (handoff) paketini ve SLA'yı belirt."),
    ("Uygulama / Worklow", "Yukarıdakini 7/24 çalışan bir iş akışına bağla: tetikleyici → adımlar → doğrulama → damga → geri-besleme."),
]


TIER_KEY = {"C": "C-LEVEL", "EVP": "EVP", "DIRECTOR": "DIRECTOR",
            "LEAD": "LEAD", "SPECIALIST": "SPECIALIST", "ANALYST": "ANALYST"}


def load_bank():
    p = os.path.join(ROOT, "data", "soru_bankasi.json")
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else None


def build_questions(dept, role, bank, target):
    """Deterministik ≥target öz-denetim sorusu. Uydurma yok: bunlar soru/kontrol; olgusal iddia değil."""
    if not bank:
        return []
    lenses = list(bank.get("universal", {}).keys())
    units = dept.get("units", []) or ["genel"]
    kpis = dept.get("kpis", [])
    qs = []
    for items in bank.get("universal", {}).values():
        qs += items
    qs += bank.get("by_dept", {}).get(dept.get("code", ""), [])
    qs += bank.get("by_tier", {}).get(TIER_KEY.get(role.get("tier", "C"), "C-LEVEL"), [])
    for u in units:
        for l in lenses:
            qs.append(f"[{l}] '{u}' birimi için bu hafta hangi somut kanıtı ürettim; sonraki aksiyonun sahibi+tarihi ne?")
    for k in kpis:
        for l in lenses[:8]:
            qs.append(f"[{l}] KPI '{k}' hedefte mi; sapma varsa kök neden + düzeltme sahibi+tarihi ne?")
    seen, out = set(), []
    for q in qs:
        if q not in seen:
            seen.add(q); out.append(q)
    i = 0
    while len(out) < target:
        l = lenses[i % len(lenses)]
        u = units[i % len(units)]
        cand = (f"[{l}] '{u}' · döngü #{i}: önceki koşumun çıktısını girdi aldım mı (🔗), "
                f"zaman damgaladım mı, öğrenimi BILGI_TABANI'na damıttım mı?")
        if cand not in seen:
            seen.add(cand); out.append(cand)
        i += 1
    return out


def questions_section(dept, role, bank, target):
    qlist = build_questions(dept, role, bank, target)
    if not qlist:
        return ""
    lines = [f"### (D) ÖZ-DENETİM SORU SETİ — gömülü, {len(qlist)} soru (hedef ≥{target})",
             "> Kaynak: docs/OZ-DENETIM-SORU-BANKASI.md + birim/KPI×lens türevleri. "
             "Günlük döngü her koşumda örnekleyip yanıtlar. Uydurma yok; bunlar kontrol sorularıdır.", ""]
    for i, q in enumerate(qlist, 1):
        lines.append(f"{i}. {q}")
    lines.append("")
    return "\n".join(lines)


def w(path, content):
    fp = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)


def tools_for(code):
    return DEPT_TOOLS.get(code, DEFAULT_TOOLS)


def family(fam_name, subject, ctx, tools, modules):
    """Tek bir prompt ailesini (title/ekip/uygulama) modüllerle üret."""
    lines = [f"### {fam_name}", "```prompt",
             f"Sen: {subject}", f"Bağlam: {ctx}",
             f"Onaylı araçlar: {', '.join(tools)}",
             "Kurallar: veri uydurma yok · her bulgu URL'li · 'bulunamadı' açıkça yazılır · "
             "çıktı sinyal odaklı · her işlem zaman damgalı arşivlenir.", ""]
    for i, (title, body) in enumerate(modules[:len(MODULES)], 1):
        lines.append(f"{i}. [{title}] {body}")
    lines += ["", "Bittiğinde: ⏱️[start→end] 🔍[GEÇTİ/KALDI] 📚[öğrenim] 🔗[önceki arşiv okundu?]",
              "```", ""]
    return "\n".join(lines)


def role_doc(dept, role, modules, bank=None, questions=0):
    code = dept["code"]
    tools = tools_for(code)
    dtr = dept.get("name_tr", dept.get("name_en", code))
    unit_line = ", ".join(dept.get("units", [])[:5])
    kpi_line = ", ".join(dept.get("kpis", [])[:4])
    head = [
        "---",
        f"name: prompt-{role['slug']}",
        f"description: \"{role.get('title', role['slug'])} — title/ekip/uygulama prompt ailesi ({dtr}).\"",
        f"tier: {role.get('tier', 'C')}",
        f"department: \"{dept.get('name_en', code)}\"",
        f"generated_utc: {NOW}",
        "---",
        f"# PROMPT — {role.get('title', role['slug'])}",
        f"> Departman: **{dtr}** ({code}) · Kademe: **{role.get('tier','C')}** · "
        f"Rapor: `{role.get('reports_to','owner')}` · Üretim: {NOW}",
        f"> Birimler: {unit_line or '—'} · KPI: {kpi_line or '—'}",
        "",
        "Bu dosya 3 kopyala-yapıştır-hazır prompt ailesi içerir. LLM ajans (Claude Code / Cursor / "
        "Lovable / GitHub Actions) her aileyi ilgili tetikleyicide çağırır.",
        "",
    ]
    subj = f"{role.get('title', role['slug'])} ({dtr} / {role.get('tier','C')})"
    a = family("(A) TITLE PROMPT — rolün kendi çalışması",
               subj, f"{dtr} hattında bireysel/hat sorumluluğu.", tools, modules)
    b = family("(B) EKİP PROMPT — koordinasyon",
               f"{dtr} ekibinin bir üyesi olarak {subj}",
               f"{dtr} ekip hedefleri ve bağımlı hatlarla senkron.", tools, modules)
    c = family("(C) UYGULAMA PROMPT — 7/24 worklow",
               f"{subj} için otomasyon mühendisi",
               "Yukarıdaki title+ekip promptlarını çalışan bir iş akışına bağla.", tools, modules)
    d = questions_section(dept, role, bank, questions) if questions else ""
    return "\n".join(head) + a + b + c + d


def team_doc(dept, modules):
    code = dept["code"]
    dtr = dept.get("name_tr", dept.get("name_en", code))
    tools = tools_for(code)
    head = [
        "---",
        f"name: prompt-ekip-{dept['slug']}",
        f"description: \"{dtr} departmanı ekip promptu (hedef/roadmap/toplantı/7-24).\"",
        f"generated_utc: {NOW}",
        "---",
        f"# EKİP PROMPT — {dtr} ({code})",
        f"> Headcount: {dept.get('headcount','?')} · Birimler: {', '.join(dept.get('units',[]))}",
        f"> KPI: {', '.join(dept.get('kpis',[]))} · Üretim: {NOW}",
        "",
    ]
    fam = family("EKİP OPERASYON PROMPTU",
                 f"{dtr} departman lideri (EVP hattı)",
                 "Departmanın 7/24 kalp atışını yönet: roadmap, dateline, toplantı, nöbet.",
                 tools, modules)
    extra = [
        "## Ekip hedef & roadmap iskeleti",
        "- Çeyrek hedefi → aylık kilometre taşı → haftalık taahhüt → günlük aksiyon.",
        "- Her birim (yukarıda) için sahip hat + KPI + dateline ata.",
        "- Aylık `research_loop.py` çıktısını oku; rol-model/kaynak güncellemesini ekibe yay.",
        "",
    ]
    return "\n".join(head) + fam + "\n".join(extra)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dept", help="sadece bu departman kodu")
    ap.add_argument("--modules", type=int, default=len(MODULES))
    ap.add_argument("--questions", type=int, default=500,
                    help="her title'a gömülü öz-denetim sorusu sayısı (0=kapalı)")
    args = ap.parse_args()

    org = json.load(open(os.path.join(ROOT, "data", "org.json"), encoding="utf-8"))
    modules = MODULES[: max(1, min(args.modules, len(MODULES)))]
    bank = load_bank()
    nq = max(0, args.questions)

    n_role = n_team = 0

    # C-level
    if not args.dept:
        cdept = {"code": "clevel", "slug": "c-level", "name_tr": "C-Seviye Liderlik",
                 "name_en": "C-Level", "units": [], "kpis": []}
        for r in org.get("c_level", []):
            role = {"slug": r["slug"], "title": r["title"], "tier": "C",
                    "reports_to": r.get("reports_to", "owner")}
            w(f"c-level/{r['slug']}.md", role_doc(cdept, role, modules, bank, nq))
            n_role += 1

    for dept in org["departments"]:
        if args.dept and dept["code"] != args.dept:
            continue
        for role in dept["roles"]:
            w(f"{dept['slug']}/{role['slug']}.md", role_doc(dept, role, modules, bank, nq))
            n_role += 1
        w(f"{dept['slug']}/_EKIP-{dept['slug']}.md", team_doc(dept, modules))
        n_team += 1

    # Index
    idx = [f"# PROMPT KÜTÜPHANESİ (üretim: {NOW})",
           f"> {n_role} title promptu + {n_team} ekip promptu. Her title dosyası (A)title (B)ekip (C)uygulama içerir.",
           f"> Modül/aile: {len(modules)} · Üreteç: `scripts/generate_prompts.py`.",
           "", "## Departmanlar"]
    for dept in org["departments"]:
        idx.append(f"- **{dept.get('name_tr', dept['code'])}** (`{dept['code']}`) — "
                   f"{len(dept['roles'])} rol · `components/prompts/{dept['slug']}/`")
    w("_INDEX.md", "\n".join(idx) + "\n")

    print(f"PROMPTS WRITTEN: {n_role} title + {n_team} team (modules={len(modules)}, gömülü-soru≥{nq})")


if __name__ == "__main__":
    main()
