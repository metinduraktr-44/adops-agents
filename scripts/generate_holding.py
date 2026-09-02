#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HOLDING ÜRETECİ — holding + iştirak (subsidiary) yapısı için kişisel + grup workflow'lar.
data/holding.json tek doğruluk kaynağı. Her rol için:
  - kişisel workflow'lar: egitim, todo, roadmap, toplanti, iletisim (üst/alt/yan), öz-denetim
  - grup workflow'ları (iştirak bazında): ekip-egitim/todo/roadmap/toplanti/iletisim/raporlama/7-24-nöbet
Ayrıca holding org şeması (mermaid) üretir.
Çıktı: components/holding/<istirak>/<rol>.md, components/holding/<istirak>/_GRUP.md, docs/HOLDING-SEMASI.md
Kullanım: python3 scripts/generate_holding.py
Not: 900 katrilyon karakter gibi hedefler imkânsızdır (🚩); bu üreteç yüksek-sinyalli, ölçeklenebilir çıktı verir.
"""
import json, os, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
OUT = os.path.join(ROOT, "components", "holding")
H = json.load(open(os.path.join(ROOT, "data", "holding.json"), encoding="utf-8"))


def w(path, content):
    fp = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, "w", encoding="utf-8").write(content)


def kisisel_workflows(role, sub, countries):
    t = role.get("tier", "C")
    title = role.get("title", role["slug"])
    up = role.get("reports_to", "owner")
    wf = H["workflow_types"]["kisisel"]
    blocks = {
        "egitim": ["- Kadans: günlük 1 kaynak/changelog · haftalık 1 öğrenim notu · aylık 1 sertifika modülü.",
                   "- Alan: bu iştirakın uzmanlık alanı + rolün kademesi.",
                   "- Rol-model: data/holding_kaynaklar.json (ülke+title başına top-5; gece worklow'u ile büyür)."],
        "todo": ["- Günlük: en yüksek etkili 3 aksiyon (KPI gerekçeli).",
                 "- Kaynak: üst iş listesi → task'a çevir → sahip+tarih ata.",
                 "- Biten işi arşive taşı; zaman damgala (AUDIT_LOG)."],
        "roadmap": ["- Çeyrek hedef → aylık kilometre taşı → haftalık taahhüt → günlük aksiyon.",
                    "- Dateline: her kilometre taşına tarih + sahip.",
                    "- Bağımlılıklar üst/yan rollerle senkron."],
        "toplanti": ["- Günlük standup satırı (dün/bugün/blocker).",
                     "- Haftalık iştirak sync + aylık holding kurulu.",
                     "- Çıktısız toplantı yok: karar+aksiyon(sahip,tarih)+risk+🚩."],
        "iletisim-ust": [f"- Üst: `{up}` — haftalık rapor + eskalasyon (blocker >4h)."],
        "iletisim-alt": ["- Alt: devrettiğin işin sahibi+SLA net; review kadansı."],
        "iletisim-yan": ["- Yan: bağımlı iştirak/departman arayüzleri; handoff paketi."],
        "oz-denetim": ["- Soru bankasından günün seti (docs/OZ-DENETIM-SORU-BANKASI.md, 500+).",
                       "- Kritik 'hayır'lar todo'ya aksiyon olarak düşer."],
    }
    lines = [f"## Kişisel Workflow'lar — {title}"]
    for k in wf:
        lines.append(f"\n### {k}")
        lines += blocks.get(k, ["- (tanımlı)"])
    lines.append(f"\n> Ülke kapsamı: {', '.join(countries)} · her ülke için aynı workflow yerelleştirilir (dil/hukuk).")
    return "\n".join(lines)


def role_doc(role, sub, countries):
    title = role.get("title", role["slug"])
    head = [
        "---",
        f"name: holding-{role['slug']}",
        f"description: \"{title} — {sub['name']} kişisel workflow paketi (holding).\"",
        f"tier: {role.get('tier','C')}",
        f"subsidiary: \"{sub['name']}\"",
        f"generated_utc: {NOW}",
        "---",
        f"# {title} — {sub['name']}",
        f"> İştirak: **{sub['name']}** · Alan: {sub.get('alan','')} · Rapor: `{role.get('reports_to','owner')}` · Üretim: {NOW}",
        "",
        "7/24 LLM ajans olarak çalışır: incele → araştır (top-5 rol-model) → uygula → zaman damgalı arşivle → geri oku → tekrarla.",
        "",
    ]
    return "\n".join(head) + kisisel_workflows(role, sub, countries) + "\n"


def grup_doc(sub, countries):
    wf = H["workflow_types"]["grup"]
    head = [
        "---",
        f"name: holding-grup-{sub['slug']}",
        f"description: \"{sub['name']} grup (ekip) workflow paketi.\"",
        f"generated_utc: {NOW}",
        "---",
        f"# GRUP WORKFLOW — {sub['name']}",
        f"> Alan: {sub.get('alan','')} · Roller: {len(sub['roles'])} · Ülke: {', '.join(countries)}",
        "",
    ]
    desc = {
        "ekip-egitim": "Ortak eğitim takvimi + paylaşılan öğrenim notları (BILGI_TABANI).",
        "ekip-todo": "Ekip backlog'u → önceliklendirme → sahip ataması.",
        "ekip-roadmap": "İştirak çeyrek roadmap'i + dateline + bağımlılık haritası.",
        "ekip-toplanti": "Haftalık ekip sync + aylık holding kuruluna girdi.",
        "ekip-iletisim": "Üst/alt/yan iletişim protokolü + eskalasyon matrisi.",
        "ekip-raporlama": "Haftalık iştirak raporu → Group C-level.",
        "7-24-nobet": "Follow-the-sun nöbet: 3 vardiya, kesintisiz kapsama.",
    }
    lines = list(head)
    for k in wf:
        lines.append(f"### {k}\n- {desc.get(k, '(tanımlı)')}\n")
    return "\n".join(lines)


def org_chart():
    lines = ["# HOLDING ŞEMASI", f"> Üretim: {NOW} · Kaynak: data/holding.json", "",
             "```mermaid", "flowchart TD", "  OWNER([Metin Durak — Owner])"]
    hold = H["holding"]
    lines.append(f"  OWNER --> {hold['slug']}([{hold['name']}])")
    for c in hold["c_level"]:
        lines.append(f"  {hold['slug']} --> {c['slug']}[{c['title']}]")
    for sub in H["subsidiaries"]:
        lines.append(f"  {hold['slug']} --> {sub['slug']}([{sub['name']}])")
    lines += ["```", "", "## İştirakler ve roller"]
    for sub in H["subsidiaries"]:
        lines.append(f"\n### {sub['name']} (`{sub['slug']}`) — {sub.get('alan','')}")
        for r in sub["roles"]:
            lines.append(f"- **{r.get('tier','')}** {r['title']} (`{r['slug']}`) → `{r.get('reports_to','')}`")
    lines += ["", "## Ülkeler",
              f"- Hedef: {', '.join(H['countries']['hedef'])}",
              f"- Pazar: {', '.join(H['countries']['pazar'])}",
              "", "> Her iştirak her ülke için yerelleştirilir (dil + hukuk); gece araştırma worklow'u top-5'i tazeler."]
    open(os.path.join(ROOT, "docs", "HOLDING-SEMASI.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")


def main():
    countries = H["countries"]["hedef"]
    n_role = n_grup = 0

    # Holding C-level (kendi klasörü)
    hold = H["holding"]
    hsub = {"slug": hold["slug"], "name": hold["name"], "alan": "Holding merkez ofis", "roles": hold["c_level"]}
    for r in hold["c_level"]:
        w(f"{hold['slug']}/{r['slug']}.md", role_doc(r, hsub, countries))
        n_role += 1
    w(f"{hold['slug']}/_GRUP.md", grup_doc(hsub, countries))
    n_grup += 1

    for sub in H["subsidiaries"]:
        for r in sub["roles"]:
            w(f"{sub['slug']}/{r['slug']}.md", role_doc(r, sub, countries))
            n_role += 1
        w(f"{sub['slug']}/_GRUP.md", grup_doc(sub, countries))
        n_grup += 1

    # Index
    idx = [f"# HOLDING WORKFLOW KÜTÜPHANESİ (üretim: {NOW})",
           f"> {n_role} rol × kişisel workflow + {n_grup} grup workflow paketi.",
           f"> Kişisel: {', '.join(H['workflow_types']['kisisel'])}",
           f"> Grup: {', '.join(H['workflow_types']['grup'])}", "", "## İştirakler"]
    idx.append(f"- **{hold['name']}** (`{hold['slug']}`) — {len(hold['c_level'])} C-level")
    for sub in H["subsidiaries"]:
        idx.append(f"- **{sub['name']}** (`{sub['slug']}`) — {len(sub['roles'])} rol")
    w("_INDEX.md", "\n".join(idx) + "\n")

    org_chart()
    print(f"HOLDING WRITTEN: {n_role} role workflows + {n_grup} group workflows + docs/HOLDING-SEMASI.md")


if __name__ == "__main__":
    main()
