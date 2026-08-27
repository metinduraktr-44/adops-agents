---
name: canva-export
description: Define export formats and dimensions for Canva jobs. Use when finalizing CANVA_OPS manifests or export steps.
---

# Canva Export Skill

1. Read MATRIX/ for target format and dimensions.
2. Manifest fields: `export_formats[]`, `dimensions`, `design_id` (FULL mode only).
3. BRIEF-ONLY: document intended exports without MCP call.
4. Validate with `scripts/spec_validate.py`.
