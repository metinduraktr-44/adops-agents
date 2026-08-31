# Master Plan — Creative Agency OS (Bölüm 13)

Türkçe not: Faz 0..7 yürütme planı. `DEVAM`/`RESUME` bu listedeki ilk işaretlenmemiş
maddeden devam eder. Varsayılan mod: **CANVA:BRIEF-ONLY** (dry-run, yan etki yok).

Current mode: `CANVA:BRIEF-ONLY` · See `STATE.md` for live state.

## Faz 0 — Bootstrap & Context
- [ ] Confirm scaffold present (`.cursor/`, `tools/`, Bölüm 12 folders).
- [ ] Fill `CONTEXT/CONTEXT_BRIEF.md` from owner input (brand, goals, audience).
- [ ] Drop raw inputs into `CONTEXT/INBOX/`.
- [ ] Set brand guardrail values in `.cursor/rules/10-brand-guardrails.mdc`.

## Faz 1 — Research
- [ ] `RESEARCH/RESEARCH_NOTES.md` — market/context notes (sourced or `araştırılacak`).
- [ ] `RESEARCH/COMPETITORS.md` — competitor scan (no fabricated URLs).
- [ ] `RESEARCH/INSIGHTS.md` — distilled insights feeding scenarios.

## Faz 2 — Org & Skills
- [ ] `ORG/ORG_CHART.md` — 40+ title hierarchy (Bölüm 5).
- [ ] `ORG/SKILLS_INVENTORY.md` + `ORG/SKILL_MATRIX.md` — capabilities per role.

## Faz 3 — Experts Engine
- [ ] `EXPERTS/DIGEST.md` — seed roster + monthly loop (READ→DELTA→DIFF→WRITE→DIGEST).
- [ ] Mark all unsourced claims `araştırılacak / URL doğrulanmalı`.

## Faz 4 — Scenarios & Matrix
- [ ] `SCENARIOS/README.md` — 8-scenario framework concepts.
- [ ] `MATRIX/CHANNEL_MATRIX.md` + `MATRIX/PRODUCTION_GRID.csv` — channel×size specs (verify vs official docs).

## Faz 5 — Briefs
- [ ] `BRIEFS/*` — one production brief per channel×scenario, grounded in CONTEXT_BRIEF.

## Faz 6 — Production (Canva)
- [ ] In `CANVA:BRIEF-ONLY`: write intended ops + registry rows only (no Canva calls).
- [ ] In `CANVA:ON` (after user OAuth): bulk-create → resize → brand-check → export.
- [ ] Register all designs in `CANVA_OPS/DESIGN_REGISTRY.csv`; log errors.

## Faz 7 — QA & Archive
- [ ] `QA/QA_REPORT.md` — spec + brand + copy verdicts (critics).
- [ ] Spec-validate every asset (`spec-dogrula` / hook).
- [ ] Archive completed phase outputs to `ARCHIVE/<date>-<phase>/`.
- [ ] `python3 scripts/validate.py` → `VALIDATION: GECTI`.
