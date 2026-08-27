# AGENTS.md

`adops-agents` is a Claude Code component pack + agency-automation repo (not a deployable web app). Content lives in `components/`, `docs/`, and `data/`; automation lives in `scripts/`. See `README.md` and `CONTRIBUTING.md` for the product overview and contribution rules.

## GIGA Creative Agency (Canva Dual-Mode)

In-repo bootstrap — Claude Code paste **cancelled** (K-003).

| Area | Location |
|---|---|
| Master prompt | `docs/CURSOR-GIGA-MASTER-PROMPT.md` |
| Bootstrap + usage | `docs/GIGA-AGENCY-BOOTSTRAP.md` |
| Phase tracker | `STATE.md` |
| Plan | `.cursor/plans/master-plan.md` |
| Creative artifacts | `BRIEFS/`, `MATRIX/`, `CANVA_OPS/`, `QA/`, `ARCHIVE/` |
| Canva MCP | `.cursor/mcp.json` → owner OAuth required |
| Spec hook | `scripts/spec_validate.py` |

**Default mode:** `CANVA_MODE=BRIEF-ONLY` — briefs/specs/manifests only until owner completes Canva OAuth in Cursor. Autofill is Enterprise-only. Rules live in `.cursor/rules/00-agency-core.mdc` … `40-canva-ops.mdc` (not duplicated here).

## Cursor Cloud specific instructions

### Runtime & dependencies
- Pure Python 3 stdlib + Bash, wrapped by npm scripts. There are **no** package dependencies: `package.json` has no `dependencies`, and there is no `requirements.txt`/lockfile. `npm install` is effectively a no-op, so no install step is required to start working.
- There is no application server, database, or GUI. "Running the app" means running the validator and the cron-style automation scripts below.

### Primary gate (lint/test/build equivalent)
- `npm run validate` (= `python3 scripts/validate.py`) is the single quality gate used by CI (`.github/workflows/validate-components.yml`). Success prints `VALIDATION: GECTI`; failure prints `VALIDATION: KALDI` and exits non-zero. Run this before committing (per `CONTRIBUTING.md`).

### Automation scripts write into the repo (important gotcha)
- The ops scripts (`scripts/daily_ops.py`, `scripts/weekly_board.py [--board]`, `scripts/nightly.sh`, `scripts/timestamp.sh`) and the generators (`scripts/generate_org.py`, `scripts/generate_docs.py`, `scripts/build_question_bank.py`) **write files** into `gundem/`, `makaleler/`, `toplantilar/`, `docs/`, `data/`, `components/`, and append to `AUDIT_LOG.jsonl` / `BILGI_TABANI.md` / `IS_LISTESI.md`. Running any of them dirties the working tree.
- Non-obvious: the generators can emit content (including new untracked `components/agents/agency/**` files) that differs from what is currently committed. Only run them if you intend to commit regenerated org/docs output. `generate_org.py` asserts exactly 600 agents.
- If you ran these only to smoke-test the environment, restore a clean tree with `git checkout -- . && git clean -fd` (safe here because these are regenerable outputs).
- `daily_ops.py` / the daily article step is skip-if-exists: it will not overwrite an already-present `makaleler/<date>-<topic>.md`.

### Optional LLM generation
- LLM-backed content generation is optional and requires the `ANTHROPIC_API_KEY` env var (paid API). Without it, every loop still runs deterministically (skeleton articles, real standups/minutes/validation). No key is needed for validation or normal development.
