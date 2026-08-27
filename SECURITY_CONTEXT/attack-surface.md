# Attack Surface — Defense View

> Damga: 2026-08-27T12:40:00Z · what to **protect**, not how to attack

## Surfaces

1. **Source repository** — unauthorized commits, secret commits, dependency confusion
2. **CI/CD workflows** — poisoned actions, over-privileged tokens (`${{ secrets.* }}` only)
3. **Cursor MCP integrations** — token theft if misconfigured; keep catalog minimal
4. **Generated scripts** — dangerous shell patterns (hooks **refuse/forbid** destructive wipe-root and pipe-to-shell idioms)
5. **Prompt / agent content** — prompt injection into agency components
6. **Data archives** — `data/arsiv/**` integrity and over-sharing
7. **Supply chain** — third-party actions, Python stdlib assumption (no pip deps today)

## Priority controls (map to families)
- Secrets → secret-hygiene + ENC/TC controls
- Change integrity → CHANGE + TRANSPARENT_CODE
- Identity to MCP/CI → CONDITIONAL + IAM
- Network egress assumptions → FIREWALLS (policy templates)
- Defense-in-depth docs → LAYERS

## Out of scope here
Exploit development, PoC content, and any weaponization — **forbidden** (defense-only).
