# Domain 7 — Governance, Workflow Automation & Self-Improvement
> Damga: 2026-08-25T14:44:29Z · Owner: `ceo-orchestrator` · Dept: `yonetim`

## Mandate
Mini-LLM agency for this domain. Route skills; do not invent people; do not pad prompts.

## Directives
- RFC 3339 timestamp every governance action
- Read prior archive before monthly research refresh
- DORA + SLO reviewed weekly

## Skills (9)
- `/run-pipeline`
- `/create-pipeline-v1`
- `/dora-metrics`
- `/gitops-status`
- `/manage-slos`
- `/knowledge-update`
- `/deep-research`
- `/audit-report`
- `/manage-pull-requests`

## MCP hints
- Harness
- GitHub
- Tierzero
- Linear

## Artifacts
- catalog only

## Workflows
- realtime: alert-investigation, tierzero-investigate, opentelemetry-validation
- daily: observability-service-health, debug-k8s-collection, gitops-status
- weekly: review-security, chaos-experiment, dora-metrics
- monthly: deep-research, knowledge-update, analyze-costs, audit-report

## P0 checklist
- [ ] MCP Authorize for needed servers only
- [ ] Secrets in env / vault — never commit
- [ ] Read `data/arsiv/domains/2026-08/` before research tick
