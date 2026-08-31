# Cigkoftem — İştirak org (doküman)
> Damga: 2026-08-25T14:44:29Z · TR: QSR / F&B markası · Tip: `opco_brand` · Repo: `planned/cigkoftem`

## Mandate
Franchise ops + local demand gen + loyalty

## HoldCo arayüzü
Reports to: `holdco-coo` · Surfaces: web, ios, android

## Ladder (C→Analyst)
| Slug | Title | Tier | Reports to |
|---|---|---|---|
| `ck-ceo` | CEO — cigkoftem | C-LEVEL | `holdco-ceo` |
| `ck-evp-cigkoftem` | EVP, cigkoftem | EVP | `ck-ceo` |
| `ck-dir-ops` | Director, Operations — cigkoftem | DIRECTOR | `ck-evp-cigkoftem` |
| `ck-lead-delivery` | Lead, Delivery — cigkoftem | LEAD | `ck-dir-ops` |
| `ck-spec-core` | Specialist, Core — cigkoftem | SPECIALIST | `ck-lead-delivery` |
| `ck-analyst-metrics` | Analyst, Metrics — cigkoftem | ANALYST | `ck-lead-delivery` |

## Workflows
- **Kişisel:** daily_standup_line, todo_queue_from_IS_LISTESI, education_module_monthly, self_inquiry_sample_8, upward_report_weekly, downward_assign_daily, lateral_dependency_ping, roadmap_slice_own_OKRs
- **Grup:** dept_weekly_sync, cross_sub_dependency_board, monthly_board_score, incident_war_room, release_train_comms, country_localization_review

## KPI
Same-store sales · Loyalty MAU · Delivery partner SLA

## Eğitim / toplantı / yol haritası
- Eğitim: aylık 1 sertifika/modül + BILGI_TABANI damıtımı
- Toplantı: günlük standup · haftalık OpCo sync · aylık HoldCo board satırı
- Yol haritası: OpCo OKR → HoldCo sermaye zarfı içinde
- İletişim: yukarı `holdco-coo` · yatay diğer OpCo · aşağı ladder

## Soru örnekleme
`data/holding_soru_bloklari.json` → `cigkoftem` + merkezi 501 banka.

## Rol modelleri
`data/holding_rol_modelleri.json` → `cigkoftem` (≤5, kaynaklı).

## Anti-desen
Sahte GitHub issue üretme · HoldCo'yu mikro-yönetme · sessiz eskalasyon.
