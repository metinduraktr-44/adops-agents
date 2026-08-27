---
description: Monthly research refresh + archive cycle for GIGA creative agency.
---
# /aylik-dongu

```bash
python3 scripts/monthly_research_refresh.py 2>/dev/null || echo "monthly script optional"
```

1. Refresh EXPERTS/ pending_research queues (no invented bios).
2. Archive completed BRIEFS/ + MATRIX/ + CANVA_OPS/ → `ARCHIVE/YYYY-MM/`.
3. Update STATE.md phase markers.
4. Run `python3 scripts/validate.py`.
5. Stamp AUDIT_LOG + BILGI_TABANI learning.
