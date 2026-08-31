---
name: canva-bulk-create
description: Use when generating many designs at once from a data table via Canva autofill/bulk create.
---

# Canva Bulk Create

## Instructions
1. Prepare a data table (rows = variants, columns = template fields) grounded in approved briefs.
2. Mode gate: dry-run writes the intended autofill payload to `CANVA_OPS/`; `CANVA:ON` submits the autofill job.
3. Submit autofill against a brand template ID; poll the job to completion.
4. `spec-dogrula` each output; register all in `DESIGN_REGISTRY.csv`.

## Examples
- "Create 20 promo variants from `offers.csv`" → autofill job → 20 spec-checked designs.

## Performance Notes
- Chunk large batches; respect rate limits with retry/backoff.

## Troubleshooting
- Partial batch failure → log failed rows to `ERRORS.md`, re-submit only those.
