---
name: compliance-paket
description: Assemble a compliance evidence package (e.g. ISO 27001 SoA) from mapped controls, with verify banners.
---

# /compliance-paket (COMPLIANCE PAKET)

## Objective
Bundle mapped controls + assessment evidence into a compliance package (ISO 27001:2022 Statement of Applicability, NIST CSF profile, etc.).

## Requirements
- Read control files, `SECURITY_MATRIX/matrix.md`, `ASSESSMENTS/**`, and `COMPLIANCE/` stubs.
- Populate the SoA template stub: control ref, applicability (yes/no + justification), status, evidence pointer.
- Add "verify against official source before production" banner to all reproduced standard values (ISO 27001:2022 = 93 Annex A controls; 800-53 Rev.5 range ~1,189–1,196).
- No fabricated evidence; mark missing evidence `araştırılacak`. No secrets.

## Output
- `COMPLIANCE/<YYYY-MM-DD>-<standard>-package.md` (+ SoA table filled from real mapped controls).
- Coverage/readiness summary line.
