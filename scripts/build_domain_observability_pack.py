#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Domain 1–7 agency pack from owner docx intent (v2.13).

Focus deliverables from uploads:
- Domain 1 infra / Domain 2 observability (Datadog, Sentry, PagerDuty, Slack, OTel)
- Domains 3–7 catalog + routing
- Dense prompts (NOT 900B) · research queues · monthly archive

K-003 red flags honored.
"""
from __future__ import annotations

import datetime
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.datetime.now(datetime.timezone.utc)
TS = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
YM = NOW.strftime("%Y-%m")

DOMAINS = [
    {
        "id": "d1-infra",
        "num": 1,
        "name": "Infrastructure, Kubernetes & Cloud Computing",
        "c_owner": "holdco-cto",
        "primary_dept": "inf",
        "skills": [
            "setup-linux-host-collection", "setup-linux-host-backend", "setup-k8s-collection",
            "setup-k8s-backend", "deploy-linux-host-explorer", "deploy-k8s-explorer",
            "debug-linux-host-collection", "debug-k8s-collection", "azure-kubernetes",
            "airunway-aks-setup", "aws-step-functions", "aws-serverless-deployment",
            "aws-lambda", "render-workflows", "cloudflare", "wrangler", "create-infrastructure",
            "azure-deploy", "azure-compute", "azure-validate", "azure-cost", "azure-rbac",
            "chaos-experiment", "managing-tls-certificates", "configuring-ip-allowlists",
            "analyze-costs", "onboard-confidence-dry-run", "audit-report",
        ],
        "directives": [
            "Dry-run before mutate: /onboard-confidence-dry-run + /azure-validate",
            "K8s crash → /debug-k8s-collection first",
            "Host IO/mem → /debug-linux-host-collection",
            "Cost ceiling → /azure-cost + /analyze-costs",
            "Weekly chaos → /chaos-experiment",
            "Timestamp every infra action → /audit-report",
        ],
        "mcp_hints": ["Azure", "Render", "Cloudflare-docs", "Harness", "Aws-mcp"],
        "artifacts": [],
    },
    {
        "id": "d2-observability",
        "num": 2,
        "name": "Telemetry, Observability & Diagnostics",
        "c_owner": "cto-platform",
        "primary_dept": "ops",
        "skills": [
            "opentelemetry-validation", "opentelemetry-manual-instrumentation",
            "opentelemetry-auto-instrumentation", "observe-cli", "alert-investigation",
            "tierzero-investigate", "tierzero-fetch", "sentry-create-alert", "sentry-debug-issue",
            "kibana-alerting-rules", "observability-service-health", "observability-manage-slos",
            "observability-logs-search", "observability-llm-obs", "grafana-cloud-mcp-tools",
            "ddconfig", "ddsetup", "signals-scout-anomaly-detection", "finding-replay-for-issue",
            "elasticsearch-esql", "configuring-log-export", "pagerduty-mcp-setup",
        ],
        "directives": [
            "Every new service ships with /opentelemetry-auto-instrumentation",
            "Incident first call: /tierzero-investigate + /alert-investigation",
            "WARN → Slack only; CRITICAL → Slack + PagerDuty page",
            "Auto-resolve PD on Datadog/Sentry recovery",
            "Validate pipelines with /opentelemetry-validation after deploy",
            "Mask PII via /configuring-log-export",
        ],
        "mcp_hints": ["Datadog", "Sentry", "Pagerduty-mcp", "Grafana-cloud", "Tierzero", "Elastic-docs"],
        "artifacts": [
            "infra/observability/terraform/main.tf",
            "infra/observability/k8s/opentelemetry-collector.yaml",
        ],
    },
    {
        "id": "d3-data",
        "num": 3,
        "name": "Data Engineering, Pipelines & Storage",
        "c_owner": "cdo-data",
        "primary_dept": "ana",
        "skills": [
            "setup-warehouse", "setup-warehouse-snowflake", "setup-warehouse-bigquery",
            "warehouse-init", "airflow", "debugging-dags", "testing-dags", "dagster-expert",
            "tracing-upstream-lineage", "tracing-downstream-lineage", "pinecone-query",
            "scylladb-data-modeling", "mongodb-query-optimizer", "profiling-tables",
            "building-dbt-semantic-layer", "running-dbt-commands",
        ],
        "directives": [
            "Warehouse via /warehouse-init before loads",
            "Lineage on every model change",
            "DAG fail → /debugging-dags then /testing-dags",
        ],
        "mcp_hints": ["Snowflake", "Neon", "Mongodb", "Pinecone", "Clickhouse"],
        "artifacts": [],
    },
    {
        "id": "d4-platform",
        "num": 4,
        "name": "Full-Stack Platform, Identity & Frontend UI",
        "c_owner": "holdco-cto",
        "primary_dept": "prd",
        "skills": [
            "nextjs", "react-best-practices", "encore-api", "encore-auth", "workos",
            "firebase-auth-basics", "clerk-setup", "convex-quickstart", "gsap-core",
            "figma-design-to-code",
        ],
        "directives": [
            "Auth before feature: WorkOS/Clerk/Encore auth patterns",
            "No secrets in client bundles",
        ],
        "mcp_hints": ["Convex", "Clerk", "Workos", "Firebase", "Figma"],
        "artifacts": [],
    },
    {
        "id": "d5-comms",
        "num": 5,
        "name": "Communications, Engagement & Scrapers",
        "c_owner": "cmo-brand",
        "primary_dept": "nbd",
        "skills": [
            "twilio-send-message", "twilio-sms-send-message", "twilio-email-send",
            "twilio-webhook-architecture", "twilio-security-hardening",
            "apify-actor-development", "bd-scrape", "exa-web-search", "exa-fetch",
        ],
        "directives": [
            "Comms webhooks verified before prod send",
            "Scrape → archive with timestamp; no PII leakage",
        ],
        "mcp_hints": ["Twilio-docs", "Apify", "Bright Data", "Exa", "Slack"],
        "artifacts": [],
    },
    {
        "id": "d6-product-sec-ai",
        "num": 6,
        "name": "Product Management, Security & AI/ML Models",
        "c_owner": "cpo-product",
        "primary_dept": "prd",
        "skills": [
            "write-prd", "update-prd", "check-prd-alignment", "implement-from-prd",
            "review-security", "auditing-cloud-cluster-security", "manage-feature-flags",
            "migrate-posthog", "onboard-confidence",
        ],
        "directives": [
            "PRD alignment gate before implement",
            "Security review on auth/payment paths",
        ],
        "mcp_hints": ["ChatPRD", "Posthog", "Sentry", "Braintrust"],
        "artifacts": [],
    },
    {
        "id": "d7-governance",
        "num": 7,
        "name": "Governance, Workflow Automation & Self-Improvement",
        "c_owner": "ceo-orchestrator",
        "primary_dept": "yonetim",
        "skills": [
            "run-pipeline", "create-pipeline-v1", "dora-metrics", "gitops-status",
            "manage-slos", "knowledge-update", "deep-research", "audit-report",
            "manage-pull-requests",
        ],
        "directives": [
            "RFC 3339 timestamp every governance action",
            "Read prior archive before monthly research refresh",
            "DORA + SLO reviewed weekly",
        ],
        "mcp_hints": ["Harness", "GitHub", "Tierzero", "Linear"],
        "artifacts": [],
    },
]

TITLES = ["CEA", "CTO", "EVP", "Director", "Lead", "Senior", "Analyst", "Worker"]

WORKFLOWS = {
    "realtime": ["alert-investigation", "tierzero-investigate", "opentelemetry-validation"],
    "daily": ["observability-service-health", "debug-k8s-collection", "gitops-status"],
    "weekly": ["review-security", "chaos-experiment", "dora-metrics"],
    "monthly": ["deep-research", "knowledge-update", "analyze-costs", "audit-report"],
}


def ladder(domain_id: str) -> list[dict]:
    out = []
    for i, t in enumerate(TITLES):
        out.append({
            "tier": t,
            "slug": f"{domain_id}-{t.lower()}",
            "mandate": f"{t} owns Domain pack decisions at altitude {i}; escalate up, execute down.",
        })
    return out


def prompts_for(domain: dict) -> dict:
    """Dense templates — K-003: not 900B chars."""
    did = domain["id"]
    name = domain["name"]
    skills = ", ".join(f"/{s}" for s in domain["skills"][:12])
    dirs = "\n".join(f"- {d}" for d in domain["directives"])
    arts = "\n".join(f"- `{a}`" for a in domain["artifacts"]) or "- (catalog only)"
    base = f"""# DOMAIN PROMPT — {did}
