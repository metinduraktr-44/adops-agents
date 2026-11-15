# Master Plan — Creative Agency OS (Bölüm 13)

Türkçe not: Faz 0..7 yürütme planı. `DEVAM`/`RESUME` bu listedeki ilk işaretlenmemiş
maddeden devam eder. Varsayılan mod: **CANVA:BRIEF-ONLY** (dry-run, yan etki yok).

Current mode: `CANVA:BRIEF-ONLY` · See `STATE.md` for live state.

## Faz 0 — Bootstrap & Context
- [x] Confirm scaffold present (`.cursor/`, `tools/`, Bölüm 12 folders). (filesystem 2026-11-03)
- [ ] Fill `CONTEXT/CONTEXT_BRIEF.md` from owner input (brand, goals, audience). **blocked — no fabricate**
- [ ] Drop raw inputs into `CONTEXT/INBOX/`. **blocked — owner**
- [ ] Set brand guardrail values in `.cursor/rules/10-brand-guardrails.mdc`. (placeholders only; wait for CONTEXT_BRIEF)

## Faz 1 — Research
- [x] `RESEARCH/RESEARCH_NOTES.md` scaffold with `araştırılacak` (no invented URLs).
- [x] `RESEARCH/COMPETITORS.md` scaffold (no fabricated URLs).
- [ ] `RESEARCH/INSIGHTS.md` — distilled insights feeding scenarios. **needs sourced research**

## Faz 2 — Org & Skills
- [x] `ORG/ORG_CHART.md` — 49 functional titles (no invented people).
- [ ] `ORG/SKILLS_INVENTORY.md` + `ORG/SKILL_MATRIX.md` — extend rows to match 40+ titles (thin stub today).

## Faz 3 — Experts Engine
- [x] `EXPERTS/DIGEST.md` seed roster + DELTA log (unsourced marked `araştırılacak`).
- [x] Unsourced claims marked `araştırılacak / URL doğrulanmalı`.
- [ ] Monthly sourced loop (READ→DELTA→DIFF→WRITE) — not run; no fabricated bios.

## Faz 4 — Scenarios & Matrix
- [x] `SCENARIOS/README.md` — 8-scenario framework concepts.
- [x] `MATRIX/CHANNEL_MATRIX.md` + `MATRIX/PRODUCTION_GRID.csv` present — **status=verify** until official docs.

## Faz 5 — Briefs
- [ ] `BRIEFS/*` — one production brief per channel×scenario, grounded in CONTEXT_BRIEF. **blocked on CONTEXT**

## Faz 6 — Production (Canva)
- [x] `CANVA:BRIEF-ONLY` registry header in `CANVA_OPS/DESIGN_REGISTRY.csv` (no Canva calls).
- [ ] In `CANVA:ON` (after user OAuth): bulk-create → resize → brand-check → export.
- [ ] Register designs (rows) in `CANVA_OPS/DESIGN_REGISTRY.csv`; log errors.

## Faz 7 — QA & Archive
- [x] `QA/QA_REPORT.md` scaffold (no asset verdicts yet).
- [ ] Spec-validate every asset (`spec-dogrula` / hook).
- [ ] Archive completed phase outputs to `ARCHIVE/<date>-<phase>/`.
- [x] `python3 scripts/validate.py` → `VALIDATION: GECTI` (2026-11-03 continue pass; briefs/assets still empty).
