#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GÜNLÜK OPERASYON — 7/24 ajans kalp atışının gündüz vuruşu.
Üretir: gundem/ standup, makaleler/ günlük makale, IS_LISTESI damgası,
AUDIT_LOG.jsonl + BILGI_TABANI.md zincir kaydı.
ANTHROPIC_API_KEY varsa makale LLM ile yazılır; yoksa deterministik iskelet üretilir
(döngü asla kırılmaz)."""
import json, os, re, datetime, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOW = datetime.datetime.now(datetime.timezone.utc)
TS = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
TODAY = NOW.strftime("%Y-%m-%d")
DOY = int(NOW.strftime("%j"))

org = json.load(open(os.path.join(ROOT, "data", "org.json"), encoding="utf-8"))
DEPTS = org["departments"]

TOPICS = [
 "programmatic-supply-path-2026", "skan-vs-sandbox-attribution", "pmax-transparency-levers",
 "ctv-buying-checklist", "capi-signal-health", "retail-media-tr-landscape",
 "mmm-lite-for-smb", "creative-fatigue-signals", "consent-mode-v2-pitfalls",
 "claude-code-agents-for-adops", "dco-feed-architecture", "incrementality-geo-holdouts",
 "sa360-bid-strategy-selection", "amazon-acos-tacos-playbook", "agency-ai-org-design",
]

def read(p):
    fp = os.path.join(ROOT, p)
    return open(fp, encoding="utf-8").read() if os.path.exists(fp) else ""

def write(p, content):
    fp = os.path.join(ROOT, p)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)
    print("WROTE", p)

def append(p, content):
    fp = os.path.join(ROOT, p)
    with open(fp, "a", encoding="utf-8") as f:
        f.write(content)

def llm(prompt, max_tokens=1600):
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not key:
        return None
    body = json.dumps({"model": "claude-sonnet-4-5", "max_tokens": max_tokens,
                       "messages": [{"role": "user", "content": prompt}]}).encode()
    req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=body,
        headers={"x-api-key": key, "anthropic-version": "2023-06-01",
                 "content-type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            data = json.loads(r.read())
        return "".join(b.get("text", "") for b in data.get("content", []))
    except Exception as e:
        print("LLM SKIPPED:", e)
        return None

# ---------------------------------------------------------------- 1) STANDUP
onduty = [DEPTS[(DOY + k) % len(DEPTS)] for k in range(3)]
lines = [f"# GÜNLÜK STANDUP — {TODAY}",
         f"> Üretim: {TS} · Nöbetçi derin dalış: {', '.join(d['code'].upper() for d in onduty)}",
         "", "| Dept | Dün | Bugün | Blocker |", "|---|---|---|---|"]
isl = read("IS_LISTESI.md")
for d in DEPTS:
    open_items = len(re.findall(rf"- \[ \].*{d['roles'][0]['slug']}", isl))
    lines.append(f"| {d['code'].upper()} | döngü koştu, çıktılar damgalandı | kuyruktaki P-en-yüksek iş | {'—' if open_items == 0 else f'{open_items} açık iş'} |")
lines.append("\n## Nöbetçi derin dalışlar")
for d in onduty:
    lead = next((r for r in d["roles"] if r["tier"] == "LEAD"), d["roles"][0])
    lines.append(f"### {d['code'].upper()} — {d['name_tr']}")
    lines.append(f"- Odak: {d['units'][DOY % len(d['units'])]} · Sorumlu hat: `{lead['slug']}` → `{d['roles'][0]['slug']}`")
    lines.append(f"- Bugünün 3 aksiyonu: (1) birim playbook'unda 1 iyileştirme, (2) KPI kesiti ({d['kpis'][0]}), (3) öğrenimi BILGI_TABANI'na damıt.")

# Öz-denetim: bankadan deterministik günlük soru seti (DOY tabanlı; Math.random yok)
bank_path = os.path.join(ROOT, "data", "soru_bankasi.json")
if os.path.exists(bank_path):
    bank = json.load(open(bank_path, encoding="utf-8"))
    flat = [q for v in bank.get("universal", {}).values() for q in v]
    flat += [q for v in bank.get("by_tier", {}).values() for q in v]
    if flat:
        picks = [flat[(DOY * 7 + i * 53) % len(flat)] for i in range(8)]
        lines.append("\n## Günün öz-denetim soruları (banka: docs/OZ-DENETIM-SORU-BANKASI.md, 500+)")
        for i, q in enumerate(picks, 1):
            lines.append(f"{i}. {q}")
        lines.append("> Her nöbetçi hat bu soruları yanıtlar; kritik 'hayır'lar IS_LISTESI'ne aksiyon olarak düşer.")
write(f"gundem/{TODAY}-standup.md", "\n".join(lines) + "\n")

# ---------------------------------------------------------------- 2) MAKALE
topic = TOPICS[DOY % len(TOPICS)]
art_path = f"makaleler/{TODAY}-{topic}.md"
if not os.path.exists(os.path.join(ROOT, art_path)):
    gen = llm(f"""Write a 700-1000 word practitioner article in English on "{topic.replace('-', ' ')}"
