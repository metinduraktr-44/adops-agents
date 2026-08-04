#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v2.10 — Holding mimarisi paketi (umbrella + iştirak + ülke + web/mobil).

K-003:
- 900B karakter prompt YOK → yoğun şablon + kart runtime
- title başına top-100 YOK → disiplin/iştirak ≤5 kaynaklı model
- title başına +500 gömülü soru YOK → merkezi 501 + holding blokları

Usage: python3 scripts/build_holding_pack.py
"""
from __future__ import annotations

import datetime
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.datetime.now(datetime.timezone.utc)
TS = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")

TIERS = ["C-LEVEL", "EVP", "DIRECTOR", "LEAD", "SPECIALIST", "ANALYST"]

# Shared workflow templates (personalized + group)
PERSONAL_WF = [
    "daily_standup_line",
    "todo_queue_from_IS_LISTESI",
    "education_module_monthly",
    "self_inquiry_sample_8",
    "upward_report_weekly",
    "downward_assign_daily",
    "lateral_dependency_ping",
    "roadmap_slice_own_OKRs",
]
GROUP_WF = [
    "dept_weekly_sync",
    "cross_sub_dependency_board",
    "monthly_board_score",
    "incident_war_room",
    "release_train_comms",
    "country_localization_review",
]


def ladder(prefix: str, dept: str, reports_c: str) -> list[dict]:
    """Minimal C→Analyst ladder for a subsidiary domain (docs-only, not 600 fake agents)."""
    evp = f"{prefix}-evp-{dept}"
    return [
        {"slug": f"{prefix}-ceo", "title": f"CEO — {dept}", "tier": "C-LEVEL", "reports_to": "holdco-ceo"},
        {"slug": evp, "title": f"EVP, {dept}", "tier": "EVP", "reports_to": f"{prefix}-ceo"},
        {
            "slug": f"{prefix}-dir-ops",
            "title": f"Director, Operations — {dept}",
            "tier": "DIRECTOR",
            "reports_to": evp,
        },
        {
            "slug": f"{prefix}-lead-delivery",
            "title": f"Lead, Delivery — {dept}",
            "tier": "LEAD",
            "reports_to": f"{prefix}-dir-ops",
        },
        {
            "slug": f"{prefix}-spec-core",
            "title": f"Specialist, Core — {dept}",
            "tier": "SPECIALIST",
            "reports_to": f"{prefix}-lead-delivery",
        },
        {
            "slug": f"{prefix}-analyst-metrics",
            "title": f"Analyst, Metrics — {dept}",
            "tier": "ANALYST",
            "reports_to": f"{prefix}-lead-delivery",
        },
    ]


def holding_payload() -> dict:
    holdco_c = [
        {"slug": "holdco-ceo", "title": "HoldCo CEO", "reports_to": "Metin Durak (Owner)"},
        {"slug": "holdco-coo", "title": "HoldCo COO — Portfolio Ops", "reports_to": "holdco-ceo"},
        {"slug": "holdco-cfo", "title": "HoldCo CFO — Capital & Risk", "reports_to": "holdco-ceo"},
        {"slug": "holdco-clo", "title": "HoldCo CLO — Legal Ring-fence", "reports_to": "holdco-ceo"},
        {"slug": "holdco-cto", "title": "HoldCo CTO — Shared Platform", "reports_to": "holdco-ceo"},
        {"slug": "holdco-cdo", "title": "HoldCo CDO — Data & Privacy", "reports_to": "holdco-ceo"},
    ]

    subsidiaries = [
        {
            "id": "adops-agents",
            "name": "AdOps Agents",
            "tr": "Performans pazarlama Claude Code ajansı",
            "type": "opco_platform",
            "repo": "metinduraktr-44/adops-agents",
            "org_source": "data/org.json",
            "headcount_roles": 600,
            "mandate": "LLM agency for performance marketing delivery; 20 depts; 7/24 cron",
            "reports_to_holdco": "holdco-coo",
            "ladder": "uses full data/org.json (600)",
            "workflows": {"personal": PERSONAL_WF, "group": GROUP_WF},
            "surfaces": ["web_admin", "cli", "github"],
            "kpis": ["CI green ≥99%", "Agent eval ≥95%", "Inbound path live"],
        },
        {
            "id": "permergrowth",
            "name": "Permergrowth",
            "tr": "Performans büyüme holding iştiraki (aynı org deseni)",
            "type": "opco_agency",
            "repo": "planned/permergrowth",
            "org_source": "docs/holding/istirakler/permergrowth.md",
            "headcount_roles": 48,
            "mandate": "Client-facing performance growth; mirrors AdOps ladder at smaller scale",
            "reports_to_holdco": "holdco-coo",
            "ladder": ladder("pg", "performance-growth", "holdco-coo"),
            "workflows": {"personal": PERSONAL_WF, "group": GROUP_WF},
            "surfaces": ["web", "ios", "android"],
            "kpis": ["Client CPA vs plan", "Report SLA 100%", "Churn risk ≥14d early"],
        },
        {
            "id": "vizatrack",
            "name": "VizaTrack",
            "tr": "Vize / başvuru takip ürünü",
            "type": "opco_product",
            "repo": "planned/vizatrack",
            "org_source": "docs/holding/istirakler/vizatrack.md",
            "headcount_roles": 34,
            "mandate": "Case tracking, document readiness, status notifications",
            "reports_to_holdco": "holdco-cto",
            "ladder": ladder("vt", "vizatrack", "holdco-cto"),
            "workflows": {"personal": PERSONAL_WF, "group": GROUP_WF},
            "surfaces": ["web", "ios", "android"],
            "kpis": ["Case SLA", "Doc completeness ≥95%", "Push delivery ≥99%"],
        },
        {
            "id": "movea",
            "name": "Movea",
            "tr": "Mobilite / seyahat markası",
            "type": "opco_brand",
            "repo": "planned/movea",
            "org_source": "docs/holding/istirakler/movea.md",
            "headcount_roles": 34,
            "mandate": "Brand + booking funnel + paid acquisition",
            "reports_to_holdco": "holdco-coo",
            "ladder": ladder("mv", "movea", "holdco-coo"),
            "workflows": {"personal": PERSONAL_WF, "group": GROUP_WF},
            "surfaces": ["web", "ios", "android"],
            "kpis": ["Bookings vs plan", "CAC payback", "App store rating ≥4.5"],
        },
        {
            "id": "cigkoftem",
            "name": "Cigkoftem",
            "tr": "QSR / F&B markası",
            "type": "opco_brand",
            "repo": "planned/cigkoftem",
            "org_source": "docs/holding/istirakler/cigkoftem.md",
            "headcount_roles": 29,
            "mandate": "Franchise ops + local demand gen + loyalty",
            "reports_to_holdco": "holdco-coo",
            "ladder": ladder("ck", "cigkoftem", "holdco-coo"),
            "workflows": {"personal": PERSONAL_WF, "group": GROUP_WF},
            "surfaces": ["web", "ios", "android"],
            "kpis": ["Same-store sales", "Loyalty MAU", "Delivery partner SLA"],
        },
        {
            "id": "hukuk",
            "name": "Hukuk OpCo",
            "tr": "Grup hukuk / KVKK / reklam politikası",
            "type": "shared_service",
            "repo": "planned/hukuk",
            "org_source": "docs/holding/istirakler/hukuk.md",
            "headcount_roles": 18,
            "mandate": "Ring-fence, privacy, ad policy, contracts across OpCos",
            "reports_to_holdco": "holdco-clo",
            "ladder": ladder("hk", "legal-compliance", "holdco-clo"),
            "workflows": {"personal": PERSONAL_WF, "group": GROUP_WF},
            "surfaces": ["web_admin"],
            "kpis": ["0 violations", "Policy answers ≤24h", "100% contracts screened"],
        },
        {
            "id": "platform-shared",
            "name": "Shared Platform",
            "tr": "Kimlik, bildirim, analitik, CI ortak katmanı",
            "type": "shared_service",
            "repo": "planned/platform-shared",
            "org_source": "docs/holding/istirakler/platform-shared.md",
            "headcount_roles": 22,
            "mandate": "Auth, feature flags, observability, mobile CI for all apps",
            "reports_to_holdco": "holdco-cto",
            "ladder": ladder("pl", "shared-platform", "holdco-cto"),
            "workflows": {"personal": PERSONAL_WF, "group": GROUP_WF},
            "surfaces": ["api", "web_admin"],
            "kpis": ["Uptime ≥99.9%", "MTTR ≤30m", "0 secret leaks"],
        },
    ]

    countries = [
        {
            "code": "TR",
            "role": "home",
            "name": "Türkiye",
            "language": ["tr"],
            "law": ["KVKK", "Ticaret Kanunu", "RTÜK reklam"],
            "priority": 1,
            "agency": "country-tr-llm",
        },
        {
            "code": "DE",
            "role": "target",
            "name": "Almanya",
            "language": ["de", "en"],
            "law": ["GDPR", "UWG"],
            "priority": 2,
            "agency": "country-de-llm",
        },
        {
            "code": "GB",
            "role": "target",
            "name": "Birleşik Krallık",
            "language": ["en"],
            "law": ["UK GDPR", "ASA CAP"],
            "priority": 3,
            "agency": "country-gb-llm",
        },
        {
            "code": "US",
            "role": "target",
            "name": "Amerika Birleşik Devletleri",
            "language": ["en"],
            "law": ["CCPA/CPRA", "FTC ad rules"],
            "priority": 4,
            "agency": "country-us-llm",
        },
        {
            "code": "AE",
            "role": "target",
            "name": "Birleşik Arap Emirlikleri",
            "language": ["ar", "en"],
            "law": ["PDPL UAE", "local ad permits"],
            "priority": 5,
            "agency": "country-ae-llm",
        },
        {
            "code": "NL",
            "role": "market",
            "name": "Hollanda",
            "language": ["nl", "en"],
            "law": ["GDPR", "ACM"],
            "priority": 6,
            "agency": "country-nl-llm",
        },
    ]

    country_agencies = []
    for c in countries:
        prefix = c["code"].lower()
        country_agencies.append(
            {
                "id": c["agency"],
                "country": c["code"],
                "mandate": f"7/24 LLM agency for {c['name']}: localize playbooks, law, creatives, meetings",
                "ladder": ladder(f"cty-{prefix}", f"country-{prefix}", "holdco-coo"),
                "workflows": {
                    "personal": PERSONAL_WF,
                    "group": GROUP_WF
                    + ["nightly_market_research", "top5_competitor_scan", "locale_qa"],
                },
                "nightly": {
                    "read_archive": f"data/arsiv/holding/{c['code']}/",
                    "research": ["competitors_top5", "regulation_delta", "channel_benchmarks"],
                    "stamp": True,
                    "write_back": True,
                },
            }
        )

    apps = {
        "web": {
            "stack_hint": ["Next.js", "Vercel", "Clerk/WorkOS auth via HoldCo platform"],
            "surfaces": ["holdco_console", "opco_dashboards", "public_marketing"],
            "owners": ["holdco-cto", "platform-shared"],
        },
        "ios": {
            "stack_hint": ["SwiftUI", "TestFlight", "shared API"],
            "surfaces": ["vizatrack", "movea", "cigkoftem", "permergrowth_client"],
            "owners": ["holdco-cto", "each OpCo product lead"],
        },
        "android": {
            "stack_hint": ["Kotlin", "Play Console", "shared API"],
            "surfaces": ["vizatrack", "movea", "cigkoftem", "permergrowth_client"],
            "owners": ["holdco-cto", "each OpCo product lead"],
        },
    }

    governance = {
        "model": "holding_company_portfolio",
        "sources": [
            "https://umbrex.com/resources/corporate-strategy-playbook/designing-the-role-of-the-corporate-center/",
            "https://www.diligent.com/resources/blog/what-is-a-holding-company",
            "https://ctacquisitions.com/how-to-build-holdco-from-your-existing-business/",
        ],
        "holdco_owns": [
            "capital_allocation",
            "portfolio_entry_exit",
            "major_risk",
            "shared_platform_investment",
            "c_level_appointments",
        ],
        "opco_owns": [
            "competitive_strategy",
            "day_to_day_ops",
            "hiring_within_budget",
            "product_roadmap_within_envelope",
        ],
        "raci_escalation": {
            "budget_policy": "holdco-cfo + holdco-clo",
            "security": "holdco-cto + cco-compliance (adops)",
            "impossible_target": "🚩 [ne]·[neden]·[alternatif]",
        },
        "meeting_cadence": {
            "daily": "OpCo standups → gundem/",
            "weekly": "HoldCo portfolio sync (Mon)",
            "monthly": "Board score + country research rollup",
            "nightly": "country + holding research archive loop",
        },
    }

    return {
        "ts": TS,
        "version": "2.10",
        "name": "Performance Growth Holding",
        "name_tr": "Performans Büyüme Holding",
        "owner": "Metin Durak",
        "charter": "House of brands + shared platform; HoldCo allocates capital/risk; OpCos execute.",
        "c_level": holdco_c,
        "tiers": TIERS,
        "subsidiaries": subsidiaries,
        "countries": countries,
        "country_agencies": country_agencies,
        "apps": apps,
        "governance": governance,
        "links": {
            "org_adops": "data/org.json",
            "questions": "data/soru_bankasi.json",
            "role_models": "data/rol_modelleri.json",
            "holding_role_models": "data/holding_rol_modelleri.json",
            "holding_questions": "data/holding_soru_bloklari.json",
            "blueprint": "docs/HOLDING-WEB-MOBIL-BLUEPRINT.md",
            "architecture": "docs/HOLDING-MIMARI.md",
        },
        "red_flags": [
            "Do not invent 900B-char prompts",
            "Do not invent top-100 people per title",
            "Do not embed 500 unique questions per title card",
            "Do not mint third-party API keys without owner account",
        ],
    }


def role_models() -> dict:
    """≤5 sourced models per OpCo domain — empty preferred over invention."""
    return {
        "_note": f"Holding OpCo top models (≤5). Sourced only. Damga: {TS}",
        "adops-agents": {
            "discipline_map": "data/rol_modelleri.json",
            "note": "Uses existing 20-dept role models",
        },
        "permergrowth": [
            ["Blair Enns", "Win Without Pitching", "https://www.winwithoutpitching.com/about/"],
            ["Les Binet", "60/40 effectiveness", "https://ipa.co.uk/knowledge/effectiveness-research-analysis/les-binet-peter-field"],
            ["Byron Sharp", "How Brands Grow", "https://marketingscience.info/staff/professor-byron-sharp"],
            ["Mark Ritson", "Mini MBA", "https://minimba.com/markritson/"],
            ["Avinash Kaushik", "Web Analytics 2.0", "https://www.kaushik.net/avinash/"],
        ],
        "vizatrack": [
            ["Ann Cavoukian", "Privacy by Design", "https://en.wikipedia.org/wiki/Ann_Cavoukian"],
            ["Daniel J. Solove", "Privacy law", "https://www.danielsolove.com/"],
            ["Max Schrems", "noyb / GDPR enforcement", "https://en.wikipedia.org/wiki/Max_Schrems"],
            ["Chip Huyen", "ML/product systems", "https://huyenchip.com/"],
            ["Guillermo Rauch", "DX / shipping", "https://www.linkedin.com/in/guillermo-rauch-51a852208/"],
        ],
        "movea": [
            ["Byron Sharp", "Mental/physical availability", "https://marketingscience.info/staff/professor-byron-sharp"],
            ["Les Binet", "Brand+activation", "https://ipa.co.uk/knowledge/effectiveness-research-analysis/les-binet-peter-field"],
            ["Eric Seufert", "Mobile UA economics", "https://mobiledevmemo.com/"],
            ["Peep Laja", "CRO discipline", "https://peeplaja.com/"],
            ["Rory Sutherland", "Behavioral creative", "https://en.wikipedia.org/wiki/Rory_Sutherland_(advertising_executive)"],
        ],
        "cigkoftem": [
            ["Byron Sharp", "Category entry points", "https://marketingscience.info/staff/professor-byron-sharp"],
            ["Mark Ritson", "Brand positioning", "https://minimba.com/markritson/"],
            ["Orlando Wood", "System1 creative", "https://system1group.com/lemon"],
            ["Peter Fader", "CLV / loyalty", "https://marketing.wharton.upenn.edu/profile/faderp/"],
            ["Jenny Plant", "Client/account ops transfer", "https://www.accountmanagementskills.com/"],
        ],
        "hukuk": [
            ["Daniel J. Solove", "Privacy", "https://www.danielsolove.com/"],
            ["Ann Cavoukian", "PbD", "https://en.wikipedia.org/wiki/Ann_Cavoukian"],
            ["Max Schrems", "Enforcement", "https://en.wikipedia.org/wiki/Max_Schrems"],
            ["Rebecca Tushnet", "Advertising law", "https://hls.harvard.edu/faculty/rebecca-tushnet/"],
            ["Kin Lane", "API governance mindset", "https://apievangelist.com/"],
        ],
        "platform-shared": [
            ["Charity Majors", "Observability", "https://charity.wtf/about"],
            ["Chip Huyen", "ML systems", "https://huyenchip.com/"],
            ["Simon Willison", "LLM ops / injection", "https://simonwillison.net/"],
            ["Hamel Husain", "Evals", "https://hamel.dev/blog/posts/evals/"],
            ["Guillermo Rauch", "Platform DX", "https://www.linkedin.com/in/guillermo-rauch-51a852208/"],
        ],
        "country_agencies": [
            ["Mark Ritson", "Market localization", "https://minimba.com/markritson/"],
            ["Les Binet", "Effectiveness by market", "https://ipa.co.uk/knowledge/effectiveness-research-analysis/les-binet-peter-field"],
            ["Aleyda Solis", "Intl SEO", "https://www.aleydasolis.com/en/"],
            ["Ann Cavoukian", "Cross-border privacy", "https://en.wikipedia.org/wiki/Ann_Cavoukian"],
            ["Blair Enns", "Pricing/positioning by geo", "https://www.winwithoutpitching.com/about/"],
        ],
    }


def question_blocks() -> dict:
    """Holding-specific blocks; cards sample these + central 501 bank."""
    return {
        "ts": TS,
        "policy": "K-003: sample 8–17/run; do not paste 500×title",
        "holdco": [
            "Sermaye tahsisi bu hafta en yüksek marjinal getirili OpCo'ya mı gitti?",
            "Portföy KPI'ları OpCo'lar arasında karşılaştırılabilir mi (ROIC/FCF)?",
            "Bir OpCo riski ring-fence dışında mı sızıyor?",
            "Ülke ajansı gece arşivini okuyup delta yazdı mı?",
            "Web/iOS/Android ortak platform SLA'sı yeşil mi?",
        ],
        "permergrowth": [
            "Müşteri CPA planı vs gerçekleşen sapması kök nedenli mi?",
            "Pitch ≤48h SLA tutuldu mu?",
            "Churn riski ≥14 gün önce bayraklandı mı?",
        ],
        "vizatrack": [
            "Vaka SLA ihlali var mı; müşteri bilgilendirildi mi?",
            "Doküman tamamlılığı ≥95% mi?",
            "KVKK/GDPR veri minimizasyonu uygulandı mı?",
        ],
        "movea": [
            "CAC payback hedefte mi?",
            "App store rating düşüş sinyali var mı?",
            "Ülke lokalizasyonu (dil/ödeme) QA geçti mi?",
        ],
        "cigkoftem": [
            "Same-store sales trendi açıklanabilir mi?",
            "Loyalty MAU hedefte mi?",
            "Franchise iletişim protokolü çalıştı mı?",
        ],
        "hukuk": [
            "0 ihlal hedefi kırıldı mı?",
            "Reklam politikası taraması %100 mü?",
            "Sözleşme incelemesi ≤24h mi?",
        ],
        "country": [
            "Hedef pazar regülasyon deltası arşive damgalandı mı?",
            "Rakip top-5 tarama bu gece koştu mu?",
            "Yerel dil kreatif QA geçti mi?",
        ],
        "apps": [
            "Web konsol P0 bug açık mı?",
            "iOS/Android release train tarihi net mi?",
            "Ortak auth/feature-flag regressyonu var mı?",
        ],
    }


def write_istirak_md(sub: dict) -> str:
    ladder = sub.get("ladder")
    if isinstance(ladder, str):
        ladder_txt = ladder
    else:
        lines = ["| Slug | Title | Tier | Reports to |", "|---|---|---|---|"]
        for r in ladder:
            lines.append(f"| `{r['slug']}` | {r['title']} | {r['tier']} | `{r['reports_to']}` |")
        ladder_txt = "\n".join(lines)

    personal = ", ".join(sub["workflows"]["personal"])
    group = ", ".join(sub["workflows"]["group"])
    kpis = " · ".join(sub["kpis"])
    return f"""# {sub['name']} — İştirak org (doküman)
