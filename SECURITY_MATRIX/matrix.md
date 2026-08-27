# SECURITY_MATRIX — Crosswalk (draft)

> status: draft · needs_expert_review · damga: 2026-08-27T12:40:00Z

## Coverage

| Family | Count | Prefix | Notes |
|---|---|---|---|
| LAYERS | 100 | LYR | Defense-in-depth |
| FIREWALLS | 100 | FW | Policy templates |
| ENCRYPTION | 100 | ENC | Includes PQC hybrid TLS controls |
| CHANGE | 100 | CHG | Secure change |
| TRANSPARENT_CODE | 100 | TC | SBOM/SLSA |
| CONDITIONAL | 100 | COND | Conditional access |

**Total:** 600 draft controls.

## Standards pins
See skill `references/standards.md` — NIST CSF 2.0, 800-53 Rev.5 (~1189–1196 range note),
ISO 27001:2022, CIS v8.1, OWASP ASVS 5.0.0, FIPS 203/204/205, SLSA v1.0, NIST 800-207, CISA ZTMM 2.0.

## Coverage gaps (initial)
- [ ] Exact 800-53 Rev.5 control-to-enhancement enumeration (verify NIST PDF)
- [ ] ASVS 5.0.0 chapter-level binding per app tier
- [ ] ZTMM 2.0 pillar maturity scoring
- [ ] Expert review of PQC hybrid deployment assumptions

## Red flags
🚩 900k single-file prompt · mega expander + phased refs
🚩 Invented top-100 experts · sourced+pending only
🚩 Exploit/PoC · ethics · defense-only