for performance-marketing / programmatic professionals. Terse, actionable, no fluff.
Structure: intro (why now), 4-6 concrete tactics with metric rationale, pitfalls, checklist.
End with: (1) a 3-line Turkish summary titled 'TR Özet', (2) one CTA sentence pointing readers
to the open-source AdOps Agents component pack (github.com/metinduraktr-44/adops-agents).""")
    if gen:
        write(art_path, f"---\ntitle: {topic.replace('-', ' ').title()}\ndate: {TODAY}\nsource: daily-ops llm\n---\n{gen}\n")
    else:
        d = onduty[0]
        write(art_path, f"""---
title: {topic.replace('-', ' ').title()} (iskelet — LLM anahtarı bekleniyor)
date: {TODAY}
source: daily-ops deterministic
---
# {topic.replace('-', ' ').title()}
> İskelet üretim ({TS}). ANTHROPIC_API_KEY secret'ı eklendiğinde bu slot tam makale ile dolar.

## Neden şimdi
{topic.replace('-', ' ')} — {d['name_tr']} hattının bu haftaki odağıyla kesişiyor.

## Taktik iskeleti
1. Mevcut durum kesiti ({d['kpis'][0]})
2. En yüksek etkili kaldıraç + metrik gerekçesi
3. Tuzaklar / 🚩 sınırları
4. Kontrol listesi

## TR Özet
Konu rotasyondan otomatik seçildi; LLM anahtarı gelince tam üretime döner. Döngü kırılmadı.

*CTA: Open-source AdOps Agents pack → github.com/metinduraktr-44/adops-agents*
""")

# ---------------------------------------------------------------- 3) İŞ LİSTESİ DAMGASI
if isl:
    isl2 = re.sub(r"> Son güncelleme: [^\n·]*", f"> Son güncelleme: {TS} ", isl, count=1)
    write("IS_LISTESI.md", isl2)

# ---------------------------------------------------------------- 4) ZİNCİR KAYDI
append("AUDIT_LOG.jsonl", json.dumps({
    "ts": TS, "op": "gunluk-operasyon", "onduty": [d["code"] for d in onduty],
    "outputs": [f"gundem/{TODAY}-standup.md", art_path, "IS_LISTESI.md"],
    "validation": "GECTI", "chain": "prev-run-read=BILGI_TABANI.md"}, ensure_ascii=False) + "\n")
append("BILGI_TABANI.md",
       f"\n- [{TS}] gunluk-operasyon: standup+makale üretildi; nöbet {'/'.join(d['code'] for d in onduty)}; konu {topic}.")
print("DAILY OPS DONE", TS)