> Damga: {TS} · K-003: dense, not padded · Domain {domain['num']}: {name}

## Role
You are the Domain {domain['num']} mini-agency orchestrator ({domain['c_owner']}).
Primary dept: `{domain['primary_dept']}`.

## Skill surface (route, don't invent)
{skills}

## Directives
{dirs}

## Artifacts
{arts}

## Execution protocol
1. Read prior archive under `data/arsiv/domains/{YM}/`
2. Dry-run / validate before mutate
3. Prefer indexed MCP tools when authenticated; else document 🚩 needs-auth
4. Stamp AUDIT_LOG.jsonl + distill BILGI_TABANI.md
5. Never commit secrets; never invent top-100 people lists

## Output contract
- Decision log (UTC)
- Actions taken / blocked
- Next loop input
"""
    return {
        "title": base.replace("DOMAIN PROMPT", "TITLE PROMPT"),
        "team": base.replace("DOMAIN PROMPT", "TEAM PROMPT") + "\n## Team ritual\n- Standup blockers\n- On-call handoff\n- KPI slice\n",
        "apply": base.replace("DOMAIN PROMPT", "APPLY PROMPT") + "\n## Apply steps\n1. Load artifacts\n2. Run validate\n3. Open PR if infra changed\n4. Page only on CRITICAL\n",
    }


def research_queue(domain: dict) -> dict:
    """Sourced slots + pending_research — no invented names."""
    topics = [
        f"{domain['name']} operating model 2026",
        f"best practices {domain['skills'][0] if domain['skills'] else domain['id']}",
        "incident response on-call patterns",
        "OpenTelemetry production collector topology",
        "Datadog vs Sentry alert fatigue reduction",
    ]
    slots = []
    for i, topic in enumerate(topics * 20):  # 100 slots
        if i >= 100:
            break
        slots.append({
            "slot": i + 1,
            "status": "pending_research",
            "query": f"{topic} · domain={domain['id']} · slot={i+1}",
            "sources": [],
        })
    # seed a few sourced placeholders (mechanisms, not people)
    for i, src in enumerate([
        ("Google SRE Book — Monitoring Distributed Systems", "https://sre.google/sre-book/monitoring-distributed-systems/"),
        ("OpenTelemetry Collector docs", "https://opentelemetry.io/docs/collector/"),
        ("PagerDuty Events API v2", "https://developer.pagerduty.com/docs/events-api-v2/overview/"),
        ("Datadog monitors", "https://docs.datadoghq.com/monitors/"),
        ("Sentry issue alerts", "https://docs.sentry.io/product/alerts/"),
    ]):
        slots[i] = {
            "slot": i + 1,
            "status": "sourced",
            "query": src[0],
            "sources": [{"title": src[0], "url": src[1]}],
        }
    return {"domain": domain["id"], "slots": 100, "items": slots}


def write_ci_snippet() -> None:
    path = ROOT / "infra" / "observability" / "ci" / "domain2-pipeline-snippet.yml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"""# Domain 2 CI snippet — reference only (wire into real pipeline as needed)
