---
name: sbom-provenance
description: Use when generating SBOMs and build provenance / supply-chain integrity (CycloneDX/SPDX, SLSA v1.0).
icon: shield
---

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

# Sbom Provenance

## Instructions
1. Generate SBOMs (CycloneDX/SPDX — verify) and build provenance (SLSA v1.0 — verify); verify signatures.
2. No secrets in manifests; reference registries by env. Feed TRANSPARENT_CODE controls.
3. Tools wrapped in `tools/security-scanners/` (no deps installed, no network).

## References
- `references/OUTLINE.md` — depth outline (filled in phases).

## Note
Full ~20k-char content is produced later in phases. This is the discoverable skeleton.
