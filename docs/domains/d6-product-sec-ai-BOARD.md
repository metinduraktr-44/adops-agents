# Domain 6 — Product Management, Security & AI/ML Models
> Damga: 2026-08-25T14:09:36Z · Owner: `cpo-product` · Dept: `prd`

## Mandate
Mini-LLM agency for this domain. Route skills; do not invent people; do not pad prompts.

## Directives
- PRD alignment gate before implement
- Security review on auth/payment paths

## Skills (9)
- `/write-prd`
- `/update-prd`
- `/check-prd-alignment`
- `/implement-from-prd`
- `/review-security`
- `/auditing-cloud-cluster-security`
- `/manage-feature-flags`
- `/migrate-posthog`
- `/onboard-confidence`

## MCP hints
- ChatPRD
- Posthog
- Sentry
- Braintrust

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
