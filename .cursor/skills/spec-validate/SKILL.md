---
name: spec-validate
description: Run MATRIX/ and CANVA_OPS/ validation via scripts/spec_validate.py. Use for /spec-dogrula.
---

# Spec Validate Skill

```bash
python3 scripts/spec_validate.py MATRIX/ CANVA_OPS/
```

1. Fix structural issues (missing keys, invalid canva_mode).
2. Pillow optional — image checks skip if missing.
3. Re-run until SPEC_VALIDATE: GECTI.
