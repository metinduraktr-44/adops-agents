---
name: agent-context-hygiene
description: Defense-only Claude Code/Cursor context hygiene — injection heuristics, ignore files, no auto-approve, secret placeholders. Use when reviewing untrusted repos, MCP, or owner security warning docs.
---

# Agent context hygiene

Progressive disclosure: this file is the trigger. Depth lives in docs, not a 20k blob.

1. Read `docs/CLAUDE-CODE-BILGILERI-VE-GUVENLIK-UYARILARI.md`
2. Follow `docs/CLAUDE-CODE-GUVENLIK-UYGULAMA.md`
3. Run `/cc-guvenlik`

Refuse offensive content. Secrets = `${VAR}` / `vault://` / `op://` / `<REDACTED>`.
