# Hukuk OpCo — İştirak org (doküman)
> Damga: 2026-08-04T09:40:15Z · TR: Grup hukuk / KVKK / reklam politikası · Tip: `shared_service` · Repo: `planned/hukuk`

## Mandate
Ring-fence, privacy, ad policy, contracts across OpCos

## HoldCo arayüzü
Reports to: `holdco-clo` · Surfaces: web_admin

## Ladder (C→Analyst)
| Slug | Title | Tier | Reports to |
|---|---|---|---|
| `hk-ceo` | CEO — legal-compliance | C-LEVEL | `holdco-ceo` |
| `hk-evp-legal-compliance` | EVP, legal-compliance | EVP | `hk-ceo` |
| `hk-dir-ops` | Director, Operations — legal-compliance | DIRECTOR | `hk-evp-legal-compliance` |
| `hk-lead-delivery` | Lead, Delivery — legal-compliance | LEAD | `hk-dir-ops` |
| `hk-spec-core` | Specialist, Core — legal-compliance | SPECIALIST | `hk-lead-delivery` |
| `hk-analyst-metrics` | Analyst, Metrics — legal-compliance | ANALYST | `hk-lead-delivery` |

## Workflows
- **Kişisel:** daily_standup_line, todo_queue_from_IS_LISTESI, education_module_monthly, self_inquiry_sample_8, upward_report_weekly, downward_assign_daily, lateral_dependency_ping, roadmap_slice_own_OKRs
- **Grup:** dept_weekly_sync, cross_sub_dependency_board, monthly_board_score, incident_war_room, release_train_comms, country_localization_review

## KPI
0 violations · Policy answers ≤24h · 100% contracts screened

## Eğitim / toplantı / yol haritası
- Eğitim: aylık 1 sertifika/modül + BILGI_TABANI damıtımı
- Toplantı: günlük standup · haftalık OpCo sync · aylık HoldCo board satırı
- Yol haritası: OpCo OKR → HoldCo sermaye zarfı içinde
- İletişim: yukarı `holdco-clo` · yatay diğer OpCo · aşağı ladder

## Soru örnekleme
`data/holding_soru_bloklari.json` → `hukuk` + merkezi 501 banka.

## Rol modelleri
`data/holding_rol_modelleri.json` → `hukuk` (≤5, kaynaklı).

## Anti-desen
Sahte GitHub issue üretme · HoldCo'yu mikro-yönetme · sessiz eskalasyon.
