# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

# LAYERS — Defense-in-Depth Layers (100-control framework)

Türkçe not: Katmanlı savunma (perimeter→data→identity) 100-kontrol çerçevesi. Additive; MODE=ASSESS-ONLY.

> ⚠️ Standard values reproduced for scaffolding — **verify against official source before production**.

## Scope
- Perimeter/network segmentation & NAC
- Host/endpoint hardening
- Application security
- Data protection
- Identity & access
- Monitoring & detection

## Control row schema (mandatory — see `.cursor/rules/20-control-mapping.mdc`)
Each of the 100 controls MUST carry all fields below. CIS/OWASP where applicable.

| id | ad | NIST_CSF (2.0) | 800-53 Rev.5 | ISO27001:2022 | CIS v8.1 | OWASP ASVS 5.0.0 | doğrulama_yöntemi | savunma_gerekçesi |
|---|---|---|---|---|---|---|---|---|
| LAY-001 | Network segmentation | PR.AA/PR.IR* | SC-7* | A.8.20* | CIS 12* | — | VLAN/ACL review + isolation test | limits lateral movement |
| LAY-002 | Endpoint baseline hardening | PR.PS* | CM-6* | A.8.9* | CIS 4* | — | CIS-benchmark scan evidence | reduces exploitable surface |

`*` = verify id/version against official docs. Rows above are **TEMPLATE examples**, not the final set.

## Note
Do NOT enumerate all 100 controls here in scaffold. Generate in batches via `/kontrol-uret`; keep the stable header. Full content is produced in phased runs. Detections may cite MITRE ATT&CK ids **only** to justify a D3FEND countermeasure.