> Damga: {TS} · TR: {sub['tr']} · Tip: `{sub['type']}` · Repo: `{sub['repo']}`

## Mandate
{sub['mandate']}

## HoldCo arayüzü
Reports to: `{sub['reports_to_holdco']}` · Surfaces: {', '.join(sub['surfaces'])}

## Ladder (C→Analyst)
{ladder_txt}

## Workflows
- **Kişisel:** {personal}
- **Grup:** {group}

## KPI
{kpis}

## Eğitim / toplantı / yol haritası
- Eğitim: aylık 1 sertifika/modül + BILGI_TABANI damıtımı
- Toplantı: günlük standup · haftalık OpCo sync · aylık HoldCo board satırı
- Yol haritası: OpCo OKR → HoldCo sermaye zarfı içinde
- İletişim: yukarı `{sub['reports_to_holdco']}` · yatay diğer OpCo · aşağı ladder

## Soru örnekleme
`data/holding_soru_bloklari.json` → `{sub['id']}` + merkezi 501 banka.

## Rol modelleri
`data/holding_rol_modelleri.json` → `{sub['id']}` (≤5, kaynaklı).

## Anti-desen
Sahte GitHub issue üretme · HoldCo'yu mikro-yönetme · sessiz eskalasyon.
"""


def write_architecture(h: dict) -> str:
    subs = "\n".join(
        f"| `{s['id']}` | {s['name']} | {s['type']} | {s['headcount_roles']} | `{s['reports_to_holdco']}` |"
        for s in h["subsidiaries"]
    )
    cos = "\n".join(
        f"| {c['code']} | {c['name']} | {c['role']} | {c['agency']} | {', '.join(c['law'])} |"
        for c in h["countries"]
    )
    return f"""# HOLDING MİMARİSİ
