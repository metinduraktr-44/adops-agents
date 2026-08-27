---
name: resume
description: English alias of DEVAM; resume the agency run from STATE.md.
---

# /resume (RESUME)

## Objective
English-language alias of `/devam`. Resume the agency run from the last completed phase in `STATE.md`.

## Requirements
- Identical behavior to `/devam`: read `STATE.md`, continue at the first unchecked item in `.cursor/plans/master-plan.md`.
- Keep the recorded Canva mode; never enable `CANVA:ON` implicitly.
- Additive only; no overwrite of prior outputs.

## Output
- Continued phase artifacts + updated `STATE.md`.
- Status line summarizing resumed phase and next step.
