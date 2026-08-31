# CANVA_OPS — MCP Tools & OAuth

Türkçe not: Canva MCP sunucusu `.cursor/mcp.json` içinde **yalnızca URL** ile
tanımlıdır. **OAuth bir kullanıcı eylemidir** — sırlar repoya konmaz.

## MCP server
- Configured in `.cursor/mcp.json`:
  ```json
  { "mcpServers": { "canva": { "url": "https://mcp.canva.com/mcp" } } }
  ```

## OAuth (user action — required before CANVA:ON)
1. The user connects/authorizes the Canva MCP server in the Cursor IDE (browser consent).
2. No client secret, token, or key is stored in this repo. Ever.
3. Until OAuth is complete, stay in `CANVA:BRIEF-ONLY` (dry-run).

## Tool discovery
- Before calling any Canva MCP tool, discover its schema first.
- If the server reports `needsAuth`, red-flag (🚩) and continue in dry-run.

## Expected tool families (DOC-VERIFY against Canva MCP)
- design create / edit
- autofill (bulk create from data)
- resize
- export
- asset upload

> Fall back to `tools/canva-client/` (Connect API scaffold) only when MCP is unavailable.
> That client is stubs-only today and makes no live calls.
