# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

# SECURITY_RESEARCH — defensive research notes (skeleton)

Türkçe not: Savunma-odaklı araştırma çıktıları. Kaynaksız iddialar `araştırılacak / URL doğrulanmalı` işaretlenir. Ağ yan etkisi yok.

## Contents (fill in phases)
- `standards-watch.md` — NIST CSF 2.0, 800-53 Rev.5, ISO 27001:2022, CIS v8.1, OWASP ASVS 5.0.0, PQC (FIPS 203/204/205), SLSA v1.0, 800-207/ZTMM 2.0 — each with source + "verify against official source before production".
- `threat-landscape.md` — defensive threat trends (no offensive TTP recipes).
- `tooling-notes.md` — defensive tools (Semgrep, Trivy, OPA, …) evaluated at concept level.

## Rules
- No fabrication of facts, CVEs, or URLs. No secrets. Defense-only.
- Research does not enable live scanning or external calls in this repo (MCP servers default OFF).
