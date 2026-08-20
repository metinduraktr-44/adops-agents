# Domain 1 — Infrastructure, Kubernetes & Cloud Computing
> Damga: 2026-08-10T10:10:53Z · Owner: `holdco-cto` · Dept: `inf`

## Mandate
Mini-LLM agency for this domain. Route skills; do not invent people; do not pad prompts.

## Directives
- Dry-run before mutate: /onboard-confidence-dry-run + /azure-validate
- K8s crash → /debug-k8s-collection first
- Host IO/mem → /debug-linux-host-collection
- Cost ceiling → /azure-cost + /analyze-costs
- Weekly chaos → /chaos-experiment
- Timestamp every infra action → /audit-report

## Skills (28)
- `/setup-linux-host-collection`
- `/setup-linux-host-backend`
- `/setup-k8s-collection`
- `/setup-k8s-backend`
- `/deploy-linux-host-explorer`
- `/deploy-k8s-explorer`
- `/debug-linux-host-collection`
- `/debug-k8s-collection`
- `/azure-kubernetes`
- `/airunway-aks-setup`
- `/aws-step-functions`
- `/aws-serverless-deployment`
- `/aws-lambda`
- `/render-workflows`
- `/cloudflare`
- `/wrangler`
- `/create-infrastructure`
- `/azure-deploy`
- `/azure-compute`
- `/azure-validate`
- `/azure-cost`
- `/azure-rbac`
- `/chaos-experiment`
- `/managing-tls-certificates`
- `/configuring-ip-allowlists`
- `/analyze-costs`
- `/onboard-confidence-dry-run`
- `/audit-report`

## MCP hints
- Azure
- Render
- Cloudflare-docs
- Harness
- Aws-mcp

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
