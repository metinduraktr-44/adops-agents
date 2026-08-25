# HOLDING MİMARİSİ
> Damga: 2026-08-25T14:44:29Z · v2.10 · Performance Growth Holding (Performans Büyüme Holding) · Owner: Metin Durak

## Charter
House of brands + shared platform; HoldCo allocates capital/risk; OpCos execute.

## HoldCo C-level
| Slug | Title | Reports to |
|---|---|---|
| `holdco-ceo` | HoldCo CEO | `Metin Durak (Owner)` |
| `holdco-coo` | HoldCo COO — Portfolio Ops | `holdco-ceo` |
| `holdco-cfo` | HoldCo CFO — Capital & Risk | `holdco-ceo` |
| `holdco-clo` | HoldCo CLO — Legal Ring-fence | `holdco-ceo` |
| `holdco-cto` | HoldCo CTO — Shared Platform | `holdco-ceo` |
| `holdco-cdo` | HoldCo CDO — Data & Privacy | `holdco-ceo` |

## İştirakler
| ID | Name | Type | Roles (doc) | Reports |
|---|---|---|---|---|
| `adops-agents` | AdOps Agents | opco_platform | 600 | `holdco-coo` |
| `permergrowth` | Permergrowth | opco_agency | 48 | `holdco-coo` |
| `vizatrack` | VizaTrack | opco_product | 34 | `holdco-cto` |
| `movea` | Movea | opco_brand | 34 | `holdco-coo` |
| `cigkoftem` | Cigkoftem | opco_brand | 29 | `holdco-coo` |
| `hukuk` | Hukuk OpCo | shared_service | 18 | `holdco-clo` |
| `platform-shared` | Shared Platform | shared_service | 22 | `holdco-cto` |

## Ülkeler / pazarlar
| Code | Name | Role | Agency | Law focus |
|---|---|---|---|---|
| TR | Türkiye | home | country-tr-llm | KVKK, Ticaret Kanunu, RTÜK reklam |
| DE | Almanya | target | country-de-llm | GDPR, UWG |
| GB | Birleşik Krallık | target | country-gb-llm | UK GDPR, ASA CAP |
| US | Amerika Birleşik Devletleri | target | country-us-llm | CCPA/CPRA, FTC ad rules |
| AE | Birleşik Arap Emirlikleri | target | country-ae-llm | PDPL UAE, local ad permits |
| NL | Hollanda | market | country-nl-llm | GDPR, ACM |

## Governance (özet)
- HoldCo owns: capital_allocation, portfolio_entry_exit, major_risk, shared_platform_investment, c_level_appointments
- OpCo owns: competitive_strategy, day_to_day_ops, hiring_within_budget, product_roadmap_within_envelope
- Kaynaklar: https://umbrex.com/resources/corporate-strategy-playbook/designing-the-role-of-the-corporate-center/, https://www.diligent.com/resources/blog/what-is-a-holding-company, https://ctacquisitions.com/how-to-build-holdco-from-your-existing-business/

## Ritmi
- Daily / Weekly / Monthly / Nightly → `governance.meeting_cadence` in `data/holding.json`

## K-003
- Do not invent 900B-char prompts
- Do not invent top-100 people per title
- Do not embed 500 unique questions per title card
- Do not mint third-party API keys without owner account

## Bağlantılar
- JSON: `data/holding.json`
- Web/mobil: `docs/HOLDING-WEB-MOBIL-BLUEPRINT.md`
- Özet: `docs/OZET-HOLDING-V210.md`
