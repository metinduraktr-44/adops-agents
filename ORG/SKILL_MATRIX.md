# SKILL_MATRIX

Türkçe not: Cursor skill/MCP dump → family mini-ajans matrisi. Canlı “hepsini çalıştır” yok.
> Damga: 2026-11-15T11:07:36Z · Kaynak: `data/skill_agency_registry.json` (696 skills / 43 families / 81 MCPs)

## Creative RACI (baseline)

| Capability \ Role | CD | Copy | Design | Strategy | QA |
|---|:--:|:--:|:--:|:--:|:--:|
| Concept development | ✓ | ○ | ○ | ○ |  |
| Copywriting |  | ✓ |  | ○ |  |
| Art direction / layout | ✓ |  | ✓ |  |  |
| Brand guardrails | ○ | ○ | ○ |  | ✓ |
| Spec validation |  |  | ○ |  | ✓ |
| Research / insight |  |  |  | ✓ |  |

## Owner slash/MCP dump → mini-agency

| Command family | Mini-agency | Not |
|---|---|---|
| `/status /deploy /env /domains` | `web-vercel` | Vercel Doctor + deploy — link required; no purchase without domain |
| `/workflows /diff /tasks /plan /fast` | `cursor-meta` | Cursor meta — stamp via registry; no live-all |
| `/skills dump (all plugins)` | `cursor-meta → family router` | skill-agency-router; family mini-agency only |
| `brand-voice / creative` | `design-figma + Creative OS` | CANVA:BRIEF-ONLY; no invent brand data |
| `windsor / analytics connectors` | `bi-analytics / product-analytics` | MCP needsAuth → 🚩 catalog only |
| `pdf-viewer / sign-fill` | `product-docs` | No unsigned PDF sign; upload gate |
| `firecrawl / apify / exa / bright-data` | `web-intel` | Archive-first research_loop; Exa needsAuth |
| `twilio-*` | `comms-twilio` | Auth required before send |
| `harness / cicd` | `cicd-harness` | Read schema before write |
| `security /sec-*` | `Security GIGA (ASSESS-ONLY)` | ethics-checker; no exploit |
| `latos-*` | `LATOS GIGA` | generators + pending_research; K-003 |
| `holding / opco` | `holding-agency-router` | data/holding.json v2.10 |

## Family catalog (EVP→Analyst)

