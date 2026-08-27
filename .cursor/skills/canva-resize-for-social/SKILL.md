---
name: canva-resize-for-social
description: Use when resizing one design into multiple social placements/sizes from the channel matrix.
---

# Canva Resize For Social

## Instructions
1. Read target placements/sizes from `MATRIX/PRODUCTION_GRID.csv`.
2. Mode gate: dry-run lists intended resize jobs; `CANVA:ON` runs the Canva resize job (Magic Resize / Connect resize).
3. For each target: create a resized variant, then `spec-dogrula` for exact pixels/ratio.
4. Register every variant in `DESIGN_REGISTRY.csv`.

## Examples
- "Resize `DAF-123` for IG feed, IG story, and FB feed" → 3 spec-checked variants.

## Performance Notes
- Submit resize as a job and poll; do not block on a single synchronous call.

## Troubleshooting
- Off-spec output → reject + log to `VALIDATION.log`; adjust and retry.
