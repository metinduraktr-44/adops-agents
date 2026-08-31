# Domain 5 — Communications, Engagement & Scrapers
> Damga: 2026-08-25T14:44:29Z · Owner: `cmo-brand` · Dept: `nbd`

## Mandate
Mini-LLM agency for this domain. Route skills; do not invent people; do not pad prompts.

## Directives
- Comms webhooks verified before prod send
- Scrape → archive with timestamp; no PII leakage

## Skills (9)
- `/twilio-send-message`
- `/twilio-sms-send-message`
- `/twilio-email-send`
- `/twilio-webhook-architecture`
- `/twilio-security-hardening`
- `/apify-actor-development`
- `/bd-scrape`
- `/exa-web-search`
- `/exa-fetch`

## MCP hints
- Twilio-docs
- Apify
- Bright Data
- Exa
- Slack

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
