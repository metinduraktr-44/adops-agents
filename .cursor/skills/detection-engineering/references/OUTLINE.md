# Detection Engineering — Outline (skeleton)

GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok. Standard values: verify against official source before production.

## Method
- Pick technique (ATT&CK id) to cover — for detection only
- Identify data source / observable
- Write rule (Sigma/YARA/EDR) — descriptive
- Tune false positives
- Map to D3FEND countermeasure

## Output
- Detection rules + coverage notes under `IMPLEMENTATION/`.

## TODO (phased)
- [ ] Expand to full content in phased runs.
- [ ] Verify every standard id/version against official docs.
