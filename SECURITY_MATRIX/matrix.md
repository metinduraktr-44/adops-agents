# SECURITY_MATRIX — Crosswalk (draft)

> HAND_AUTHORED · status: draft · needs_expert_review · damga: 2026-08-27T12:55:00Z

## Coverage

| Family | Count | Prefix | Path | Notes |
|---|---|---|---|---|
| LAYERS | 100 | LYR | `LAYERS/` | Defense-in-depth |
| FIREWALLS | 100 | FW | `FIREWALLS/` | Policy templates |
| ENCRYPTION | 100 | ENC | `ENCRYPTION/` | Includes PQC hybrid TLS notes |
| CHANGE | 100 | CHG | `CHANGE/` | Secure change / CAB |
| TRANSPARENT_CODE | 100 | TC | `TRANSPARENT_CODE/` | SBOM/SLSA |
| CONDITIONAL | 100 | COND | `CONDITIONAL/` | Conditional access |

**Total:** 600 draft controls · all mappings `needs_expert_review`.

## Standards pins (authoritative sources)

| Standard | Pin | Source |
|---|---|---|
| NIST CSF | 2.0 (CSWP 29, Feb 2024) | https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final |
| NIST SP 800-53 | Rev.5 (catalog size ~1189–1196 commonly cited; verify PDF) | NIST CSRC |
| ISO/IEC 27001 | 2022 | Annex A crosswalk draft in COMPLIANCE |
| CIS Controls | v8.1 | CIS |
| OWASP ASVS | 5.0.0 | OWASP |
| PQC | FIPS 203/204/205 | NIST |
| SLSA | v1.0 Build track (pin); note v1.2 exists upstream | https://slsa.dev/spec/v1.0/ |
| NIST SP 800-207 | Zero Trust Architecture | NIST |
| CISA ZTMM | 2.0 (Apr 2023) | https://www.cisa.gov/sites/default/files/2023-04/zero_trust_maturity_model_v2_508.pdf |

## Family → standard emphasis (draft)

| Family | CSF focus | 800-53 families | ISO 27001:2022 | CIS | ASVS |
|---|---|---|---|---|---|
| LAYERS | PR.IR, PR.PS, ID.AM | SC, CM, AC | A.8.20–A.8.28 | CIS-1..4 | V1,V13 |
| FIREWALLS | PR.IR, DE.CM | SC-7, AC-4 | A.8.20–A.8.22 | CIS-13 | V1,V13 |
| ENCRYPTION | PR.DS | SC-12, SC-13, SC-28 | A.8.24 | CIS-3 | V6 |
| CHANGE | GV.PO, PR.PS | CM, CM-3 | A.8.32 | CIS-4 | V14 |
| TRANSPARENT_CODE | ID.RA, PR.PS | SA, SR, SI | A.8.25–A.8.28 | CIS-16 | V14 |
| CONDITIONAL | PR.AA | AC, IA | A.5.15, A.8.2–A.8.3 | CIS-5,6 | V2,V4 |

## Repo surface → control sample (ASSESS crosswalk)

| Repo surface | Sample control IDs | Gap? |
|---|---|---|
| `.github/workflows/*` | TC-009, TC-049, CHG-001 | SBOM/provenance evidence missing |
| `scripts/secret_scan.py` hooks | TC-069, ENC-* key hygiene | Covered partially |
| `.cursor/mcp.json` | COND-001, IAM skill | Security MCP off (good) |
| `infra/.../main.tf` | LYR cloud-control-plane, ENC | Apply path undocumented |
| `data/holding.json` + country agencies | Privacy skill, A.5.x SoA | DPIA stubs thin |
| Creative GIGA coexistence | CHANGE + LYR people-process | Namespace rules exist |

## Coverage gaps (explicit)

| ID | Gap | Severity | Next action (ASSESS) |
|---|---|---|---|
| G-MAT-01 | Exact 800-53 Rev.5 control-to-enhancement enumeration | Med | Verify against current NIST PDF |
| G-MAT-02 | ASVS 5.0.0 chapter-level binding per app tier | Med | Component pack ≠ classic web app — redefine tier |
| G-MAT-03 | ZTMM 2.0 pillar maturity scoring for this repo | Med | Score Identity/Devices/Networks/Apps/Data as Traditional→Initial |
| G-MAT-04 | PQC hybrid deployment assumptions in ENC-* | Low | Expert review before IMPLEMENT |
| G-MAT-05 | SLSA pin: v1.0 vs upstream v1.2 Source track | Low | Document pin rationale in SoA |
| G-MAT-06 | Holding OpCo / country overlay rows missing | Med | Extend matrix rows after inventory OpCo pass |
| G-MAT-07 | Sample of 600 mappings unreviewed by human expert | High | `/sec-uzman-guncelle` + SEC-T002 |

## Red flags
🚩 900k single-file prompt · mega expander + phased refs (~900k **aggregate**)
🚩 Invented top-100 experts · sourced+pending only
🚩 Exploit/PoC · ethics · defense-only
🚩 Certification claim from draft matrix · SoA is draft/needs expert review
