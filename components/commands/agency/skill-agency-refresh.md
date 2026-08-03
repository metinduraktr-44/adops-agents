---
name: skill-agency-refresh
description: Rebuild skill→agency registry and archive stamp. Use when skills inventory changes or monthly research runs.
---

# /skill-agency-refresh

```bash
python3 scripts/build_skill_agency_registry.py
python3 scripts/validate.py
```

Outputs: `data/skill_agency_registry.json`, `docs/SKILL-AGENCY-REGISTRY.md`, `data/prompt_bank/skill_families.json`, archive snapshot, activation doc append.
