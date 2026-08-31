---
description: Start LATOS GIGA — Faz 0 bootstrap, read LATOS_STATE, confirm phase.
---
# /latos-baslat (alias /baslat for LATOS)

```bash
cat LATOS_STATE.md
head -n 80 docs/LATOS-GIGA-BOOTSTRAP.md
python3 scripts/generate_latos_giga_pack.py --git-scan
```

1. Read `LATOS_STATE.md` + `.cursor/plans/latos-master-plan.md`
2. Confirm `CONTEXT/CONTEXT_BRIEF.md` exists; drop inbox files in `CONTEXT/INBOX/`
3. Verify 600 titles in `ROSTER/TITLE_INVENTORY.md`
4. **Restart Cursor** after first bootstrap (skill discovery)
5. Stamp AUDIT_LOG after work block
