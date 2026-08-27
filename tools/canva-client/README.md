# canva-client (SCAFFOLD)

Türkçe not: Canva Connect API istemcisinin **iskeletidir** (Bölüm 9, Mod A2). Şu an
hiçbir gerçek API çağrısı yapmaz; tüm metotlar `NotImplementedError` fırlatır.

TypeScript scaffold for the Canva Connect API client used by the Creative Agency OS.

## Status: stubs only — no network, no secrets
- Every method is a documented stub. Nothing calls the real Canva API yet.
- **OAuth is a user action.** This client never stores or requests secrets. Provide
  `clientId` / `redirectUri` at runtime; keep tokens in memory or a secure store.
- All endpoints/scopes/field names are marked `DOC-VERIFY` — confirm them against the
  official docs before implementing: <https://www.canva.dev/docs/connect/>

## Layout
- `src/types.ts` — shared interfaces (all field names DOC-VERIFY).
- `src/poll.ts` — `pollJob` + `withRetry` (exponential backoff + jitter).
- `src/log.ts` — writes `CANVA_OPS/ERRORS.md` (errors) and `CANVA_OPS/DESIGN_REGISTRY.csv` (append-only).
- `src/index.ts` — `CanvaClient` with OAuth2 PKCE, token refresh, asset upload,
  autofill+poll, resize job, export job.

## Build (no deps installed here)
```bash
# from tools/canva-client (installs devDeps: typescript, @types/node)
npm install
npm run typecheck   # or: npm run build
```
Dependencies are intentionally **not** installed in this scaffold pass and no network
calls are made. Run the above yourself when you are ready to develop the client.

## Intended flow (see `exampleProductionFlow` in `src/index.ts`)
1. User completes OAuth (browser) → `buildAuthorizeUrl` → `exchangeCodeForToken`.
2. `uploadAsset` → `autofillDesign` (bulk) → `resizeDesign` → `exportDesign`.
3. `registerDesign(...)` records each result; failures go to `ERRORS.md`.
