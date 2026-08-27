---
name: spec-dogrula
description: Validate produced assets against channel x size specs and file limits.
---

# /spec-dogrula (Spec Validate)

## Objective
Validate produced or planned assets against the channel × size matrix and record verdicts.

## Requirements
- Compare each asset to its `MATRIX/PRODUCTION_GRID.csv` row: exact pixels, aspect ratio, max file size, format.
- Where image files exist, `scripts/spec_validate.py` can check pixels/ratio/size (Pillow optional; degrades to metadata-only).
- Always append: "verify against official platform docs before production."

## Output
- Verdict lines in `CANVA_OPS/VALIDATION.log` (file, expected vs actual, PASS/FAIL).
- A short summary in `QA/QA_REPORT.md`; off-spec items block phase completion.
