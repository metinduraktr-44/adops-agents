---
name: domain-obs-router
description: Route Domain 1–7 / observability requests to domain_pack + infra/observability artifacts.
---
# Domain Observability Router
Damga: 2026-08-25T14:44:29Z

When user asks about PagerDuty, Slack alerts, Datadog, Sentry, OpenTelemetry, Domain 1/2:
1. Read `data/domains/domain_pack.json`
2. Use `infra/observability/**` as reference IaC (do not apply without creds)
3. Follow alert policy: WARN=Slack only; CRITICAL=Slack+PD
4. Honor K-003 (no 900B, no invented people)
