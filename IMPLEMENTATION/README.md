# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

# IMPLEMENTATION — defensive rollout artifacts (skeleton)

Türkçe not: Kontrollerin uygulanma çıktıları — sertleştirme rehberleri, tespit kuralları (Sigma/YARA/EDR), IR runbook'ları, policy-as-code (OPA/Rego). MODE=ASSESS-ONLY: artefakt üret, canlı sisteme uygulama.

## Contents (fill in phases)
- `hardening/` — baseline hardening guides per layer.
- `detections/` — Sigma/YARA/EDR rules (descriptive; ATT&CK ids only to justify detection).
- `runbooks/` — incident-response runbooks (NIST 800-61 — verify).
- `policies/` — OPA/Rego policies (test via `tools/security-scanners/opa_test.sh`).

## Rules
- Defense-only; no offensive PoC/payloads/bypasses. No secrets (`${VAR}`/`vault://`/`op://`).
- Every artifact references the control id(s) it implements.
