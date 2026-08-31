---
description: Title discovery — refresh ROSTER/TITLE_INVENTORY from org.json + git.
---
# /latos-title-kesif

```bash
python3 scripts/generate_latos_giga_pack.py --git-scan --force
python3 scripts/qa_check.py
```

- Rescan org.json (600 slugs)
- Git deleted paths: read-only log; restore needs human approval
- Update `ROSTER/TITLE_INVENTORY.md`
