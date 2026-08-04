# Permergrowth — İştirak org (doküman)
> Damga: 2026-08-04T09:52:36Z · TR: Performans büyüme holding iştiraki (aynı org deseni) · Tip: `opco_agency` · Repo: `planned/permergrowth`

## Mandate
Client-facing performance growth; mirrors AdOps ladder at smaller scale

## HoldCo arayüzü
Reports to: `holdco-coo` · Surfaces: web, ios, android

## Ladder (C→Analyst)
| Slug | Title | Tier | Reports to |
|---|---|---|---|
| `pg-ceo` | CEO — performance-growth | C-LEVEL | `holdco-ceo` |
| `pg-evp-performance-growth` | EVP, performance-growth | EVP | `pg-ceo` |
| `pg-dir-ops` | Director, Operations — performance-growth | DIRECTOR | `pg-evp-performance-growth` |
| `pg-lead-delivery` | Lead, Delivery — performance-growth | LEAD | `pg-dir-ops` |
| `pg-spec-core` | Specialist, Core — performance-growth | SPECIALIST | `pg-lead-delivery` |
| `pg-analyst-metrics` | Analyst, Metrics — performance-growth | ANALYST | `pg-lead-delivery` |

## Workflows
- **Kişisel:** daily_standup_line, todo_queue_from_IS_LISTESI, education_module_monthly, self_inquiry_sample_8, upward_report_weekly, downward_assign_daily, lateral_dependency_ping, roadmap_slice_own_OKRs
- **Grup:** dept_weekly_sync, cross_sub_dependency_board, monthly_board_score, incident_war_room, release_train_comms, country_localization_review

## KPI
Client CPA vs plan · Report SLA 100% · Churn risk ≥14d early

## Eğitim / toplantı / yol haritası
- Eğitim: aylık 1 sertifika/modül + BILGI_TABANI damıtımı
- Toplantı: günlük standup · haftalık OpCo sync · aylık HoldCo board satırı
- Yol haritası: OpCo OKR → HoldCo sermaye zarfı içinde
- İletişim: yukarı `holdco-coo` · yatay diğer OpCo · aşağı ladder

## Soru örnekleme
`data/holding_soru_bloklari.json` → `permergrowth` + merkezi 501 banka.

## Rol modelleri
`data/holding_rol_modelleri.json` → `permergrowth` (≤5, kaynaklı).

## Anti-desen
Sahte GitHub issue üretme · HoldCo'yu mikro-yönetme · sessiz eskalasyon.
