---
name: brief-uret
description: Generate production briefs per channel/scenario from context and matrix.
---

# /brief-uret (Brief Produce)

## Objective
Generate copy-paste-ready production briefs per channel × scenario, grounded in `CONTEXT/CONTEXT_BRIEF.md` and `MATRIX/`.

## Requirements
- Pull brand facts only from `CONTEXT_BRIEF.md`; never invent brand values, prices, or claims.
- One brief per channel/scenario combination that exists in `SCENARIOS/` and `MATRIX/PRODUCTION_GRID.csv`.
- Include: objective, audience, key message, mandatory brand elements, size/spec, CTA, deliverables.
- Mark any missing input `araştırılacak / owner tarafından doldurulacak`.

## Output
- Files under `BRIEFS/` (one per brief), following `30-file-structure` naming.
- A brief index update in `BRIEFS/README.md`.
