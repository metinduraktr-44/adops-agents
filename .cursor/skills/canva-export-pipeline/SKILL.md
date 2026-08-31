---
name: canva-export-pipeline
description: Use when exporting finished Canva designs to files (PNG/JPG/PDF/MP4) with correct formats per channel.
---

# Canva Export Pipeline

## Instructions
1. Read required export format/quality per placement from `MATRIX/PRODUCTION_GRID.csv`.
2. Mode gate: dry-run lists intended exports; `CANVA:ON` submits export jobs and polls for URLs.
3. Validate exported files with `spec-dogrula` (format, size, dimensions).
4. Record export URLs/paths and verdicts in `DESIGN_REGISTRY.csv` + `VALIDATION.log`.

## Examples
- "Export the approved set as JPG for IG and MP4 for Reels" → format-correct exports, spec-checked.

## Performance Notes
- Batch exports; poll jobs; back off on rate limits.

## Troubleshooting
- Export job stuck → time-box polling, log to `ERRORS.md`, retry.
