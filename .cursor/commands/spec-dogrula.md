---
description: Validate MATRIX and CANVA_OPS specs via spec_validate.py hook.
---
# /spec-dogrula

```bash
python3 scripts/spec_validate.py MATRIX/ CANVA_OPS/
python3 scripts/validate.py
```

1. Fix reported dimension/format/brief-ref issues.
2. Pillow checks optional — script exits 0 if only Pillow missing.

Skill: `.cursor/skills/spec-validate/SKILL.md`
