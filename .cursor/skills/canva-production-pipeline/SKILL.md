---
name: canva-production-pipeline
description: Use when running the full end-to-end Canva production flow — brief to bulk-create to resize to brand-check to export.
---

# Canva Production Pipeline

## Instructions
End-to-end orchestrator chaining the other Canva skills:
1. `brief-writer` / `/brief-uret` → briefs grounded in CONTEXT_BRIEF + MATRIX.
2. `canva-bulk-create` → generate variants (autofill).
3. `canva-resize-for-social` → placement variants from the matrix.
4. `canva-brand-check` + `spec-matrix`/`spec-dogrula` → gate every asset.
5. `canva-export-pipeline` → export approved assets.
6. `archive-loop` → archive + register.

Mode gate throughout: in `CANVA:BRIEF-ONLY` produce the full plan + registries without calling Canva.

## Examples
- "Run full production for the Spring campaign" → briefs → designs → resizes → QA → exports → archive.

## Performance Notes
- Fail-open on non-critical steps; never let one asset block the batch.

## Troubleshooting
- Any stage failure → log to `ERRORS.md`, keep the rest of the pipeline moving, report at the end.

See `references/` for detailed per-stage checklists when needed.
