---
name: canva-uret
description: Produce Canva designs (or dry-run briefs) for approved matrix rows.
---

# /canva-uret (Canva Produce)

## Objective
Turn approved briefs + matrix rows into Canva designs — or, in `CANVA:BRIEF-ONLY`, into fully specified production instructions without calling Canva.

## Requirements
- **Mode gate:** if `CANVA:BRIEF-ONLY`, do NOT call Canva; write intended ops to `CANVA_OPS/` and stop. Only call Canva when `CANVA:ON` and OAuth is complete (user action).
- Every asset must match an approved row in `MATRIX/PRODUCTION_GRID.csv` and pass brand guardrails.
- Use Canva MCP (discover schema first) or fall back to `tools/canva-client/`. Poll long jobs; retry with backoff.
- Register outputs; log errors.

## Output
- `CANVA_OPS/DESIGN_REGISTRY.csv` rows (one per asset/variant).
- Exports/links (only in `CANVA:ON`); errors → `CANVA_OPS/ERRORS.md`; spec results → `CANVA_OPS/VALIDATION.log`.
