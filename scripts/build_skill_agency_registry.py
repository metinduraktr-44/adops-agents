#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build skill→agency routing pack (v2.9).

Maps the full Cursor skill inventory into AdOps LLM-agency families:
- family catalog + dept ownership
- MCP binding (available vs needs-auth vs N/A)
- title ladder per family (C→worker)
- monthly self-update loop hooks
- Claude Code paste block expansion

K-003: no 900B-char blobs; no invented top-100 people; signal > length.
"""
from __future__ import annotations

import datetime
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.datetime.now(datetime.timezone.utc)
TS = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
YM = NOW.strftime("%Y-%m")

# --- Raw skill inventory (deduped) from owner request ---
RAW_SKILLS = """
setup-linux-host-collection setup-linux-host-backend setup-k8s-collection setup-k8s-backend
query-card-visualization outlier-detection-analysis opentelemetry-validation
opentelemetry-manual-instrumentation opentelemetry-auto-instrumentation observe-cli generate-opal
deploy-linux-host-explorer deploy-k8s-explorer debug-linux-host-collection debug-k8s-collection
alert-investigation apify-ultimate-scraper apify-sdk-integration apify-generate-output-schema
apify-actorization apify-actor-development setup-warehouse-snowflake setup-warehouse-redshift
setup-warehouse-databricks setup-warehouse-bigquery setup-warehouse onboard-confidence-dry-run
onboard-confidence migrate-statsig migrate-posthog migrate-optimizely migrate-eppo mintlify
cx-setup cx-config write-prd update-prd implement-from-prd check-prd-alignment
scylladb-vector-search scylladb-data-modeling scylladb-cloud-setup monk grafana-cloud-mcp-tools
tracking-implementation manage-lexicon deep-research tierzero-investigate tierzero-fetch
twilio-sendgrid-webhooks twilio-sendgrid-suppressions twilio-sendgrid-inbound-parse
twilio-sendgrid-engagement-quality twilio-sendgrid-email-settings twilio-sendgrid-email-send
twilio-sendgrid-deliverability-advisor twilio-sendgrid-account-setup twilio-whatsapp-send-message
twilio-whatsapp-manage-senders twilio-webhook-architecture twilio-voice-twiml
twilio-voice-outbound-calls twilio-verify-send-otp twilio-taskrouter-routing twilio-studio-flows
twilio-sms-send-message twilio-isv-sms-best-practices twilio-send-message twilio-security-hardening
twilio-security-compliance-hipaa twilio-security-api-auth twilio-reliability-patterns
twilio-regulatory-compliance-bundles twilio-rcs-messaging twilio-organizations-setup
twilio-numbers-senders twilio-notifications-alerts-advisor twilio-migrate-messaging-to-verify
twilio-messaging-webhooks twilio-messaging-services twilio-messaging-overview
twilio-messaging-channel-advisor twilio-marketing-promotions-advisor twilio-lookup-phone-intelligence
twilio-identity-verification-advisor twilio-iam-auth-setup twilio-enterprise-knowledge
twilio-email-send twilio-email-deliverability-advisor twilio-debugging-observability
twilio-customer-support-architect twilio-conversations-classic-api twilio-conversation-orchestrator
twilio-conversation-memory twilio-conversation-intelligence twilio-content-template-builder
twilio-conference-calls twilio-compliance-traffic twilio-compliance-onboarding twilio-cli-reference
twilio-call-recordings twilio-ai-agent-architect twilio-agent-connect
twilio-agent-augmentation-architect twilio-account-setup template-usage security-report
scorecard-review run-pipeline migrate-pipeline manage-users manage-slos manage-roles
manage-pull-requests manage-freeze-windows manage-feature-flags manage-delegates gitops-status
dora-metrics debug-pipeline create-trigger create-template create-secret create-policy
create-pipeline-v1 create-pipeline create-infrastructure create-environment create-connector
create-agent-template create-agent chaos-experiment audit-report analyze-costs
gsap-utils gsap-timeline gsap-scrolltrigger gsap-react gsap-plugins gsap-performance
gsap-frameworks gsap-core opensearch-skills dagster-expert get-visual-embed-sdk-reference
get-rest-api-reference get-developer-docs-reference microsoft-foundry entra-app-registration
entra-agent-id azure-validate azure-upgrade azure-storage azure-resource-visualizer
azure-resource-lookup azure-reliability azure-rbac azure-quotas azure-prepare azure-messaging
azure-kusto azure-kubernetes azure-hosted-copilot-sdk azure-enterprise-infra-planner
azure-diagnostics azure-deploy azure-cost azure-compute azure-compliance azure-cloud-migrate
azure-aigateway azure-ai appinsights-instrumentation airunway-aks-setup temporal-developer
temporal-cloud-setup dsql workos-widgets workos exa-web-search exa-fetch exa-best-practices
tpuf appwrite-typescript appwrite-swift appwrite-ruby appwrite-python appwrite-php
appwrite-kotlin appwrite-go appwrite-dotnet appwrite-dart appwrite-cli bd-structured-data
bd-search bd-scrape bd-code bd-browser bd-batch-scrape preparing-compliance-documentation
managing-tls-certificates hardening-user-privileges enforcing-password-policies
enabling-cmek-encryption configuring-sso-and-scim configuring-private-connectivity
configuring-log-export configuring-ip-allowlists configuring-audit-logging
auditing-cloud-cluster-security cockroachdb-sql upgrading-cluster-version reviewing-cluster-health
provisioning-cluster-for-production performing-cluster-maintenance managing-cluster-settings
managing-cluster-capacity managing-certificates-and-encryption molt-verify molt-replicator
molt-fetch triaging-live-sql-activity profiling-transaction-fingerprints
profiling-statement-fingerprints monitoring-background-jobs auditing-table-statistics
analyzing-schema-change-storage-risk analyzing-range-distribution designing-multi-region-applications
designing-application-transactions benchmarking-transaction-patterns warehouse-init
tracing-upstream-lineage tracing-downstream-lineage testing-dags setting-up-astro-project
profiling-tables migrating-airflow-2-to-3 managing-astro-local-env deploying-airflow
debugging-dags creating-openlineage-extractors cosmos-dbt-fusion cosmos-dbt-core checking-freshness
blueprint authoring-dags annotating-task-lineage analyzing-data airflow-plugins airflow-hitl airflow
pinecone-quickstart pinecone-query pinecone-mcp pinecone-help pinecone-full-text-search
pinecone-docs pinecone-cli pinecone-assistant security-generate-security-sample-data
security-detection-rule-management security-case-management security-alert-triage
observability-service-health observability-manage-slos observability-logs-search
observability-llm-obs observability-edot-python-migrate observability-edot-python-instrument
observability-edot-java-migrate observability-edot-java-instrument observability-edot-dotnet-migrate
observability-edot-dotnet-instrument kibana-streams kibana-vega kibana-dashboards kibana-connectors
kibana-audit kibana-alerting-rules kibana-agent-builder elasticsearch-security-troubleshooting
elasticsearch-onboarding elasticsearch-file-ingest elasticsearch-esql elasticsearch-authz
elasticsearch-authn elasticsearch-audit cloud-setup cloud-network-security cloud-manage-project
cloud-create-project cloud-access-management working-with-dbt-mesh using-dbt-for-analytics-engineering
troubleshooting-dbt-job-errors running-dbt-commands fetching-dbt-docs configuring-dbt-mcp-server
building-dbt-semantic-layer answering-natural-language-questions-with-dbt adding-dbt-unit-test
encore-testing encore-service encore-migrate encore-infrastructure encore-go-testing
encore-go-service encore-go-infrastructure encore-go-getting-started encore-go-database
encore-go-code-review encore-go-auth encore-go-api encore-getting-started encore-frontend
debug-traces encore-database create-service encore-code-review encore-auth encore-api
add-infrastructure xcode-project-setup firebase-security-rules-auditor firebase-remote-config-basics
firebase-hosting-basics firebase-firestore firebase-data-connect firebase-crashlytics firebase-basics
firebase-auth-basics firebase-ai-logic-basics firebase-app-hosting-basics session-replay
feedback-analysis feature-adoption account-health amplify-workflow aws-step-functions
aws-serverless-deployment aws-lambda-managed-instances aws-lambda-durable-functions aws-lambda
api-gateway amazon-location-service mongodb-search-and-ai mongodb-schema-design
mongodb-query-optimizer mongodb-natural-language-querying mongodb-mcp-setup mongodb-connection
atlas-stream-processing investigate fix antimetal-mcp-setup omni-query omni-model-explorer
omni-model-builder omni-embed omni-content-explorer omni-content-builder omni-ai-optimizer
omni-admin postman-routing postman-knowledge agent-ready-apis ddtoolsets ddsetup ddconfig
render-workflows render-web-services render-static-sites render-scaling render-private-services
render-postgres render-networking render-monitor render-migrate-from-heroku render-mcp
render-keyvalue render-env-vars render-domains render-docker render-disks render-deploy
render-debug render-cron-jobs render-cli render-blueprints render-background-workers
jfrog-package-safety-and-download jfrog-ai-catalog-skills jfrog pagerduty-mcp-setup
firecrawl-search firecrawl-scrape firecrawl-parse firecrawl-monitor firecrawl-map firecrawl-interact
firecrawl-download firecrawl-crawl firecrawl firecrawl-agent what-would-lenny-do weekly-brief
taxonomy review-agent-insights replay-ux-audit monitor-reliability monitor-ai-quality
investigate-ai-session instrument-events discover-opportunities discover-event-surfaces
discover-analytics-patterns diff-outreach diagnose-errors debug-replay daily-brief create-dashboard
create-chart compare-user-journeys analyze-feedback analyze-experiments analyze-dashboard
analyze-chart analyze-ai-topics analyze-account-health add-analytics-instrumentation
postgres vitess mysql neki grafana-assistant-cli trl-training transformers-js
train-sentence-transformers huggingface-zerogpu huggingface-vision-trainer huggingface-trackio
huggingface-tool-builder huggingface-spaces huggingface-papers huggingface-paper-publisher
huggingface-lora-space-builder huggingface-local-models huggingface-llm-trainer huggingface-gradio
huggingface-datasets huggingface-community-evals hf-cli huggingface-best redis-development
working-with-skills tuning-incremental-sync-config triaging-visual-review-runs triaging-error-issues
suppressing-noisy-errors suggesting-data-imports skills-store signals-scout-surveys
signals-scout-revenue-analytics signals-scout-observability-gaps signals-scout-logs
signals-scout-general signals-scout-error-tracking signals-scout-csp-violations
signals-scout-anomaly-detection signals-scout-ai-observability signals setting-up-a-data-warehouse-source
querying-posthog-data planning-user-interviews managing-subscriptions managing-path-cleaning-rules
managing-experiment-lifecycle managing-endpoint-versions investigating-replay investigating-error-issue
investigate-metric instrument-product-analytics instrument-logs instrument-llm-analytics
instrument-integration instrument-feature-flags instrument-error-tracking inbox-exploration
grouping-noisy-errors formatting-insight-axes finding-sessions-to-watch finding-replay-for-issue
finding-experiments finding-deleted-feature-flags feature-usage-feed exploring-signals-scouts
exploring-llm-traces exploring-llm-evaluations exploring-llm-costs exploring-live-traffic
exploring-autocapture-events exploring-apm-traces downloading-batch-export-files
diagnosing-stacktrace-symbolication diagnosing-sdk-health diagnosing-missing-recordings
diagnosing-failed-warehouse-syncs diagnosing-experiment-results diagnosing-endpoint-performance
debugging-signals-pipeline debugging-local-replay creating-replay-vision-scanners creating-experiments
creating-an-endpoint copying-flags-across-projects consuming-endpoints-from-client-code
configuring-experiment-rollout configuring-experiment-analytics cleaning-up-stale-feature-flags
authoring-signals-scouts authoring-log-alerts auditing-warehouse-data-health auditing-experiments-flags
auditing-endpoints assessing-heatmaps analyzing-experiment-session-replays
clickhousectl-cloud-deploy chdb-datastore clickhouse-best-practices clickhouse-architecture-advisor
clickhousectl-local-dev chdb-sql clickhouse-js-node-troubleshooting clerk-swift clerk-expo
clerk-android clerk-vue-patterns clerk-tanstack-patterns clerk-react-router-patterns
clerk-react-patterns clerk-nuxt-patterns clerk-nextjs-patterns clerk-expo-patterns
clerk-chrome-extension-patterns clerk-astro-patterns clerk-webhooks clerk-testing clerk-orgs
clerk-billing clerk-setup clerk-custom-ui clerk-backend-api clerk functions slack-search
slack-messaging slack-cli slack-api create-slack-app block-kit figma-use-slides figma-use-motion
figma-use-figjam figma-use figma-swiftui figma-implement-motion figma-generate-library
figma-generate-diagram figma-generate-design figma-design-to-code figma-create-new-file
figma-code-connect snowflake-mcp-setup supabase supabase-postgres-best-practices hex-to-canvas
hex-notebook-authoring hex-business-analytics-question elastic-beanstalk deploy aws-architecture-diagram
workflow verification vercel-storage vercel-sandbox vercel-functions vercel-firewall vercel-connect
vercel-cli vercel-agent turbopack shadcn runtime-cache routing-middleware react-best-practices
nextjs next-upgrade next-forge next-cache-components microfrontends marketplace knowledge-update
eve env-vars deployments-cicd chat-sdk cdn-caching bootstrap auth ai-sdk ai-gateway
access-protected-vercel-deployment sentry-snapshots-cocoa sentry-otel-exporter-setup sentry-instrument
sentry-get-started sentry-feature-setup sentry-debug-issue sentry-create-alert
scan-and-fix-accessibility run-web-tests-on-browserstack run-mobile-tests-on-browserstack
wrangler workers-best-practices web-perf sandbox-sdk durable-objects cloudflare
building-mcp-server-on-cloudflare building-ai-agent-on-cloudflare agents-sdk
prisma-upgrade-v7-schema-changes prisma-upgrade-v7-removed-features prisma-upgrade-v7-prisma-config
prisma-upgrade-v7-esm-support prisma-upgrade-v7-env-variables prisma-upgrade-v7-driver-adapters
prisma-upgrade-v7-accelerate-users prisma-database-setup-sqlserver prisma-database-setup-sqlite
prisma-database-setup-prisma-postgres prisma-database-setup-prisma-client-setup
prisma-database-setup-postgresql prisma-database-setup-mysql prisma-database-setup-mongodb
prisma-database-setup-cockroachdb prisma-client-api-transactions prisma-client-api-relations
prisma-client-api-raw-queries prisma-client-api-query-options prisma-client-api-model-queries
prisma-client-api-filters prisma-client-api-constructor prisma-client-api-client-methods
prisma-cli-validate prisma-cli-studio prisma-cli-migrate-status prisma-cli-migrate-resolve
prisma-cli-migrate-reset prisma-cli-migrate-diff prisma-cli-migrate-dev prisma-cli-migrate-deploy
prisma-cli-init prisma-cli-generate prisma-cli-format prisma-cli-dev prisma-cli-debug
prisma-cli-db-seed prisma-cli-db-push prisma-cli-db-pull prisma-cli-db-execute schema-builder
migration-helper function-creator convex-quickstart convex-helpers-guide components-guide
auth-setup update-cursor-settings update-cli-config statusline split-to-prs shell review-security
review-bugbot review migrate-to-skills migrate-to-builds sdk create-subagent create-skill
create-rule create-hook canvas babysit
"""

# Prefix → (family_id, family_name, primary_dept, c_owner, mcp_hint, product_fit)
FAMILY_RULES = [
    (r"^twilio-", "comms-twilio", "Comms & Messaging (Twilio)", "cls", "cro-revenue", "Twilio-docs", "Client alerts, OTP, WhatsApp lead nurture"),
    (r"^firecrawl|^bd-|^apify-|^exa-", "web-intel", "Web Intelligence & Scraping", "seo", "cso-strategy", "Bright Data|Apify|Exa|Firecrawl", "Competitive ads, SERP, creator intel"),
    (r"^observe|^opentelemetry|^setup-linux|^setup-k8s|^deploy-|^debug-linux|^debug-k8s|^generate-opal|^query-card|^outlier|^alert-investigation", "obs-observe", "Observability (Observe)", "inf", "cto-platform", "Observe", "Agency infra + client site health"),
    (r"^grafana|^monk", "obs-grafana", "Observability (Grafana)", "inf", "cto-platform", "Grafana-cloud", "Dashboards for media ops"),
    (r"^tierzero-", "obs-tierzero", "Prod Investigation (TierZero)", "inf", "cto-platform", "Tierzero", "Incident evidence for infra/agents"),
    (r"^antimetal|^investigate$|^fix$", "obs-antimetal", "Infra RCA (Antimetal)", "inf", "cto-platform", "Antimetal", "Causal graphs for outages"),
    (r"^sentry-", "obs-sentry", "Error Tracking (Sentry)", "inf", "cto-platform", "Sentry", "Component runtime errors"),
    (r"^pagerduty", "ops-pagerduty", "Incident Mgmt (PagerDuty)", "ops", "coo-delivery", "Pagerduty-mcp", "On-call for trafficking incidents"),
    (r"^elastic|^kibana|^observability-|^security-|^cloud-setup|^cloud-network|^cloud-manage|^cloud-create|^cloud-access", "obs-elastic", "Search & SecOps (Elastic)", "inf", "cto-platform", "Elastic-docs|Coralogix", "Log search for agency tools"),
    (r"^datadog|^ddtool|^ddsetup|^ddconfig", "obs-datadog", "APM (Datadog)", "inf", "cto-platform", "Datadog", "Service health for connectors"),
    (r"^posthog|^signals|^instrument-|^session-replay|^feedback|^feature-adoption|^account-health|^taxonomy|^weekly-brief|^daily-brief|^what-would-lenny|^discover-|^analyze-|^create-dashboard|^create-chart|^compare-user|^add-analytics|^diff-outreach|^diagnose-errors|^debug-replay|^monitor-|^review-agent|^replay-|^finding-|^exploring-|^investigating-|^investigate-ai|^investigate-metric|^creating-|^configuring-experiment|^cleaning-up-stale|^authoring-|^auditing-|^assessing-|^managing-experiment|^managing-endpoint|^managing-path|^managing-subscriptions|^planning-user|^querying-posthog|^setting-up-a-data-warehouse|^suggesting-data|^skills-store|^working-with-skills|^tuning-incremental|^triaging-|^suppressing-|^grouping-|^formatting-|^feature-usage|^downloading-batch|^diagnosing-|^debugging-signals|^debugging-local|^copying-flags|^consuming-endpoints|^inbox-exploration|^analyzing-experiment-session", "product-analytics", "Product Analytics (PostHog)", "ana", "cdo-data", "Posthog", "Inbound product + experiment analytics"),
    (r"^migrate-statsig|^migrate-posthog|^migrate-optimizely|^migrate-eppo|^onboard-confidence|^manage-lexicon|^tracking-implementation", "experimentation", "Experimentation & Flags", "cro", "cpo-product", "Confidence-flags|Posthog", "CRO + flag migrations"),
    (r"^write-prd|^update-prd|^implement-from-prd|^check-prd|^mintlify|^cx-", "product-docs", "Product Spec & Docs", "prd", "cpo-product", "ChatPRD|Mintlify", "Premium pack PRDs + docs"),
    (r"^harness|^run-pipeline|^migrate-pipeline|^manage-users|^manage-slos|^manage-roles|^manage-pull|^manage-freeze|^manage-feature|^manage-delegates|^gitops|^dora|^debug-pipeline|^create-trigger|^create-template|^create-secret|^create-policy|^create-pipeline|^create-infrastructure|^create-environment|^create-connector|^create-agent|^chaos-experiment|^audit-report|^analyze-costs|^template-usage|^security-report|^scorecard-review", "cicd-harness", "CI/CD (Harness)", "inf", "cto-platform", "Harness", "Agency Actions + delivery pipelines"),
    (r"^airflow|^dagster|^astro|^dbt|^cosmos|^warehouse-init|^tracing-|^testing-dags|^setting-up-astro|^profiling-tables|^migrating-airflow|^managing-astro|^deploying-airflow|^debugging-dags|^creating-openlineage|^checking-freshness|^blueprint|^authoring-dags|^annotating-task|^analyzing-data|^setup-warehouse|^adding-dbt|^answering-natural-language|^building-dbt|^fetching-dbt|^running-dbt|^troubleshooting-dbt|^using-dbt|^working-with-dbt", "data-pipeline", "Data Pipelines (Airflow/dbt)", "dsc", "cdo-data", "None", "Media data warehouse ETL"),
    (r"^snowflake|^hex-|^omni-", "bi-analytics", "BI & Notebooks", "ana", "cdo-data", "Snowflake|Hex|Omni", "Client reporting notebooks"),
    (r"^clickhouse|^chdb|^neki", "olap-clickhouse", "OLAP (ClickHouse)", "dsc", "cdo-data", "Clickhouse", "High-volume event analytics"),
    (r"^cockroach|^molt-|^preparing-compliance|^managing-tls|^hardening-user|^enforcing-password|^enabling-cmek|^configuring-|^auditing-cloud|^auditing-table|^triaging-live|^profiling-transaction|^profiling-statement|^monitoring-background|^analyzing-schema|^analyzing-range|^designing-multi|^designing-application|^benchmarking-transaction|^provisioning-cluster|^performing-cluster|^managing-cluster|^managing-certificates|^reviewing-cluster|^upgrading-cluster|^cockroachdb", "db-cockroach", "Distributed SQL (Cockroach)", "inf", "cto-platform", "Cockroachdb-toolbox|Cockroachdb-cloud", "Multi-region agency DB patterns"),
    (r"^scylla", "db-scylla", "ScyllaDB", "inf", "cto-platform", "None", "Low-latency feature store patterns"),
    (r"^pinecone|^tpuf", "vector-ai", "Vector Search", "dsc", "cdo-data", "Pinecone|Turbopuffer", "Knowledge retrieval for agents"),
    (r"^mongodb|^atlas-", "db-mongo", "MongoDB Atlas", "inf", "cto-platform", "Mongodb", "Document stores for packs"),
    (r"^postgres$|^mysql$|^vitess$|^redis|^supabase|^prisma-|^schema-builder|^migration-helper", "db-relational", "Relational DB & ORM", "inf", "cto-platform", "Supabase|Prisma-Local|Prisma-Remote|Neon|PlanetScale", "Agency data models"),
    (r"^convex-|^function-creator|^components-guide|^auth-setup$", "backend-convex", "Backend (Convex)", "prd", "cto-platform", "Convex", "Realtime backend for tools"),
    (r"^encore-|^create-service$|^add-infrastructure$|^debug-traces$", "backend-encore", "Backend (Encore)", "prd", "cto-platform", "Encore-mcp", "Typed service APIs"),
    (r"^azure-|^entra-|^microsoft-|^appinsights|^airunway|^get-visual|^get-rest|^get-developer|^dsql$", "cloud-azure", "Cloud (Azure)", "inf", "cto-platform", "Azure|Azure-cosmosdb|Aurora-dsql", "Enterprise client infra"),
    (r"^aws-|^amplify|^api-gateway|^amazon-location|^elastic-beanstalk|^deploy$|^aws-architecture", "cloud-aws", "Cloud (AWS)", "inf", "cto-platform", "Aws-mcp|Awsiac|Awspricing|Awslabs.aws-api-mcp-server|Aws-knowledge-mcp-server|Aws-serverless-mcp|Awsknowledge", "Serverless connectors"),
    (r"^render-", "cloud-render", "Cloud (Render)", "inf", "cto-platform", "Render", "Hosted agency services"),
    (r"^vercel-|^nextjs|^next-|^turbopack|^shadcn|^runtime-cache|^routing-middleware|^react-best|^microfrontends|^marketplace|^knowledge-update|^eve$|^env-vars|^deployments-cicd|^chat-sdk|^cdn-caching|^bootstrap|^auth$|^ai-sdk|^ai-gateway|^access-protected|^workflow$|^verification$", "web-vercel", "Web Platform (Vercel/Next)", "prd", "cpo-product", "Vercel", "Inbound site + premium UI"),
    (r"^cloudflare|^wrangler|^workers-|^web-perf|^sandbox-sdk|^durable-objects|^building-mcp|^building-ai-agent|^agents-sdk$", "edge-cf", "Edge (Cloudflare)", "inf", "cto-platform", "Cloudflare-docs|Cloudflare-bindings|Cloudflare-builds|Cloudflare-observability", "Edge workers for tags/CAPI"),
    (r"^firebase|^xcode", "mobile-firebase", "Mobile & Firebase", "mob", "cpo-product", "Firebase", "App UA measurement adjacent"),
    (r"^clerk|^workos", "auth-identity", "Auth & Identity", "leg", "cto-platform", "Clerk|Workos", "SSO for agency tools"),
    (r"^gsap-", "motion-ui", "Motion Design (GSAP)", "cre", "cmo-brand", "None", "Landing/creative motion craft"),
    (r"^figma-", "design-figma", "Design (Figma)", "cre", "cmo-brand", "Figma|Canva", "Creative system → code"),
    (r"^slack-|^block-kit|^create-slack|^functions$", "collab-slack", "Collaboration (Slack)", "cls", "coo-delivery", "Slack", "7/24 standup channels"),
    (r"^huggingface|^hf-cli|^trl-|^transformers|^train-sentence", "ml-hf", "ML Platform (HF)", "dsc", "cdo-data", "Huggingface-skills", "Model evals / creative gen research"),
    (r"^temporal-", "workflow-temporal", "Durable Workflows", "inf", "cto-platform", "None", "Long-running agency jobs"),
    (r"^appwrite-", "baas-appwrite", "BaaS (Appwrite)", "prd", "cto-platform", "Appwrite-api|Appwrite-docs", "Lightweight backends"),
    (r"^browserstack|^scan-and-fix|^run-web-tests|^run-mobile-tests", "qa-browserstack", "QA & A11y", "prd", "coo-delivery", "Browserstack", "Landing QA before launch"),
    (r"^jfrog", "supply-jfrog", "Package Safety (JFrog)", "inf", "cto-platform", "Jfrog", "Dependency safety"),
    (r"^postman-|^agent-ready-apis$", "api-postman", "API Design (Postman)", "prd", "cto-platform", "Postman", "Connector API contracts"),
    (r"^opensearch", "search-opensearch", "OpenSearch", "inf", "cto-platform", "Opensearch-mcp-server", "Internal search"),
    (r"^deep-research", "research-core", "Deep Research", "str", "cso-strategy", "Exa", "Strategy research loops"),
    (r"^update-cursor|^update-cli|^statusline|^split-to-prs|^shell$|^review|^migrate-to-|^sdk$|^create-subagent|^create-skill|^create-rule|^create-hook|^canvas$|^babysit$", "cursor-meta", "Cursor Meta Tooling", "tal", "cto-platform", "cursor-cloud", "Agent DX for this repo"),
]

TITLE_LADDER = [
    ("evp", "EVP / Family Owner", "Owns OKRs, budget, external MCP auth"),
    ("dir", "Director", "Standards, playbooks, escalation"),
    ("lead", "Lead", "Assigns work, reviews DoD"),
    ("spc", "Specialist", "Executes skill workflows"),
    ("anl", "Analyst", "Monitors, reports, archives"),
]

# MCP servers known in this cloud agent environment (from system prompt)
MCP_CATALOG = {
    "Railway": {"use": "Deploy agency services", "min": "list services / deploy", "detail": "Bind 0.0.0.0:$PORT; ephemeral FS"},
    "Aws-mcp": {"use": "AWS control plane", "min": "describe resources", "detail": "Prefer knowledge MCP for docs"},
    "Azure": {"use": "Azure resources", "min": "resource lookup", "detail": "RBAC before mutate"},
    "Aurora-dsql": {"use": "Aurora DSQL", "min": "connect/query", "detail": "Serverless SQL patterns"},
    "Zscaler": {"use": "ZTE security", "min": "list services", "detail": "Write tools gated"},
    "Zscaler-mcp-server": {"use": "Zscaler alt", "min": "status", "detail": "Same OneAPI creds"},
    "Appwrite-api": {"use": "Appwrite API", "min": "CRUD", "detail": "Auth via project keys"},
    "Appwrite-docs": {"use": "Appwrite docs", "min": "search docs", "detail": "Read-only"},
    "Cockroachdb-toolbox": {"use": "CRDB ops", "min": "health", "detail": "SQL + cluster ops"},
    "Pinecone": {"use": "Vectors", "min": "query/upsert", "detail": "Namespace per dept"},
    "Encore-mcp": {"use": "Encore services", "min": "scaffold", "detail": "Go/TS APIs"},
    "Firebase": {"use": "Firebase", "min": "rules/auth", "detail": "Mobile-adjacent"},
    "Aws-serverless-mcp": {"use": "Lambda/API GW", "min": "deploy fn", "detail": "Serverless connectors"},
    "Mongodb": {"use": "MongoDB", "min": "query", "detail": "Schema design first"},
    "Awsiac": {"use": "IaC", "min": "plan", "detail": "No prod apply without approval"},
    "Awspricing": {"use": "Cost", "min": "price lookup", "detail": "FIN channel input"},
    "Browserstack": {"use": "Device QA", "min": "run test", "detail": "Landing a11y/QA"},
    "Convex": {"use": "Convex backend", "min": "dev schema", "detail": "Agent mode anonymous for cloud"},
    "Zoominfo": {"use": "B2B intel", "min": "search", "detail": "NBD enrichment"},
    "Mixpanel": {"use": "Product analytics", "min": "query events", "detail": "Alt to PostHog"},
    "Opensearch-mcp-server": {"use": "OpenSearch", "min": "search", "detail": "Internal knowledge"},
    "Ddg-search": {"use": "Web search", "min": "query", "detail": "Often unavailable; fallback WebSearch"},
    "Awslabs.aws-api-mcp-server": {"use": "AWS API", "min": "call API", "detail": "Prefer least privilege"},
    "Aws-knowledge-mcp-server": {"use": "AWS docs", "min": "search", "detail": "Canonical AWS guidance"},
    "Bright Data": {"use": "SERP/scrape", "min": "search_engine / scrape", "detail": "Prefer web_data_* when Pro"},
    "Prisma-Local": {"use": "Prisma local", "min": "migrate/generate", "detail": "Dev DB"},
    "Figma": {"use": "Design", "min": "get design", "detail": "CRE pipeline"},
    "Linear": {"use": "Issues", "min": "list/create", "detail": "Work tracking"},
    "Coralogix": {"use": "Logs/metrics", "min": "query", "detail": "Obs stack"},
    "Datadog": {"use": "APM", "min": "query metrics", "detail": "INF ownership"},
    "Monk": {"use": "Obs assistant", "min": "ask", "detail": "Grafana-adjacent"},
    "Twilio-docs": {"use": "Twilio docs", "min": "retrieve/search", "detail": "Comms playbooks"},
    "Vantage": {"use": "Cloud cost", "min": "cost query", "detail": "FIN"},
    "Paradedb": {"use": "ParadeDB docs", "min": "search", "detail": "Read-only docs"},
    "Awsknowledge": {"use": "AWS knowledge", "min": "search", "detail": "Docs"},
    "Workos": {"use": "Auth", "min": "org/user", "detail": "SSO"},
    "Turbopuffer": {"use": "Vectors", "min": "query", "detail": "Alt to Pinecone"},
    "Cockroachdb-toolbox-http": {"use": "CRDB HTTP", "min": "health", "detail": "Remote toolbox"},
    "Cockroachdb-cloud": {"use": "CRDB Cloud", "min": "cluster", "detail": "Provisioning"},
    "Render": {"use": "Host", "min": "deploy", "detail": "Web services"},
    "Jfrog": {"use": "Artifacts", "min": "scan", "detail": "Supply chain"},
    "Pagerduty-mcp": {"use": "Incidents", "min": "list incidents", "detail": "On-call"},
    "PlanetScale": {"use": "MySQL", "min": "query", "detail": "Branching DB"},
    "Clerk": {"use": "Auth SDK", "min": "snippets", "detail": "Frontend auth"},
    "Neon": {"use": "Postgres", "min": "branch/query", "detail": "Sponsor target"},
    "Supabase": {"use": "Supabase", "min": "sql/auth", "detail": "BaaS"},
    "Vercel": {"use": "Deploy", "min": "deploy/env", "detail": "Inbound site"},
    "Sentry": {"use": "Errors", "min": "issues", "detail": "Debug agents"},
    "Cloudflare-docs": {"use": "CF docs", "min": "search", "detail": "Workers guidance"},
    "Cloudflare-bindings": {"use": "CF bindings", "min": "list", "detail": "KV/R2/D1"},
    "Cloudflare-builds": {"use": "CF builds", "min": "status", "detail": "CI"},
    "Cloudflare-observability": {"use": "CF obs", "min": "query", "detail": "Workers logs"},
    "Observe": {"use": "Observe", "min": "query", "detail": "Host/K8s collection"},
    "Apify": {"use": "Actors", "min": "run actor", "detail": "Scraping actors"},
    "Confidence-flags": {"use": "Flags", "min": "evaluate", "detail": "Experimentation"},
    "Confidence-docs": {"use": "Confidence docs", "min": "search", "detail": "Onboarding"},
    "Grafana-cloud": {"use": "Grafana", "min": "dashboards", "detail": "patch not full update"},
    "Slack": {"use": "Slack", "min": "post/search", "detail": "Standups"},
    "Exa": {"use": "Web research", "min": "web_search_exa", "detail": "Rate-limited free tier"},
    "Spottercode": {"use": "Code spotter", "min": "docs", "detail": "API refs"},
    "Pendo-external": {"use": "Pendo", "min": "analytics", "detail": "Product adoption"},
    "Elastic-docs": {"use": "Elastic docs", "min": "search_docs", "detail": "ES/Kibana"},
    "Postman": {"use": "APIs", "min": "collections", "detail": "Contracts"},
    "Braintrust": {"use": "Evals", "min": "experiments", "detail": "LLM evals"},
    "Antimetal": {"use": "RCA", "min": "search_issues", "detail": "Needs API key"},
    "Azure-cosmosdb": {"use": "Cosmos", "min": "query", "detail": "NoSQL"},
    "Amplitude": {"use": "Product analytics", "min": "query", "detail": "Alt analytics"},
    "Huggingface-skills": {"use": "HF", "min": "models/datasets", "detail": "ML research"},
    "Posthog": {"use": "PostHog", "min": "query/flags", "detail": "Primary product analytics"},
    "Clickhouse": {"use": "CH", "min": "query", "detail": "OLAP"},
    "Snowflake": {"use": "Snowflake", "min": "query", "detail": "Warehouse"},
    "Gitbook": {"use": "Docs", "min": "search", "detail": "Knowledge"},
    "Hex": {"use": "Notebooks", "min": "query", "detail": "Analytics stories"},
    "Prisma-Remote": {"use": "Prisma remote", "min": "migrate", "detail": "Remote DB"},
    "Canva": {"use": "Design", "min": "create design", "detail": "Creative assets"},
    "Mintlify": {"use": "Docs site", "min": "search", "detail": "Product docs"},
    "Mintlify MCP": {"use": "Docs alt", "min": "search", "detail": "Same"},
    "ChatPRD": {"use": "PRDs", "min": "write/update", "detail": "Product specs"},
    "Tierzero": {"use": "Prod ask", "min": "tierzero_ask", "detail": "Grounded investigations"},
    "Harness": {"use": "CI/CD", "min": "harness_list", "detail": "Confirm org/project first"},
    "cursor-cloud": {"use": "Cloud agent meta", "min": "run-info", "detail": "This run diagnostics"},
}


def classify(skill: str) -> tuple:
    for pat, fid, fname, dept, owner, mcp, fit in FAMILY_RULES:
        if re.search(pat, skill):
            return fid, fname, dept, owner, mcp, fit
    return "misc-tools", "Miscellaneous Tools", "inf", "cto-platform", "None", "Parked until mapped"


def main() -> None:
    skills = sorted(set(re.findall(r"[a-z0-9][a-z0-9\-]+", RAW_SKILLS)))
    families: dict[str, dict] = {}
    skill_rows = []

    for s in skills:
        fid, fname, dept, owner, mcp, fit = classify(s)
        families.setdefault(fid, {
            "id": fid,
            "name": fname,
            "primary_dept": dept,
            "c_owner": owner,
            "mcp_hint": mcp,
            "product_fit": fit,
            "skills": [],
            "titles": [],
            "workflows": {
                "daily": f"Standup snippet for {fname}; sample 2 skills; stamp AUDIT_LOG",
                "weekly": f"Family lead sync with {owner}; risks + MCP auth status",
                "monthly": "Read data/arsiv/YYYY-MM → refresh skill notes → re-stamp",
                "on_demand": "Pick skill → load skill file if present → execute with MCP if auth'd else 🚩",
            },
            "prompt_ids": {
                "title": f"T-{dept}-intake-001",
                "team": f"E-{dept}-plan-003",
                "apply": f"U-{dept}-execute-004",
            },
        })
        if not families[fid]["titles"]:
            for i, (t, title, mission) in enumerate(TITLE_LADDER):
                families[fid]["titles"].append({
                    "tier": t,
                    "title": title,
                    "mission": mission,
                    "slug": f"{fid}-{t}",
                    "reports_to": None if i == 0 else f"{fid}-{TITLE_LADDER[i-1][0]}",
                })

        families[fid]["skills"].append(s)
        skill_rows.append({
            "skill": s,
            "family": fid,
            "dept": dept,
            "c_owner": owner,
            "mcp": mcp,
            "status": "routed",
        })

    # MCP catalog with skill family bindings
    mcp_out = []
    for name, meta in sorted(MCP_CATALOG.items()):
        bound = [f["id"] for f in families.values() if name.split()[0].lower() in f["mcp_hint"].lower() or name.lower() in f["mcp_hint"].lower()]
        mcp_out.append({
            "server": name,
            "minimum": meta["min"],
            "detailed": meta["detail"],
            "agency_use": meta["use"],
            "bound_families": bound,
            "auth_note": "Call GetMcpTools first; if needsAuth → ask owner to authorize in Cursor MCP settings",
        })

    payload = {
        "_meta": {
            "ts": TS,
            "skill_count": len(skills),
            "family_count": len(families),
            "mcp_count": len(mcp_out),
            "policy": "K-003: route & operate; do not invent top-100 people; do not pad prompts; auth-gated MCPs 🚩 until connected",
            "note_tr": "Her skill ailesi mini LLM ajansı: EVP→Analyst + günlük/haftalık/aylık döngü. 900B karakter talebi reddedildi.",
        },
        "families": list(families.values()),
        "skills": skill_rows,
        "mcps": mcp_out,
    }

    out_json = ROOT / "data" / "skill_agency_registry.json"
    out_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Markdown index
    lines = [
        f"# SKILL AGENCY REGISTRY — {len(skills)} skills → {len(families)} mini-ajans",
        f"> Damga: {TS} · Politika: {payload['_meta']['policy']}",
        "",
        "## TR",
        payload["_meta"]["note_tr"],
        "",
        "## Aileler (özet)",
        "| Family | Skills | Dept | C-owner | MCP |",
        "|---|---:|---|---|---|",
    ]
    for f in sorted(families.values(), key=lambda x: -len(x["skills"])):
        lines.append(
            f"| `{f['id']}` {f['name']} | {len(f['skills'])} | {f['primary_dept']} | {f['c_owner']} | {f['mcp_hint']} |"
        )
    lines += ["", "## Title ladder (her aile)", ""]
    for t, title, mission in TITLE_LADDER:
        lines.append(f"- **{t}** — {title}: {mission}")
    lines += ["", "## MCP (minimum + detay)", ""]
    for m in mcp_out[:25]:
        lines.append(f"- **{m['server']}** — min: `{m['minimum']}` · {m['detailed']}")
    lines.append(f"- … toplam {len(mcp_out)} MCP — tam liste: `data/skill_agency_registry.json`")
    lines += [
        "",
        "## 7/24 döngü",
        "1. Daily: family standup satırı → gundem/",
        "2. Weekly: C-owner sync",
        "3. Monthly: `scripts/monthly_research_refresh.py` + bu registry yeniden üretim",
        "4. Her öğrenim: BILGI_TABANI append + arşiv damgası",
        "",
        "## 🚩",
        "- Skill'i 'çalıştır' = ilgili skill dosyasını oku + MCP auth varsa çağır; yoksa red-flag.",
        "- Top-100 kişi / 900M+ karakter prompt üretilmez (K-003).",
    ]
    (ROOT / "docs" / "SKILL-AGENCY-REGISTRY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Per-family operating prompts (dense, not padded)
    fam_prompts = []
    for f in families.values():
        fam_prompts.append({
            "id": f"FAM-{f['id']}",
            "family": f["id"],
            "prompt": f"""
