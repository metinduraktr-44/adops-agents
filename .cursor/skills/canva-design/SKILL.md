---
name: canva-design
description: Create or edit Canva designs via MCP in FULL mode, or write BRIEF-ONLY manifests in CANVA_OPS/. Use for /canva-uret.
---

# Canva Design Skill

1. Check `STATE.md` → `CANVA_MODE`.
2. **BRIEF-ONLY:** Write `CANVA_OPS/<job-id>.json` with brief_ref, matrix_ref, export intent.
3. **FULL:** `GetDynamicTools` Canva namespace → discover schema → create/edit → record design IDs.
4. Auth failure → 🚩 owner OAuth; continue with manifest stub.
5. Never commit tokens.
