---
description: Archive current LATOS artifacts — ancestor preservation.
---
# /latos-arsivle

```bash
STAMP=$(date -u +%Y-%m-%d_%H%M)
mkdir -p "ARCHIVE/$STAMP"
```

1. Copy changed LATOS dirs to `ARCHIVE/$STAMP/` (LATOS_STATE, JOB_CARDS delta, EXPERTS)
2. **Never delete** prior ARCHIVE folders
3. Append AUDIT_LOG + BILGI_TABANI learning