You are the {f['name']} mini-agency inside AdOps Agents.
Titles: {', '.join(t['slug'] for t in f['titles'])}.
Owner: {f['c_owner']} · Dept: {f['primary_dept']} · MCP: {f['mcp_hint']}.
Product fit: {f['product_fit']}.
Skills in scope ({len(f['skills'])}): {', '.join(f['skills'][:12])}{'…' if len(f['skills'])>12 else ''}.

LOOP:
1) Read data/arsiv/{YM}/ + BILGI_TABANI.md tail
2) Pick skill → locate Cursor skill path if available → follow it
3) GetMcpTools for bound MCP; if needsAuth → 🚩 auth · ask owner · continue without live call
4) Produce artifact; stamp AUDIT_LOG; append learning
5) Escalate blockers >4h to {f['c_owner']}

Do NOT invent people lists. Do NOT pad text. Expand detail from role cards + real docs only.
""".strip(),
        })
    (ROOT / "data" / "prompt_bank" / "skill_families.json").write_text(
        json.dumps({"_meta": {"ts": TS, "count": len(fam_prompts)}, "prompts": fam_prompts},
                   ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    # Archive note
    arsiv = ROOT / "data" / "arsiv" / YM
    arsiv.mkdir(parents=True, exist_ok=True)
    snap_path = arsiv / "skill_agency_snapshot.json"
    snap_path.write_text(json.dumps({
        "ts": TS,
        "skills": len(skills),
        "families": len(families),
        "mcps": len(mcp_out),
        "top_families": sorted(((f["id"], len(f["skills"])) for f in families.values()), key=lambda x: -x[1])[:15],
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Expand activation doc
    act = ROOT / "docs" / "CLAUDE-CODE-AKTIVASYON.md"
    block = f"""

---

## v2.9 Skill Agency Router (yapıştır ek)
> Damga: {TS}

```
SKILL AGENCY MODE (v2.9):
- Registry: data/skill_agency_registry.json ({len(skills)} skills / {len(families)} families)
- Family prompts: data/prompt_bank/skill_families.json
- Index: docs/SKILL-AGENCY-REGISTRY.md
- MCP catalog: registry.mcps[] (minimum + detailed + auth_note)

When user names a /skill:
1) Lookup skill in registry.skills[] → family
2) Load FAM-<family> prompt
3) Use title ladder EVP→Analyst for RACI
4) Call MCP only after GetMcpTools; needsAuth → 🚩
5) Archive + timestamp protocol mandatory

GitHub: open issues with label lead|skill-agency; PRs via ManagePullRequest only from cloud agent tooling.
```
"""
    text = act.read_text(encoding="utf-8")
    if "v2.9 Skill Agency Router" not in text:
        act.write_text(text.rstrip() + block, encoding="utf-8")

    print(f"OK skills={len(skills)} families={len(families)} mcps={len(mcp_out)} ts={TS}")


if __name__ == "__main__":
    main()
