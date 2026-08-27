---
description: Ethics audit — refuse offense; scan for exploit keywords and secrets.
---
# /sec-etik-denetim

```bash
python3 scripts/ethics_check.py .
python3 scripts/secret_scan.py .
```

1. Fail closed on exploit/PoC/phishing patterns in generated content.
2. Confirm defense-only outputs.
3. Record result in AUDIT_LOG.
