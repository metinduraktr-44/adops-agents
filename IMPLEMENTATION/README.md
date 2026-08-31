# IMPLEMENTATION — Stubs (MODE=IMPLEMENT only)

> Damga: 2026-08-27T12:40:00Z · **Blocked** while MODE=ASSESS-ONLY

When owner sets `MODE=IMPLEMENT` in SECURITY_STATE.md:

1. Create change ticket under CHANGE/ CAB gates
2. Add implementation note here with control IDs
3. Prefer config-as-code PRs; no secret material
4. Verify with security-qa skill + `/sec-etik-denetim`

```text
# Example stub (do not execute as offense)
# control: ENC-011
# change: hybrid TLS planning note
# secret refs: vault://pki/tls-cert  OR  ${TLS_CERT_PATH}
```
