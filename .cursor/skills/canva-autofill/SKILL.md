---
name: canva-autofill
description: Canva Enterprise autofill workflows — plan-gated. Use only when owner confirms Enterprise plan and FULL mode.
---

# Canva Autofill Skill (Enterprise-only)

🚩 **Canva Autofill requires Enterprise plan.**

1. Confirm owner plan before any autofill MCP call.
2. If plan unknown → manifest stub with `"autofill": "pending_enterprise_confirm"`.
3. Never autofill in BRIEF-ONLY mode.
4. Document data fields mapped to brand template in CANVA_OPS/ manifest.
