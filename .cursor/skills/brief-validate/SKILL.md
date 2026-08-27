---
name: brief-validate
description: Structural validation for BRIEFS/ markdown — required sections and brand guardrails check.
---

# Brief Validate Skill

Required sections: objective, audience, tone, deliverables, constraints.

1. Scan BRIEFS/*.md for missing sections.
2. Cross-check tone against CONTEXT/brand.md.
3. Flag regulated claims per 10-brand-guardrails.mdc.
4. Report to QA/ or fix inline if requested.
