# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

# FIREWALLS — Firewall & Exposure Policy (100-control framework)

Türkçe not: Ağ/host/WAF/bulut güvenlik duvarı 100-kontrol çerçevesi (default-deny). Additive; MODE=ASSESS-ONLY.

> ⚠️ Standard values reproduced for scaffolding — **verify against official source before production**.

## Scope
- Network ACL / segmentation
- Host-based firewall
- WAF (ASVS-aligned)
- Cloud SG/NSG least-exposure
- Egress filtering & allowlists

## Control row schema (mandatory — see `.cursor/rules/20-control-mapping.mdc`)
Each of the 100 controls MUST carry all fields below. CIS/OWASP where applicable.

| id | ad | NIST_CSF (2.0) | 800-53 Rev.5 | ISO27001:2022 | CIS v8.1 | OWASP ASVS 5.0.0 | doğrulama_yöntemi | savunma_gerekçesi |
|---|---|---|---|---|---|---|---|---|
| FW-001 | Default-deny ingress | PR.IR* | SC-7* | A.8.20* | CIS 4* | — | ruleset review + connectivity test | minimizes exposed surface |
| FW-002 | Egress allowlist | DE.CM* | SC-7(5)* | A.8.20* | CIS 4* | — | egress log review | curbs C2/exfil channels (detective) |

`*` = verify id/version against official docs. Rows above are **TEMPLATE examples**, not the final set.

## Note
Do NOT enumerate all 100 controls here in scaffold. Generate in batches via `/kontrol-uret`; keep the stable header. Full content is produced in phased runs. Detections may cite MITRE ATT&CK ids **only** to justify a D3FEND countermeasure.
