---
name: sec-faz-raporu
description: Produce a concise phase report for the current Security Governance OS phase.
---

# /sec-faz-raporu (FAZ RAPORU — Security)

## Objective
Summarize the current security phase: what was produced, what is open, and risks.

## Requirements
- Read `SECURITY_STATE.md` and `.cursor/plans/security-master-plan.md`.
- List completed vs open `- [ ]` items for the current phase.
- Note any 🚩 red-flags, unverified standards (`verify against official source`), and to-verify items.
- Do not fabricate; do not expose secrets.

## Output
- A short report written to `REPORTS/<YYYY-MM-DD>-faz-raporu.md`.
- Inline summary: phase, % complete, blockers, next action.
