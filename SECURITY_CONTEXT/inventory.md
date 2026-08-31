# Security Context — Inventory (defense perspective)

> HAND_AUTHORED · Damga: 2026-08-27T12:55:00Z · MODE=ASSESS-ONLY · no secret values

## Repo type
- Claude Code / Cursor component pack + agency automation (`adops-agents`)
- Content-heavy: ~1700+ Markdown, ~90 JSON, ~25 Python, ~16 CI YAML, Bash hooks
- Runtime assumption: Python **stdlib** for gate scripts; `package.json` has validate/stamp/nightly only (no app runtime deps)
- Coexists with Creative/Canva GIGA (`STATE.md` / Canva MCP) — security uses **`SECURITY_STATE.md`**

## Languages & surfaces (scan 2026-08-27)
| Class | Count (approx) | Notes |
|---|---|---|
| Markdown | ~1723 | Agents, docs, controls, skills |
| JSON | ~89 | org, holding, prompt_bank, queues |
| Python | ~25 | validate, scanners, generators, ops |
| GitHub Actions YAML | 14 workflows | incl. `security-audit.yml` |
| Shell | ~7 | nightly, hooks |
| Terraform | 1 | `infra/observability/terraform/main.tf` (reference) |

## Assets to protect
| Asset class | Path / surface | Notes |
|---|---|---|
| Org model | `data/org.json` | 600 agents — change only via `generate_org.py` |
| Prompt banks | `data/prompt_bank/` | IP / operational prompts |
| Holding model | `data/holding.json` | OpCo + country LLM agencies |
| Skill registry | `data/skill_agency_registry.json` | routing |
| Audit chain | `AUDIT_LOG.jsonl`, `BILGI_TABANI.md` | integrity |
| Security controls | `LAYERS/` … `CONDITIONAL/` (6×100) | draft · needs_expert_review |
| Cursor config | `.cursor/` | rules, hooks, skills, MCP URLs |
| CI | `.github/workflows/` | supply chain + SARIF upload |
| Observability IaC | `infra/observability/terraform/` | sensitive vars via TF variables / env — never commit values |
| Secrets | env / MCP Authorize / Actions secrets | `${VAR}` / `${{ secrets.* }}` only |

## Auth / secret handling patterns (location + type only)
| Location | Type | Handling |
|---|---|---|
| `scripts/llm_client.py` | Env API keys (`GEMINI_*`, `OPENROUTER_*`, `ANTHROPIC_*`) | Read from env; no hardcoded values observed in scan |
| `scripts/seed_issues.py` | `GITHUB_TOKEN` | Actions-provided |
| `scripts/seed_project_items.py` | `PROJECTS_TOKEN` | Env; Projects v2 PAT required (documented) |
| `infra/.../main.tf` | TF sensitive vars (Datadog/Sentry/PagerDuty) | `sensitive = true`; provider token via env |
| `.cursor/mcp.json` | Optional security MCP Bearer | Placeholder `${SECURITY_MCP_TOKEN}` — catalog **off** |
| `.cursor/hooks.json` | N/A | Runs `secret_scan.py` + `ethics_check.py` on edit |

## Trust boundaries
- Public GitHub remote vs local workspace
- MCP servers (OAuth by owner) vs local files — Canva on; security MCP off by default
- Generated automation writes (daily_ops, nightly, holding) vs human review
- CI `GITHUB_TOKEN` (contents/read + security-events/write for SARIF) vs elevated PATs

## CI inventory (defense view)
| Workflow | Purpose |
|---|---|
| `validate-components.yml` | Structural gate |
| `security-audit.yml` | Weekly validate + SARIF upload |
| `seed-600.yml` / `seed-auto.yml` | Org seed automation |
| `gunluk-operasyon.yml` / `nightly-improve.yml` | Ops rhythm |
| Holding / domain workflows | Research & consolidate |

## Ingestion method
Path + workflow + auth-pattern scan · README/AGENTS · **no credential probing**. Any incidental secret → location+type only, value `<REDACTED>`.

## Gaps for next `/sec-devam`
- [ ] Per-OpCo data classification overlay (holding)
- [ ] SBOM generation for Python scripts (even stdlib-only attestation)
- [ ] Branch protection evidence capture (ASSESS evidence pack)
