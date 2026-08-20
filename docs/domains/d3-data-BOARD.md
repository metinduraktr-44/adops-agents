# Domain 3 — Data Engineering, Pipelines & Storage
> Damga: 2026-08-10T10:10:53Z · Owner: `cdo-data` · Dept: `ana`

## Mandate
Mini-LLM agency for this domain. Route skills; do not invent people; do not pad prompts.

## Directives
- Warehouse via /warehouse-init before loads
- Lineage on every model change
- DAG fail → /debugging-dags then /testing-dags

## Skills (16)
- `/setup-warehouse`
- `/setup-warehouse-snowflake`
- `/setup-warehouse-bigquery`
- `/warehouse-init`
- `/airflow`
- `/debugging-dags`
- `/testing-dags`
- `/dagster-expert`
- `/tracing-upstream-lineage`
- `/tracing-downstream-lineage`
- `/pinecone-query`
- `/scylladb-data-modeling`
- `/mongodb-query-optimizer`
- `/profiling-tables`
- `/building-dbt-semantic-layer`
- `/running-dbt-commands`

## MCP hints
- Snowflake
- Neon
- Mongodb
- Pinecone
- Clickhouse

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
