# Security Context — Inventory (defense perspective)

> Damga: 2026-08-27T12:40:00Z · MODE=ASSESS-ONLY · no secret values

## Repo type
- Claude Code / Cursor component pack + agency automation (`adops-agents`)
- Content: `components/`, `docs/`, `data/`
- Automation: `scripts/` (Python stdlib + Bash)

## Assets to protect
| Asset class | Path / surface | Notes |
|---|---|---|
| Org model | `data/org.json` | 600 agents — change only via generate_org.py |
| Prompt banks | `data/prompt_bank/` | IP / operational prompts |
| Holding model | `data/holding.json` | OpCo + country LLM agencies |
| Skill registry | `data/skill_agency_registry.json` | routing |
| Audit chain | `AUDIT_LOG.jsonl`, `BILGI_TABANI.md` | integrity |
| Cursor config | `.cursor/` | rules, hooks, MCP URLs |
| CI | `.github/workflows/` | supply chain |
| Secrets | env / MCP Authorize | never in repo — `${VAR}` only |

## Trust boundaries
- Public GitHub remote vs local workspace
- MCP servers (OAuth by owner) vs local files
- Generated automation writes (daily_ops, nightly) vs human review

## Ingestion method
Quick path scan + README/AGENTS — no credential probing.
