---
name: baslat
description: Cold-start the Creative Agency OS from Faz 0 of the master plan.
---

# /baslat (BAŞLAT)

## Objective
Cold-start the agency operating system from `Faz 0` and drive the phase plan forward in `CANVA:BRIEF-ONLY` unless told otherwise.

## Requirements
- Read `.cursor/plans/master-plan.md` and `STATE.md`.
- If `STATE.md` shows a phase past Faz 0, confirm the owner wants a fresh start before resetting.
- Honor the current Canva mode flag; default `CANVA:BRIEF-ONLY` (no Canva calls, no secrets).
- Ensure Bölüm 12 output folders exist; create missing skeleton files, never overwrite.

## Output
- Updated `STATE.md` (phase, flags, timestamp).
- First-phase artifacts written to their Bölüm 12 folders.
- A short status line: current phase, mode, next action.