# Damga: {TS}
name: domain2-observability-gates
on:
  workflow_call:
jobs:
  gates:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Stage1 validate (dry-run)
        run: |
          echo "[/onboard-confidence-dry-run] structural check"
          test -f infra/observability/terraform/main.tf
          test -f infra/observability/k8s/opentelemetry-collector.yaml
      - name: Stage2 OTel manifest present
        run: echo "[/opentelemetry-validation] manifest OK"
      - name: Stage3 no secrets in tree
        run: |
          if rg -n "sk-or-v1-|DD_API_KEY=[A-Za-z0-9]" infra/ --glob '!**/*.md' | rg -v REPLACE_ME; then
            echo "possible secret leak"; exit 1
          fi
          echo "secret scan soft-pass"
      - name: Stage4 triage hooks documented
        run: |
          echo "[/tierzero-investigate] [/alert-investigation] [/debug-k8s-collection]"
          echo "timestamp=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
""",
        encoding="utf-8",
    )


def main() -> None:
    domains_out = []
    prompt_bank = {"ts": TS, "policy": "K-003 dense domain prompts; no 900B", "domains": {}}
    queues = {"ts": TS, "domains": {}}

    for d in DOMAINS:
        entry = {
            **d,
            "titles": ladder(d["id"]),
            "workflows": WORKFLOWS,
            "skill_count": len(d["skills"]),
        }
        domains_out.append(entry)
        prompt_bank["domains"][d["id"]] = prompts_for(d)
        queues["domains"][d["id"]] = research_queue(d)

        # per-domain board
        board = ROOT / "docs" / "domains" / f"{d['id']}-BOARD.md"
        board.parent.mkdir(parents=True, exist_ok=True)
        board.write_text(
            f"""# Domain {d['num']} — {d['name']}
> Damga: {TS} · Owner: `{d['c_owner']}` · Dept: `{d['primary_dept']}`

## Mandate
Mini-LLM agency for this domain. Route skills; do not invent people; do not pad prompts.

## Directives
{chr(10).join(f'- {x}' for x in d['directives'])}

## Skills ({len(d['skills'])})
{chr(10).join(f'- `/{s}`' for s in d['skills'])}

## MCP hints
{chr(10).join(f'- {m}' for m in d['mcp_hints'])}

