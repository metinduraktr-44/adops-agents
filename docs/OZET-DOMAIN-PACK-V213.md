# ÖZET — Domain Pack v2.13
> Damga: 2026-08-25T14:44:29Z · TR: Owner docx (PagerDuty/Slack/OTel/Domain1–7) → in-repo pack.

## Ne geldi (docx)
| Dosya teması | Sonuç |
|---|---|
| Datadog+Sentry alarmları | `infra/observability/terraform/main.tf` |
| PagerDuty webhook + Slack | Aynı TF (warn=Slack, critical=Slack+PD) |
| OTel Collector K8s | `infra/observability/k8s/opentelemetry-collector.yaml` |
| Domain 1–2 pipeline | `infra/observability/ci/domain2-pipeline-snippet.yml` |
| Mini-ajans / 7 domain | `data/domains/domain_pack.json` + `docs/domains/*-BOARD.md` |
| 900B / top-100 talebi | 🚩 K-003 → yoğun prompt + research queue |

## Alarm politikası
- **WARN** (~%2 err): yalnızca Slack `#alerts-warnings`
- **CRITICAL** (~%5 err veya 50+/dk spike): Slack `#alerts-critical` + PagerDuty page
- Recovery → PD auto-resolve

## 🚩 Yapılmayanlar (bilinçli)
- Gerçek cluster/terraform apply (credential yok)
- 900B karakter prompt dosyası
- Uydurma “dünyanın en iyi 100 kişisi” listesi
- Secret commit

## Owner P0
1. Datadog/Sentry/PagerDuty/Slack token → lokal env / vault
2. MCP Authorize (Datadog, Sentry, PagerDuty, Grafana, TierZero…) ihtiyaca göre
3. `terraform apply` / `kubectl apply` için hedef cluster onayı

## Çalıştır
```bash
python3 scripts/build_domain_observability_pack.py
python3 scripts/validate.py
```
