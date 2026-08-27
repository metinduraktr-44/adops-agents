# Canva Client (scaffold)

TypeScript/Node scaffold for optional direct Canva API integration alongside Cursor MCP.

**This repo does not run OAuth or store tokens.** Use Cursor MCP (`https://mcp.canva.com/mcp`) as primary path.

## Setup (when owner ready)

```bash
cd tools/canva-client
npm install
# Set CANVA_ACCESS_TOKEN in env — never commit .env
```

## Enterprise autofill

Canva Autofill API requires **Enterprise** plan. Document-only in BRIEF-ONLY mode.

## MCP vs client

| Path | Use |
|---|---|
| Cursor MCP | Recommended — OAuth via Cursor Authorize |
| This client | Optional automation / CI export jobs |

## Status

Scaffold only — implement after Phase 6 (Canva FULL) owner approval.
