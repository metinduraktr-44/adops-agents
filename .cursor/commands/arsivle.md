---
name: arsivle
description: Archive completed phase outputs and snapshot state.
---

# /arsivle (Archive)

## Objective
Archive completed phase outputs into `ARCHIVE/` and snapshot the current state for auditability.

## Requirements
- Copy (never move-away needed inputs) completed artifacts into `ARCHIVE/<YYYY-MM-DD>-<phase>/`.
- Keep registries append-only; do not rewrite history.
- Record a one-line audit entry (phase, timestamp, what was archived).

## Output
- New `ARCHIVE/<date>-<phase>/` folder with copied artifacts.
- Updated `STATE.md` note and `QA/QA_REPORT.md` archive line.
