---
name: spec-matrix
description: Use when building or validating the channel x size production matrix and per-asset specs.
---

# Spec Matrix

## Instructions
1. Maintain `MATRIX/CHANNEL_MATRIX.md` (human-readable 2026 spec table) and `MATRIX/PRODUCTION_GRID.csv` (machine-readable rows).
2. Each grid row: channel, placement, width, height, aspect_ratio, max_file_size, format, notes.
3. Validate assets against rows (exact pixels, ratio, size, format) — see `20-spec-validation`.
4. Always append: "verify against official platform docs before production."

## Examples
- "Add TikTok in-feed 1080x1920 to the grid" → new CSV row + matrix note.

## Performance Notes
- Keep CSV the source of truth for automation; the markdown table is documentation.

## Troubleshooting
- Spec uncertainty → mark `verify` rather than guessing pixel values.