> Damga: {TS} · v{h['version']} · {h['name']} ({h['name_tr']}) · Owner: {h['owner']}

## Charter
{h['charter']}

## HoldCo C-level
| Slug | Title | Reports to |
|---|---|---|
""" + "\n".join(
        f"| `{r['slug']}` | {r['title']} | `{r['reports_to']}` |" for r in h["c_level"]
    ) + f"""

## İştirakler
| ID | Name | Type | Roles (doc) | Reports |
|---|---|---|---|---|
{subs}

## Ülkeler / pazarlar
| Code | Name | Role | Agency | Law focus |
|---|---|---|---|---|
{cos}

## Governance (özet)
- HoldCo owns: {', '.join(h['governance']['holdco_owns'])}
- OpCo owns: {', '.join(h['governance']['opco_owns'])}
- Kaynaklar: {', '.join(h['governance']['sources'])}

## Ritmi
- Daily / Weekly / Monthly / Nightly → `governance.meeting_cadence` in `data/holding.json`

## K-003
{chr(10).join('- ' + x for x in h['red_flags'])}

## Bağlantılar
- JSON: `data/holding.json`
- Web/mobil: `docs/HOLDING-WEB-MOBIL-BLUEPRINT.md`
- Özet: `docs/OZET-HOLDING-V210.md`
"""


def write_blueprint(h: dict) -> str:
    return f"""# HOLDING WEB / iOS / ANDROID BLUEPRINT
