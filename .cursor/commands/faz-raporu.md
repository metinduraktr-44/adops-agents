---
name: faz-raporu
description: Produce a phase-completion report for the current or a named phase.
---

# /faz-raporu (Phase Report)

## Objective
Summarize what a phase produced, whether its exit criteria are met, and what is blocked or needs verification.

## Requirements
- Read `STATE.md` and the phase's artifacts under Bölüm 12 folders.
- Check exit criteria from `.cursor/plans/master-plan.md`.
- List spec/brand/validation results; surface any `araştırılacak / URL doğrulanmalı` items.

## Output
- A concise report (Türkçe) appended to `QA/QA_REPORT.md`: phase, done ✓ / open ✗, risks, next.
- Updated checkboxes in `master-plan.md` if criteria are met.