| Family | Name | Skills | Dept | C-owner | MCP hint |
|---|---|---:|---|---|---|
| `product-analytics` | Product Analytics (PostHog) | 108 | ana | cdo-data | Posthog |
| `comms-twilio` | Comms & Messaging (Twilio) | 56 | cls | cro-revenue | Twilio-docs |
| `db-relational` | Relational DB & ORM | 48 | inf | cto-platform | Supabase|Prisma-Local|Prisma-Remote|Neon|PlanetScale |
| `obs-elastic` | Search & SecOps (Elastic) | 35 | inf | cto-platform | Elastic-docs|Coralogix |
| `data-pipeline` | Data Pipelines (Airflow/dbt) | 33 | dsc | cdo-data | None |
| `web-vercel` | Web Platform (Vercel/Next) | 31 | prd | cpo-product | Vercel |
| `cloud-azure` | Cloud (Azure) | 31 | inf | cto-platform | Azure|Azure-cosmosdb|Aurora-dsql |
| `db-cockroach` | Distributed SQL (Cockroach) | 30 | inf | cto-platform | Cockroachdb-toolbox|Cockroachdb-cloud |
| `cicd-harness` | CI/CD (Harness) | 27 | inf | cto-platform | Harness |
| `web-intel` | Web Intelligence & Scraping | 24 | seo | cso-strategy | Bright Data|Apify|Exa|Firecrawl |
| `auth-identity` | Auth & Identity | 22 | leg | cto-platform | Clerk|Workos |
| `backend-encore` | Backend (Encore) | 21 | prd | cto-platform | Encore-mcp |
| `cloud-render` | Cloud (Render) | 21 | inf | cto-platform | Render |
| `ml-hf` | ML Platform (HF) | 18 | dsc | cdo-data | Huggingface-skills |
| `cursor-meta` | Cursor Meta Tooling | 17 | tal | cto-platform | cursor-cloud |
| `obs-observe` | Observability (Observe) | 16 | inf | cto-platform | Observe |
| `design-figma` | Design (Figma) | 12 | cre | cmo-brand | Figma|Canva |
| `bi-analytics` | BI & Notebooks | 12 | ana | cdo-data | Snowflake|Hex|Omni |
| `mobile-firebase` | Mobile & Firebase | 11 | mob | cpo-product | Firebase |
| `cloud-aws` | Cloud (AWS) | 10 | inf | cto-platform | Aws-mcp|Awsiac|Awspricing|Awslabs.aws-api-mcp-server|Aws-knowledge-mcp-server|Aws-serverless-mcp|Awsknowledge |
| `baas-appwrite` | BaaS (Appwrite) | 10 | prd | cto-platform | Appwrite-api|Appwrite-docs |
| `edge-cf` | Edge (Cloudflare) | 9 | inf | cto-platform | Cloudflare-docs|Cloudflare-bindings|Cloudflare-builds|Cloudflare-observability |
| `vector-ai` | Vector Search | 9 | dsc | cdo-data | Pinecone|Turbopuffer |
| `olap-clickhouse` | OLAP (ClickHouse) | 8 | dsc | cdo-data | Clickhouse |
| `motion-ui` | Motion Design (GSAP) | 8 | cre | cmo-brand | None |
| `experimentation` | Experimentation & Flags | 8 | cro | cpo-product | Confidence-flags|Posthog |
| `db-mongo` | MongoDB Atlas | 7 | inf | cto-platform | Mongodb |
| `collab-slack` | Collaboration (Slack) | 7 | cls | coo-delivery | Slack |
| `product-docs` | Product Spec & Docs | 7 | prd | cpo-product | ChatPRD|Mintlify |
| `obs-sentry` | Error Tracking (Sentry) | 7 | inf | cto-platform | Sentry |
| `backend-convex` | Backend (Convex) | 5 | prd | cto-platform | Convex |
| `api-postman` | API Design (Postman) | 3 | prd | cto-platform | Postman |
| `obs-antimetal` | Infra RCA (Antimetal) | 3 | inf | cto-platform | Antimetal |
| `obs-datadog` | APM (Datadog) | 3 | inf | cto-platform | Datadog |
| `obs-grafana` | Observability (Grafana) | 3 | inf | cto-platform | Grafana-cloud |
| `supply-jfrog` | Package Safety (JFrog) | 3 | inf | cto-platform | Jfrog |
| `qa-browserstack` | QA & A11y | 3 | prd | coo-delivery | Browserstack |
| `db-scylla` | ScyllaDB | 3 | inf | cto-platform | None |
| `workflow-temporal` | Durable Workflows | 2 | inf | cto-platform | None |
| `obs-tierzero` | Prod Investigation (TierZero) | 2 | inf | cto-platform | Tierzero |
| `research-core` | Deep Research | 1 | str | cso-strategy | Exa |
| `search-opensearch` | OpenSearch | 1 | inf | cto-platform | Opensearch-mcp-server |
| `ops-pagerduty` | Incident Mgmt (PagerDuty) | 1 | ops | coo-delivery | Pagerduty-mcp |

## Ladder
EVP → Director → Lead → Specialist → Analyst · günlük/haftalık/aylık stamp (`scripts/research_loop_continue.py`).

## 🚩
- Live-all-skills / 900M prompts / invented top-100 → refuse (K-003)
- Vercel `purchase_*` without domain name → refuse
- MCP needsAuth → red-flag + docs-only

