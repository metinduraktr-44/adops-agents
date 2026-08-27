---
name: gap-analizi
description: Run a defensive gap analysis of current controls vs a target standard and record findings.
---

# /gap-analizi (GAP ANALİZİ)

## Objective
Compare implemented/planned controls against a target framework (NIST CSF 2.0, ISO 27001:2022, CIS v8.1, …) and identify gaps.

## Requirements
- Read the relevant `LAYERS|FIREWALLS|ENCRYPTION|CHANGE|TRANSPARENT_CODE|CONDITIONAL/**` control files and `SECURITY_MATRIX/matrix.md`.
- For each target requirement: mark `covered / partial / gap`, with evidence pointer and defensive rationale.
- `MODE=ASSESS-ONLY`: assess only; do not enact changes. No secrets, no network.
- Flag unverified standard mappings `araştırılacak / URL doğrulanmalı`.

## Output
- `ASSESSMENTS/<YYYY-MM-DD>-gap-<standard>.md` with a covered/partial/gap table and prioritized remediation ideas (defensive).
- Summary line: coverage %, top gaps.
