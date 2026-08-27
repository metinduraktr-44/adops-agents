#!/usr/bin/env bash
# Cursor beforeReadFile hook — secret redaction advisory (FAIL-OPEN).
#
# GUARDRAIL AKTIF — savunma-only, secret-redakte, exploit-yok.
#
# Turkce not: Okunmak istenen dosya gizli-bilgi tasiyabilecek turdeyse
# (.env, *.pem, *.key, id_rsa, credentials) ajani uyarir. Dosya icerigini
# ASLA stdout'a yazmaz; yalnizca uyari doner. Bloklamaz (fail-open): her zaman
# {"permission":"allow"} veya {} doner, exit 0. Gercek redaksiyon istemci
# tarafinda uygulanir; bu hook danismanlik amaclidir.
#
# I/O: reads JSON on stdin, writes advisory JSON to stdout, exits 0.
set -u

INPUT="$(cat 2>/dev/null || true)"

# Best-effort path extraction without jq.
PATHV=""
if command -v python3 >/dev/null 2>&1; then
  PATHV="$(printf '%s' "$INPUT" | python3 -c '
import sys, json
try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(0)
def find(o):
    if isinstance(o, dict):
        for k in ("file_path", "filePath", "path"):
            v = o.get(k)
            if isinstance(v, str):
                return v
        for v in o.values():
            r = find(v)
            if r:
                return r
    elif isinstance(o, list):
        for v in o:
            r = find(v)
            if r:
                return r
    return ""
print(find(d))
' 2>/dev/null)"
fi

# Sensitive filename patterns.
SENSITIVE='(^|/)(\.env(\..+)?|credentials|.*\.pem|.*\.key|id_rsa|id_dsa|id_ecdsa|id_ed25519)$'

if [ -n "${PATHV:-}" ] && printf '%s' "$PATHV" | grep -Eq "$SENSITIVE"; then
  printf '{"permission":"allow","userMessage":"redact-secrets: hassas dosya (%s) — plaintext secret beklemeyin; ${VAR}/vault://op:// kullanin."}' "gizli-bilgi turu"
  exit 0
fi

# Not sensitive (or unknown path) -> no-op, fail-open.
printf '{}'
exit 0