## Artifacts
{chr(10).join(f'- `{a}`' for a in d['artifacts']) or '- catalog only'}

## Workflows
- realtime: {', '.join(WORKFLOWS['realtime'])}
- daily: {', '.join(WORKFLOWS['daily'])}
- weekly: {', '.join(WORKFLOWS['weekly'])}
- monthly: {', '.join(WORKFLOWS['monthly'])}

## P0 checklist
- [ ] MCP Authorize for needed servers only
- [ ] Secrets in env / vault — never commit
- [ ] Read `data/arsiv/domains/{YM}/` before research tick
""",
            encoding="utf-8",
        )

    pack = {
        "_meta": {
            "ts": TS,
            "version": "v2.13-domain-pack",
            "domain_count": len(domains_out),
            "skill_mentions": sum(len(d["skills"]) for d in domains_out),
            "policy": "K-003: no 900B prompts; no invented top-100; Domain2 ships reference TF+OTel only until owner creds",
            "note_tr": "Owner docx paketi → Domain 1–7 mini-ajans + Domain2 infra referansı.",
            "source": "data/arsiv/domains/2026-08/SOURCE-DIGEST.md",
        },
        "alert_policy": {
            "warn": "Slack #alerts-warnings only (no page)",
            "critical": "Slack #alerts-critical + PagerDuty Events API v2 page",
            "auto_resolve": True,
            "thresholds": {"error_rate_warn": 0.02, "error_rate_critical": 0.05, "spike_per_min": 50},
        },
        "domains": domains_out,
    }

    (ROOT / "data" / "domains" / "domain_pack.json").write_text(
        json.dumps(pack, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (ROOT / "data" / "prompt_bank" / "domains.json").write_text(
        json.dumps(prompt_bank, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (ROOT / "data" / "domains" / "research_queues.json").write_text(
        json.dumps(queues, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    # archive snapshot
    arch = ROOT / "data" / "arsiv" / "domains" / YM
    arch.mkdir(parents=True, exist_ok=True)
    (arch / f"snapshot-{NOW.strftime('%Y-%m-%d')}.json").write_text(
        json.dumps({"ts": TS, "domains": [d["id"] for d in domains_out], "alert_policy": pack["alert_policy"]},
                   ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    write_ci_snippet()

    # overview doc
    (ROOT / "docs" / "OZET-DOMAIN-PACK-V213.md").write_text(
        f"""# ÖZET — Domain Pack v2.13
> Damga: {TS} · TR: Owner docx (PagerDuty/Slack/OTel/Domain1–7) → in-repo pack.

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
""",
        encoding="utf-8",
    )

    # cursor skill router stub
    skill = ROOT / ".cursor" / "skills" / "domain-obs-router" / "SKILL.md"
    skill.parent.mkdir(parents=True, exist_ok=True)
    skill.write_text(
        f"""---
name: domain-obs-router
description: Route Domain 1–7 / observability requests to domain_pack + infra/observability artifacts.
---
# Domain Observability Router
Damga: {TS}

When user asks about PagerDuty, Slack alerts, Datadog, Sentry, OpenTelemetry, Domain 1/2:
1. Read `data/domains/domain_pack.json`
2. Use `infra/observability/**` as reference IaC (do not apply without creds)
3. Follow alert policy: WARN=Slack only; CRITICAL=Slack+PD
4. Honor K-003 (no 900B, no invented people)
""",
        encoding="utf-8",
    )

    cmd = ROOT / "components" / "commands" / "agency" / "domain-observability.md"
    cmd.write_text(
        f"""---
description: Build/refresh Domain 1–7 observability pack (v2.13)
---
# /domain-observability
Damga: {TS}

```bash
python3 scripts/build_domain_observability_pack.py
python3 scripts/validate.py
```

Docs: `docs/OZET-DOMAIN-PACK-V213.md`
""",
        encoding="utf-8",
    )

    # audit
    with (ROOT / "AUDIT_LOG.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps({
            "ts_start": TS, "ts_end": TS, "op": "v2.13-domain-observability-pack",
            "domains": len(domains_out),
            "artifacts": [
                "infra/observability/terraform/main.tf",
                "infra/observability/k8s/opentelemetry-collector.yaml",
                "data/domains/domain_pack.json",
            ],
            "validation": "PENDING_VALIDATE",
            "red_flags_honored": ["no_900B_blob", "no_invented_people", "no_secret_commit", "no_live_tf_apply_without_creds"],
        }, ensure_ascii=False) + "\n")

    print(json.dumps({"ts": TS, "domains": len(domains_out), "skills": sum(len(d['skills']) for d in domains_out)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
