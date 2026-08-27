---
name: archive-loop
description: Use when closing a phase — archiving completed outputs and snapshotting state for audit.
---

# Archive Loop

## Instructions
1. Identify the completed phase's artifacts across Bölüm 12 folders.
2. Copy them into `ARCHIVE/<YYYY-MM-DD>-<phase>/` (registries stay append-only; never rewrite history).
3. Update `STATE.md` and append an archive line to `QA/QA_REPORT.md`.
4. Check the phase off in `.cursor/plans/master-plan.md`.

## Examples
- "Archive Faz 3 outputs" → new dated archive folder + state snapshot.

## Performance Notes
- Copy, don't move, artifacts that later phases still consume.

## Troubleshooting
- Missing exit criteria → do not archive; run `/faz-raporu` first.
