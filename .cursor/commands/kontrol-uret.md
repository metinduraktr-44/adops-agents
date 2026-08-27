---
name: kontrol-uret
description: Generate mapped security control rows for a 6x100 framework folder (schema-complete, defense-only).
---

# /kontrol-uret (KONTROL ÜRET)

## Objective
Produce security control rows for one framework (`LAYERS/`, `FIREWALLS/`, `ENCRYPTION/`, `CHANGE/`, `TRANSPARENT_CODE/`, or `CONDITIONAL/`), fully mapped to standards.

## Requirements
- Follow `.cursor/rules/20-control-mapping.mdc`: every row carries `id, ad, NIST_CSF, 800-53, ISO27001, CIS, OWASP, doğrulama_yöntemi, savunma_gerekçesi`.
- Reproduce standard values from the master prompt but add "verify against official source before production".
- Defense-only rationale; ATT&CK ids only to justify a D3FEND detection/countermeasure.
- Generate in batches; do NOT dump all 600 controls at once. Append to the folder's control file with a stable header.
- No fabricated standard ids — mark uncertain mappings `araştırılacak / URL doğrulanmalı`.

## Output
- New/updated control rows in the target framework file.
- A count + coverage note (how many of the 100 are mapped) in the folder README.
