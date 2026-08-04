# Shared Platform — İştirak org (doküman)
> Damga: 2026-08-04T08:33:11Z · TR: Kimlik, bildirim, analitik, CI ortak katmanı · Tip: `shared_service` · Repo: `planned/platform-shared`

## Mandate
Auth, feature flags, observability, mobile CI for all apps

## HoldCo arayüzü
Reports to: `holdco-cto` · Surfaces: api, web_admin

## Ladder (C→Analyst)
| Slug | Title | Tier | Reports to |
|---|---|---|---|
| `pl-ceo` | CEO — shared-platform | C-LEVEL | `holdco-ceo` |
| `pl-evp-shared-platform` | EVP, shared-platform | EVP | `pl-ceo` |
| `pl-dir-ops` | Director, Operations — shared-platform | DIRECTOR | `pl-evp-shared-platform` |
| `pl-lead-delivery` | Lead, Delivery — shared-platform | LEAD | `pl-dir-ops` |
| `pl-spec-core` | Specialist, Core — shared-platform | SPECIALIST | `pl-lead-delivery` |
| `pl-analyst-metrics` | Analyst, Metrics — shared-platform | ANALYST | `pl-lead-delivery` |

## Workflows
- **Kişisel:** daily_standup_line, todo_queue_from_IS_LISTESI, education_module_monthly, self_inquiry_sample_8, upward_report_weekly, downward_assign_daily, lateral_dependency_ping, roadmap_slice_own_OKRs
- **Grup:** dept_weekly_sync, cross_sub_dependency_board, monthly_board_score, incident_war_room, release_train_comms, country_localization_review

## KPI
Uptime ≥99.9% · MTTR ≤30m · 0 secret leaks

## Eğitim / toplantı / yol haritası
- Eğitim: aylık 1 sertifika/modül + BILGI_TABANI damıtımı
- Toplantı: günlük standup · haftalık OpCo sync · aylık HoldCo board satırı
- Yol haritası: OpCo OKR → HoldCo sermaye zarfı içinde
- İletişim: yukarı `holdco-cto` · yatay diğer OpCo · aşağı ladder

## Soru örnekleme
`data/holding_soru_bloklari.json` → `platform-shared` + merkezi 501 banka.

## Rol modelleri
`data/holding_rol_modelleri.json` → `platform-shared` (≤5, kaynaklı).

## Anti-desen
Sahte GitHub issue üretme · HoldCo'yu mikro-yönetme · sessiz eskalasyon.
