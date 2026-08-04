# AdOps Agents — İştirak org (doküman)
> Damga: 2026-08-04T08:33:11Z · TR: Performans pazarlama Claude Code ajansı · Tip: `opco_platform` · Repo: `metinduraktr-44/adops-agents`

## Mandate
LLM agency for performance marketing delivery; 20 depts; 7/24 cron

## HoldCo arayüzü
Reports to: `holdco-coo` · Surfaces: web_admin, cli, github

## Ladder (C→Analyst)
uses full data/org.json (600)

## Workflows
- **Kişisel:** daily_standup_line, todo_queue_from_IS_LISTESI, education_module_monthly, self_inquiry_sample_8, upward_report_weekly, downward_assign_daily, lateral_dependency_ping, roadmap_slice_own_OKRs
- **Grup:** dept_weekly_sync, cross_sub_dependency_board, monthly_board_score, incident_war_room, release_train_comms, country_localization_review

## KPI
CI green ≥99% · Agent eval ≥95% · Inbound path live

## Eğitim / toplantı / yol haritası
- Eğitim: aylık 1 sertifika/modül + BILGI_TABANI damıtımı
- Toplantı: günlük standup · haftalık OpCo sync · aylık HoldCo board satırı
- Yol haritası: OpCo OKR → HoldCo sermaye zarfı içinde
- İletişim: yukarı `holdco-coo` · yatay diğer OpCo · aşağı ladder

## Soru örnekleme
`data/holding_soru_bloklari.json` → `adops-agents` + merkezi 501 banka.

## Rol modelleri
`data/holding_rol_modelleri.json` → `adops-agents` (≤5, kaynaklı).

## Anti-desen
Sahte GitHub issue üretme · HoldCo'yu mikro-yönetme · sessiz eskalasyon.
