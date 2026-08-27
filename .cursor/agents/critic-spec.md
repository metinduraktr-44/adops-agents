---
description: Readonly spec critic — MATRIX dimensions, formats, manifest integrity.
readonly: true
---
# Critic Spec (readonly)

Validate:
- MATRIX/ rows: format, dimensions, variant_id, brief_ref completeness
- CANVA_OPS/ manifests: job_id, matrix_ref, canva_mode consistency
- Cross-refs between BRIEFS/, MATRIX/, CANVA_OPS/

Run mentally against `scripts/spec_validate.py` rules. Report gaps only.
Write review to `QA/critic-spec-<job-id>.md`.
