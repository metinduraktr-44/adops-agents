# VizaTrack — İştirak org (doküman)
> Damga: 2026-08-04T09:40:15Z · TR: Vize / başvuru takip ürünü · Tip: `opco_product` · Repo: `planned/vizatrack`

## Mandate
Case tracking, document readiness, status notifications

## HoldCo arayüzü
Reports to: `holdco-cto` · Surfaces: web, ios, android

## Ladder (C→Analyst)
| Slug | Title | Tier | Reports to |
|---|---|---|---|
| `vt-ceo` | CEO — vizatrack | C-LEVEL | `holdco-ceo` |
| `vt-evp-vizatrack` | EVP, vizatrack | EVP | `vt-ceo` |
| `vt-dir-ops` | Director, Operations — vizatrack | DIRECTOR | `vt-evp-vizatrack` |
| `vt-lead-delivery` | Lead, Delivery — vizatrack | LEAD | `vt-dir-ops` |
| `vt-spec-core` | Specialist, Core — vizatrack | SPECIALIST | `vt-lead-delivery` |
| `vt-analyst-metrics` | Analyst, Metrics — vizatrack | ANALYST | `vt-lead-delivery` |

## Workflows
- **Kişisel:** daily_standup_line, todo_queue_from_IS_LISTESI, education_module_monthly, self_inquiry_sample_8, upward_report_weekly, downward_assign_daily, lateral_dependency_ping, roadmap_slice_own_OKRs
- **Grup:** dept_weekly_sync, cross_sub_dependency_board, monthly_board_score, incident_war_room, release_train_comms, country_localization_review

## KPI
Case SLA · Doc completeness ≥95% · Push delivery ≥99%

## Eğitim / toplantı / yol haritası
- Eğitim: aylık 1 sertifika/modül + BILGI_TABANI damıtımı
- Toplantı: günlük standup · haftalık OpCo sync · aylık HoldCo board satırı
- Yol haritası: OpCo OKR → HoldCo sermaye zarfı içinde
- İletişim: yukarı `holdco-cto` · yatay diğer OpCo · aşağı ladder

## Soru örnekleme
`data/holding_soru_bloklari.json` → `vizatrack` + merkezi 501 banka.

## Rol modelleri
`data/holding_rol_modelleri.json` → `vizatrack` (≤5, kaynaklı).

## Anti-desen
Sahte GitHub issue üretme · HoldCo'yu mikro-yönetme · sessiz eskalasyon.
