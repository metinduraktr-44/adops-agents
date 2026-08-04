# Movea — İştirak org (doküman)
> Damga: 2026-08-04T09:52:36Z · TR: Mobilite / seyahat markası · Tip: `opco_brand` · Repo: `planned/movea`

## Mandate
Brand + booking funnel + paid acquisition

## HoldCo arayüzü
Reports to: `holdco-coo` · Surfaces: web, ios, android

## Ladder (C→Analyst)
| Slug | Title | Tier | Reports to |
|---|---|---|---|
| `mv-ceo` | CEO — movea | C-LEVEL | `holdco-ceo` |
| `mv-evp-movea` | EVP, movea | EVP | `mv-ceo` |
| `mv-dir-ops` | Director, Operations — movea | DIRECTOR | `mv-evp-movea` |
| `mv-lead-delivery` | Lead, Delivery — movea | LEAD | `mv-dir-ops` |
| `mv-spec-core` | Specialist, Core — movea | SPECIALIST | `mv-lead-delivery` |
| `mv-analyst-metrics` | Analyst, Metrics — movea | ANALYST | `mv-lead-delivery` |

## Workflows
- **Kişisel:** daily_standup_line, todo_queue_from_IS_LISTESI, education_module_monthly, self_inquiry_sample_8, upward_report_weekly, downward_assign_daily, lateral_dependency_ping, roadmap_slice_own_OKRs
- **Grup:** dept_weekly_sync, cross_sub_dependency_board, monthly_board_score, incident_war_room, release_train_comms, country_localization_review

## KPI
Bookings vs plan · CAC payback · App store rating ≥4.5

## Eğitim / toplantı / yol haritası
- Eğitim: aylık 1 sertifika/modül + BILGI_TABANI damıtımı
- Toplantı: günlük standup · haftalık OpCo sync · aylık HoldCo board satırı
- Yol haritası: OpCo OKR → HoldCo sermaye zarfı içinde
- İletişim: yukarı `holdco-coo` · yatay diğer OpCo · aşağı ladder

## Soru örnekleme
`data/holding_soru_bloklari.json` → `movea` + merkezi 501 banka.

## Rol modelleri
`data/holding_rol_modelleri.json` → `movea` (≤5, kaynaklı).

## Anti-desen
Sahte GitHub issue üretme · HoldCo'yu mikro-yönetme · sessiz eskalasyon.
