---
name: etik-denetim
description: Audit recent security outputs for defense-only compliance and secret hygiene; report violations.
---

# /etik-denetim (ETİK DENETİM)

## Objective
Review recently produced security artifacts to confirm they stay defense-only and secret-free.

## Requirements
- Scan changed/added files in the security folders for: offensive/exploit/weaponization content, plaintext or realistic-format secrets, and fabricated facts/URLs.
- Use `scripts/ethics_check.py` and `scripts/secret_scan.py` outputs (`QA/ethics-check.log`, `QA/secret-scan.log`) as inputs; do not echo any secret value.
- Read-only audit: report, do not "fix" by adding offensive content. Propose defensive remediations only.

## Output
- `QA/findings.md` updated with a dated audit entry: PASS/FAIL per check, REDACTED pointers, remediation.
- Inline verdict: defense-only OK? secrets clean? fabrication clean?
