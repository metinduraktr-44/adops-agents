---
name: canva-edit-design
description: Use when editing an existing Canva design — changing text, images, colors, or layout on a specific design ID.
---

# Canva Edit Design

## Instructions
1. Confirm mode. In `CANVA:BRIEF-ONLY`, describe the intended edits in `CANVA_OPS/` and stop; only edit live when `CANVA:ON` + OAuth done.
2. Resolve the target design ID from `CANVA_OPS/DESIGN_REGISTRY.csv`.
3. Discover the Canva MCP tool schema before calling; otherwise use `tools/canva-client/`.
4. Apply edits (text/image/color/layout) that respect `10-brand-guardrails`.
5. Re-run `spec-dogrula` on affected assets; register the new version.

## Examples
- "Swap the headline on design `DAF-123` to the Q2 offer" → edit text layer, keep brand fonts.

## Performance Notes
- Batch multiple text edits into one autofill/update call when possible.

## Troubleshooting
- MCP `needsAuth` → 🚩, continue in dry-run.
- Design ID missing → check registry / re-create via `canva-bulk-create`.
