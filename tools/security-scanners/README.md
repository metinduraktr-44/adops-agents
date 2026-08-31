# tools/security-scanners/ — validation wrappers (scaffold)

GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok.

Türkçe not: Bu klasör, savunma-amaçlı doğrulama sarmalayıcılarının (wrapper) iskeletidir.
Hiçbir bağımlılık kurulmaz, hiçbir ağ çağrısı yapılmaz. Gerçek tarayıcılar (Semgrep,
Trivy, OPA vb.) `.cursor/mcp.json` üzerinden **varsayılan KAPALI** MCP sunucularıyla veya
kullanıcı tarafından ayrıca kurulur.

## What these are
Thin, dependency-free wrappers that shell out to external scanners **only if they are
already installed and the owner opts in**. By default they run in a safe, offline
"scaffold" mode: they explain what they would do and exit 0. They never install packages,
never phone home, and never write secret values.

| wrapper | purpose | external tool (optional, user-installed) |
|---|---|---|
| `secret_scan.py` | delegate to repo secret hygiene scan | (uses stdlib; mirrors `scripts/secret_scan.py`) |
| `control_validate.py` | check control rows carry required standard-mapping fields | (none; stdlib) |
| `opa_test.sh` | run OPA/Rego policy tests if `opa` is on PATH | `opa` (Open Policy Agent) |

## Rules
- DOC-VERIFY: verify tool names, flags, and standard versions against official docs before production.
- No secrets in code or output; reference `${VAR}`/`vault://`/`op://` only.
- No network side-effects; no `npm install`/`pip install`; MODE=ASSESS-ONLY.