> Damga: {TS} · TR: Ürün kodu değil; mimari + workflow iskeleti.

## Katmanlar
1. **HoldCo Console (Web)** — portföy KPI, sermaye zarfı, ülke ajans durumu
2. **OpCo Dashboards (Web)** — Permergrowth / VizaTrack / Movea / Cigkoftem
3. **Consumer apps (iOS + Android)** — VizaTrack, Movea, Cigkoftem (+ opsiyonel Permergrowth client)
4. **Shared Platform API** — auth, flags, notifications, analytics, CI

## Stack ipuçları
- Web: {', '.join(h['apps']['web']['stack_hint'])}
- iOS: {', '.join(h['apps']['ios']['stack_hint'])}
- Android: {', '.join(h['apps']['android']['stack_hint'])}

## Workflow entegrasyonu
Her app yüzeyi için:
- Kişisel: standup · todo · eğitim · self-inquiry · up/down/lateral
- Grup: dept sync · release train · incident · localization review
- Gece: ülke + rakip top-5 arşiv döngüsü (`scripts/nightly_holding_research.py`)

## Title özelleştirme
App surface title'ları OpCo ladder'ına map edilir; HoldCo CTO sponsor.
Prompt genişletme: `data/prompt_bank/*` + rol kartı §1–21 (AdOps) veya iştirak MD ladder.

