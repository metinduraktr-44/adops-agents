---
name: devam
description: Resume the agency run from the last completed phase in STATE.md.
---

# /devam (DEVAM)

## Objective
Resume work from the exact phase and flags recorded in `STATE.md` without redoing completed phases.

## Requirements
- Read `STATE.md` first; treat it as source of truth for current phase + mode.
- Cross-check `.cursor/plans/master-plan.md` checklist; continue at the first unchecked item.
- Preserve the recorded Canva mode (`CANVA:BRIEF-ONLY` / `CANVA:ON`).
- Do not overwrite prior artifacts; append/version.

## Output
- Continued phase artifacts in Bölüm 12 folders.
- Updated `STATE.md` and checked-off items in `master-plan.md`.
- Status line: resumed-from phase → next action.
