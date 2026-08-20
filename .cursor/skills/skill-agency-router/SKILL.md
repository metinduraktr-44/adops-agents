---
name: skill-agency-router
description: Routes Cursor plugin skills and MCPs into AdOps LLM mini-agencies by family. Use when the user names a /skill, asks to run all skills, or requests MCP routing for the agency.
---

# Skill Agency Router

## Instructions

1. Open `data/skill_agency_registry.json`.
2. Find the skill in `skills[]` → resolve `family`.
3. Load matching prompt from `data/prompt_bank/skill_families.json` (`FAM-<family>`).
4. Use family `titles[]` for RACI (EVP→Analyst).
5. Before any MCP call: `GetMcpTools` for the server. If `needsAuth` → 🚩 and continue offline with docs only.
6. Stamp `AUDIT_LOG.jsonl`; append learning to `BILGI_TABANI.md`.
7. Never invent top-100 people or pad prompts (K-003).

## Examples

User: `/firecrawl-scrape competitor landing pages`
→ family `web-intel` → dept `seo` → MCP Bright Data / Apify / Firecrawl → specialist executes → archive.

User: `/twilio-sms-send-message`
→ family `comms-twilio` → needs Twilio auth → if missing 🚩.

## Performance Notes

- Prefer registry lookup over scanning skill folders.
- Progressive disclosure: do not load all skill bodies.

## Troubleshooting

- Skill not in registry: re-run `python3 scripts/build_skill_agency_registry.py`.
- MCP rate limit: fall back to WebSearch / docs MCP; record 🚩.