## DoD (blueprint)
- [x] holding.json apps bloğu
- [x] OpCo surfaces listelenmiş
- [ ] Gerçek native repo scaffold (ayrı PR; bu pakette yok — sahte commit yok)
"""


def write_one_pager(h: dict) -> str:
    return f"""# ÖZET — Holding v2.10 (tek sayfa)
> Damga: {TS}

## Ne yaptık
1. **HoldCo** (`Performance Growth Holding`) C-level + portföy governance
2. **7 iştirak** iskeleti: AdOps Agents · Permergrowth · VizaTrack · Movea · Cigkoftem · Hukuk · Shared Platform
3. **6 ülke** LLM ajansı (TR home + DE/GB/US/AE/NL) + gece araştırma döngüsü
4. **Web/iOS/Android** blueprint (mimari; native kod ayrı PR)
5. **Top-5** OpCo rol modelleri (kaynaklı) + holding soru blokları (K-003)
6. Scriptler: `build_holding_pack.py` · `holding_report.py` · `nightly_holding_research.py`
7. Workflow: `holding-konsolide.yml` · `gece-holding-arastirma.yml`

## Ne yapmadık (🚩)
- 900B karakter prompt üretimi
- Her title için top-100 kişi uydurma
- Her title'a +500 gömülü soru
- Twilio/Exa vb. ücretsiz API key mint (hesap sende)
- Claude cowork URL oturumlarına erişim (dışarı kapalı)

