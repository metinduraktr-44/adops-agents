---
name: aylik-dongu
description: Run the monthly EXPERTS refresh loop READ->DELTA->DIFF->WRITE->DIGEST.
---

# /aylik-dongu (Monthly Cycle)

## Objective
Run the monthly experts/knowledge refresh loop and update the digest — no fabrication, sources verified.

## Requirements
- Follow `EXPERTS/README.md` loop: **READ** current digest → **DELTA** new findings → **DIFF** vs prior → **WRITE** updates → **DIGEST** summary.
- Seed names are real public figures supplied by the owner; do **not** invent URLs or bios. Mark unverified items `araştırılacak / URL doğrulanmalı`.
- Piyush Pandey = historical/memorial reference (deceased 23 Oct 2025).
- No network side-effects unless the owner explicitly enables research tools.

## Output
- Updated `EXPERTS/DIGEST.md` with dated delta section.
- Verification TODOs listed for any unsourced claim.
