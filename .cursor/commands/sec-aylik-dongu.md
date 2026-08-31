---
name: sec-aylik-dongu
description: Run the monthly security experts knowledge loop (READ to DELTA to DIFF to WRITE to DIGEST).
---

# /sec-aylik-dongu (AYLIK DÖNGÜ — Security)

## Objective
Refresh the security experts digest and standards watch on a monthly cadence.

## Requirements
- Follow `EXPERTS/README.md` loop: **READ** `EXPERTS/SECURITY_DIGEST.md` → **DELTA** gather dated findings (only if research tools/MCP enabled; else placeholders) → **DIFF** vs prior → **WRITE** updates → **DIGEST** dated summary.
- Seed names are real public figures (owner-supplied); mark bios/URLs `araştırılacak / URL doğrulanmalı`. Dan Kaminsky = historical (deceased 23 Apr 2021).
- Re-check standard values (NIST CSF 2.0, 800-53 Rev.5, ISO 27001:2022, CIS v8.1, OWASP ASVS 5.0.0, PQC FIPS 203/204/205, SLSA v1.0, 800-207/ZTMM 2.0) with "verify against official source".
- No fabrication, no secrets, no network side-effects.

## Output
- Updated `EXPERTS/SECURITY_DIGEST.md` with a dated DELTA + DIGEST section and verification TODOs.
- Note in `CALENDAR/` that the monthly loop ran.
