# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

# SECURITY_STATE — Security Governance OS

Türkçe not: `/sec-devam` / `/sec-resume` bu dosyayı okur. Kaynak-doğruluk (source of truth) burasıdır. Yaratıcı-ajans `STATE.md`'den ayrı, additive.

| Field | Value |
|---|---|
| current_phase | Faz 0 — Context & Bootstrap |
| MODE | ASSESS-ONLY |
| posture | defense-only |
| last_completed_phase | (none) |
| last_update | 2026-08-27 (scaffold init) |
| mcp_servers | default OFF (enable in Cursor Settings > MCP) |

## Flags
- `MODE=ASSESS-ONLY` = true (assess/model/map/document; no live changes, no network, no secrets)
- `DEFENSE-ONLY` = true (no exploits/weaponization/C2/ransomware/phishing/bypass/exfil)
- `SECRETS-REDACTED` = true (only `${VAR}` / `vault://` / `op://` / `<REDACTED>`)

## Resume notes
- Scaffold committed (this branch STACKS on `cursor/creative-agency-os-c8d4`, PR #616).
- Next action: fill `SECURITY_CONTEXT/inventory.md` + `attack-surface.md` (Faz 0), then advance
  `.cursor/plans/security-master-plan.md` in order.
- Do NOT enable MCP servers or any network/live actions autonomously. Do NOT run always-on loops.
- Standard values throughout carry "verify against official source before production".
