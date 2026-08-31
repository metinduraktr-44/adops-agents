---
name: canva-brand-check
description: Use when verifying a design against brand guardrails — colors, fonts, logo usage, and tone before approval.
---

# Canva Brand Check

## Instructions
1. Load approved brand values from `CONTEXT/CONTEXT_BRIEF.md` (never invent them).
2. Inspect the design's colors, type families, logo variant/clearspace, and copy tone.
3. Flag every deviation; guardrail wins over creative preference.
4. Record pass/fail in `QA/QA_REPORT.md`.

## Examples
- "Check design `DAF-123` is on-brand" → compare palette + fonts to CONTEXT_BRIEF, report deltas.

## Performance Notes
- Check color/font first (cheap, high signal) before deep layout review.

## Troubleshooting
- CONTEXT_BRIEF missing values → mark `araştırılacak / owner tarafından doldurulacak`, do not guess.