## Aktivasyon
Claude Code yapıştır **İPTAL**. Kanıt: `docs/AKTIVASYON-DURUM.md` · `scripts/apply_activation.py`

## Sonraki P0
- MCP Authorize (ihtiyaç olanlar)
- OpCo native scaffold PR'ları (VizaTrack/Movea/…) Metin onayıyla
"""


def write_activation_block() -> str:
    return f"""
## v2.10 Holding Overlay (uygulandı)
> Damga: {TS}

```
HOLDING MODE (v2.10):
- data/holding.json — HoldCo + 7 OpCo + 6 country LLM agencies + apps
- docs/HOLDING-MIMARI.md · docs/HOLDING-WEB-MOBIL-BLUEPRINT.md
- docs/holding/istirakler/*.md — OpCo ladders (docs-only; no fake issues)
- data/holding_rol_modelleri.json — ≤5 sourced models / OpCo
- data/holding_soru_bloklari.json — sample with central 501 bank
- Nightly: scripts/nightly_holding_research.py (archive → research → stamp)
- Daily portfolio: scripts/holding_report.py

When user asks holding / iştirak / ülke / web-ios-android:
1) Read holding.json
2) Select OpCo or country agency ladder
3) Expand personal+group workflows
4) Sample questions; never pad characters
5) Stamp AUDIT_LOG + BILGI_TABANI
```
"""


def main() -> int:
    h = holding_payload()
    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "docs" / "holding" / "istirakler").mkdir(parents=True, exist_ok=True)
    (ROOT / "data" / "arsiv" / "holding").mkdir(parents=True, exist_ok=True)

    (ROOT / "data" / "holding.json").write_text(
        json.dumps(h, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (ROOT / "data" / "holding_rol_modelleri.json").write_text(
        json.dumps(role_models(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (ROOT / "data" / "holding_soru_bloklari.json").write_text(
        json.dumps(question_blocks(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    (ROOT / "docs" / "HOLDING-MIMARI.md").write_text(write_architecture(h), encoding="utf-8")
    (ROOT / "docs" / "HOLDING-WEB-MOBIL-BLUEPRINT.md").write_text(write_blueprint(h), encoding="utf-8")
    (ROOT / "docs" / "OZET-HOLDING-V210.md").write_text(write_one_pager(h), encoding="utf-8")

    for sub in h["subsidiaries"]:
        path = ROOT / "docs" / "holding" / "istirakler" / f"{sub['id']}.md"
        path.write_text(write_istirak_md(sub), encoding="utf-8")

    # Seed empty country archive dirs with README
    for c in h["countries"]:
        d = ROOT / "data" / "arsiv" / "holding" / c["code"]
        d.mkdir(parents=True, exist_ok=True)
        readme = d / "README.md"
        if not readme.exists():
            readme.write_text(
                f"# Arşiv {c['code']} — {c['name']}\n> İlk snapshot nightly_holding_research ile gelir.\n",
                encoding="utf-8",
            )

    act = ROOT / "docs" / "CLAUDE-CODE-AKTIVASYON.md"
    if act.exists():
        txt = act.read_text(encoding="utf-8")
        if "v2.10 Holding Overlay" not in txt:
            act.write_text(txt.rstrip() + "\n" + write_activation_block(), encoding="utf-8")

    print(f"holding pack v2.10 written @ {TS}")
    print(f"subsidiaries={len(h['subsidiaries'])} countries={len(h['countries'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
