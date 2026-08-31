# AGENTS.md

`adops-agents` is a Claude Code component pack + agency-automation repo (not a deployable web app). Content lives in `components/`, `docs/`, and `data/`; automation lives in `scripts/`. See `README.md` and `CONTRIBUTING.md` for the product overview and contribution rules.

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

## Creative Agency OS (Cursor)

Türkçe not: Bu bölüm, "Otonom AI Creative Agency Operating System (Canva Dual-Mode)" master prompt'unun işletim iskeletidir. Şu an **CANVA:BRIEF-ONLY** (dry-run) modundadır — hiçbir gerçek Canva API çağrısı, hesap, anahtar veya ağ yan etkisi yoktur.

An additive scaffold that turns this repo into a runnable creative-agency operating system. It does **not** replace the existing agency corpus under `components/**` or `data/**` — it lives alongside it in `.cursor/`, `tools/`, and new top-level output folders.

### Architecture / where things live
- `.cursor/rules/*.mdc` — always-on and scoped behavior rules (identity, brand guardrails, spec validation, file structure, Canva ops). Behavior rules go here, **not** in AGENTS.md (avoid duplication).
- `.cursor/commands/*.md` — slash commands (`/baslat`, `/devam`, `/canva-uret`, …). Each has Objective / Requirements / Output.
- `.cursor/skills/<name>/SKILL.md` — progressive-disclosure skills (Canva ops + agency workflow). Folder name equals frontmatter `name`.
- `.cursor/agents/*.md` — read-only critic subagents (`critic-copy`, `critic-design`, `critic-spec`).
- `.cursor/mcp.json` — references the Canva MCP URL only. **OAuth is a user action** (see `.cursor/skills/*/references` and `CANVA_OPS/MCP_TOOLS.md`); no secrets live in-repo.
- `.cursor/hooks.json` (v1) — `afterFileEdit` → `scripts/spec_validate.py`; optional `stop` phase-completion check. stdio JSON in/out, fail-open.
- `.cursor/plans/master-plan.md` — Faz 0..7 phase plan (Bölüm 13).
- `STATE.md` — resume state (current phase + flags). Read this on `DEVAM`/`RESUME`.
- `tools/canva-client/` — TypeScript Canva Connect API client scaffold (Bölüm 9 Mod A2). Stubs only; no deps installed, no network.

### Output folders (Bölüm 12)
`CONTEXT/`, `RESEARCH/`, `TASKS/`, `ORG/`, `EXPERTS/`, `SCENARIOS/`, `MATRIX/`, `BRIEFS/`, `CANVA_OPS/`, `QA/`, `ARCHIVE/`. Generated artifacts (designs, exports, logs) land under `CANVA_OPS/` and `ARCHIVE/`.

### How to run (owner commands)
- `BAŞLAT` — cold start from `.cursor/plans/master-plan.md` Faz 0.
- `DEVAM` / `RESUME` — resume from `STATE.md` at the last completed phase.
- `CANVA:BRIEF-ONLY` — **default/current** dry-run: produce briefs, specs, and registries but do **not** call Canva. No side-effects.
- `CANVA:ON` — enable real Canva MCP / Connect API operations. Requires the user to complete Canva OAuth first (user action). Do not enable autonomously.

### Quality gate
Same as the rest of the repo: `python3 scripts/validate.py` must print `VALIDATION: GECTI`. `validate.py` only scans `components/**`, so Creative Agency OS files do not affect it — but always run it before committing.
