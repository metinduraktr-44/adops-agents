# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

# Security Context — Attack Surface (skeleton)

Türkçe not: Saldırı yüzeyi haritası — savunma amaçlı (nereyi sertleştirmeli). Exploit üretilmez. MODE=ASSESS-ONLY.

## Entry points (defensive mapping)
| surface | exposure (public/internal) | trust_boundary | ilgili_kontrol (LAYERS/FIREWALLS/…) | savunma_notu |
|---|---|---|---|---|
| (template) external HTTPS endpoint | public | internet→app | FW-001, ENC-001 | default-deny + TLS enforce |

## Threat mapping (defense-only)
- Use `threat-modeling` skill: STRIDE per element → map to MITRE ATT&CK **only** to design D3FEND countermeasures/detections. No offensive PoC.
- Record derived detections under `IMPLEMENTATION/` and coverage in `SECURITY_MATRIX/matrix.md`.

## To verify
- All external references / CVE ids: `araştırılacak / URL doğrulanmalı`.
