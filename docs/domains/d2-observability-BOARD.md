# Domain 2 — Telemetry, Observability & Diagnostics
> Damga: 2026-08-25T14:09:36Z · Owner: `cto-platform` · Dept: `ops`

## Mandate
Mini-LLM agency for this domain. Route skills; do not invent people; do not pad prompts.

## Directives
- Every new service ships with /opentelemetry-auto-instrumentation
- Incident first call: /tierzero-investigate + /alert-investigation
- WARN → Slack only; CRITICAL → Slack + PagerDuty page
- Auto-resolve PD on Datadog/Sentry recovery
- Validate pipelines with /opentelemetry-validation after deploy
- Mask PII via /configuring-log-export

## Skills (22)
- `/opentelemetry-validation`
- `/opentelemetry-manual-instrumentation`
- `/opentelemetry-auto-instrumentation`
- `/observe-cli`
- `/alert-investigation`
- `/tierzero-investigate`
- `/tierzero-fetch`
- `/sentry-create-alert`
- `/sentry-debug-issue`
- `/kibana-alerting-rules`
- `/observability-service-health`
- `/observability-manage-slos`
- `/observability-logs-search`
- `/observability-llm-obs`
- `/grafana-cloud-mcp-tools`
- `/ddconfig`
- `/ddsetup`
- `/signals-scout-anomaly-detection`
- `/finding-replay-for-issue`
- `/elasticsearch-esql`
- `/configuring-log-export`
- `/pagerduty-mcp-setup`

## MCP hints
- Datadog
- Sentry
- Pagerduty-mcp
- Grafana-cloud
- Tierzero
- Elastic-docs

## Artifacts
- `infra/observability/terraform/main.tf`
- `infra/observability/k8s/opentelemetry-collector.yaml`

## Workflows
- realtime: alert-investigation, tierzero-investigate, opentelemetry-validation
- daily: observability-service-health, debug-k8s-collection, gitops-status
- weekly: review-security, chaos-experiment, dora-metrics
- monthly: deep-research, knowledge-update, analyze-costs, audit-report

## P0 checklist
- [ ] MCP Authorize for needed servers only
- [ ] Secrets in env / vault — never commit
- [ ] Read `data/arsiv/domains/2026-08/` before research tick
