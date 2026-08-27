---
name: canva-implement-feedback
description: Use when applying accepted design-feedback notes back into a Canva design and re-validating.
---

# Canva Implement Feedback

## Instructions
1. Take accepted notes from `canva-design-feedback` (or owner) as an ordered change list.
2. Mode gate: dry-run describes changes; `CANVA:ON` applies them via MCP / `tools/canva-client/`.
3. Apply P0→P2 in order, preserving brand guardrails.
4. Re-run `canva-brand-check` + `spec-dogrula`; register the new version.

## Examples
- "Apply the P0/P1 notes to `DAF-777`" → edit, then re-validate spec + brand.

## Performance Notes
- Group edits into a single update/autofill pass to reduce API calls.

## Troubleshooting
- If a note conflicts with a guardrail, keep the guardrail and flag the conflict.
