---
name: job-card-engine
description: Generate and expand job cards with H001..H200 index pattern.
---

# job-card-engine

> TR: LATOS skill. Keşfedilmezse inline path kullan.
> Damga: 2026-08-27T20:16:49Z

## Hybrid rule
If this skill is not discovered after Cursor restart → follow inline steps in
`docs/CURSOR-LATOS-GIGA-MASTER-PROMPT.md` for the same phase. Output paths identical.

## K-003 guardrails
- No 900M-char single prompt; expand via `references/` + `/devam`.
- No invented top-100 experts; `pending_research` + sourced seeds only.
- Human approval gates for restore, publish, self-modification.

## Progressive disclosure
- `references/overview.md` — scope
- `references/workflow.md` — operator steps
- `references/templates.md` — output schemas

## State
Read `LATOS_STATE.md` before each run. Stamp AUDIT_LOG on completion.
