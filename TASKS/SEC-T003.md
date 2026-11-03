# SEC-T003 — MODE=IMPLEMENT unlock criteria

> Damga: 2026-11-03T11:50:00Z · MODE stays **ASSESS-ONLY** until the owner signs below.
> TR: Ajan MODE’u kendi çevirmez. Kişi/900B prompt uydurulmaz.

This file **defines** the unlock checklist. It does **not** flip `SECURITY_STATE.md`.
SEC-T002 (expert sample review) stays open; do not invent reviewers.

## Hard gates (all required)

Owner Metin must confirm each item in `SECURITY_STATE.md` (date + initials) before any `MODE=IMPLEMENT` line:

| # | Gate | Evidence | Owner |
|---|---|---|---|
| 1 | Cursor restart done so `.cursor/skills`, rules, and hooks load | local session after pull | [ ] |
| 2 | `python3 scripts/validate.py` → `VALIDATION: GECTI` on the intended commit | CI or local log | [ ] |
| 3 | `python3 scripts/ethics_check.py .` exit 0 | log | [ ] |
| 4 | `python3 scripts/secret_scan.py .` exit 0; no plaintext secrets in git | log + `git grep` hygiene | [ ] |
| 5 | Defense-only still holds: no exploit/PoC, no phishing lures, no live remediations in ASSESS | ethics hook + this pack | [ ] |
| 6 | MCP security catalog remains **off** unless owner enables with `${VAR}` / vault | `.cursor/mcp.json` | [ ] |
| 7 | LLM keys only in env / `.env.local` (gitignored). Rotation: `docs/LLM-ENV.md` | env presence, never commit | [ ] |
| 8 | SEC-T002 sample mapping review **or** explicit owner waiver of T002 | dated note in `SECURITY_STATE.md` | [ ] |
| 9 | IMPLEMENTATION/ + CHANGE CAB template used for any control mutation | CHANGE family | [ ] |
| 10 | Owner personally sets `MODE` to IMPLEMENT in `SECURITY_STATE.md` (agents must not auto-flip) | git blame on that line | [ ] |

## After unlock (still defense-only)

- Order remains assess → implement → audit. No skip.
- SBOM/provenance (SEC-T010) may start only after this flip.
- Canva pack stays `CANVA:BRIEF-ONLY` until separate OAuth; this checklist does not enable Canva.

## Status

- Checklist **authored** 2026-11-03 (this file).
- Sign-off: **open** (owner).
- MODE: **ASSESS-ONLY**.
