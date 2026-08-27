#!/usr/bin/env bash
# Cursor beforeShellExecution hook — block dangerous shell commands (FAIL-CLOSED).
#
# GUARDRAIL AKTIF — savunma-only, secret-redakte, exploit-yok.
#
# Turkce not: Tehlikeli kabuk komutlarini engeller. stdin'den hook JSON okur,
# komut icinde yikici desen (rm -rf, curl|sh, wget|sh) ararsa {"permission":"deny"}
# doner. Belirsizlik/hata durumunda FAIL-CLOSED: guvenli tarafta kalip "deny" doner
# (bu hook yalnizca zaten tehlikeli-eslesme matcher'i ile cagrilir).
#
# I/O: reads JSON on stdin, writes a hook-decision JSON to stdout, exits 0.
set -u

# Read stdin defensively (may be empty).
INPUT="$(cat 2>/dev/null || true)"

emit() {
  # $1 = permission (deny|ask|allow), $2 = message
  printf '{"permission":"%s","userMessage":"%s"}' "$1" "$2"
}

# Extract a "command" field from the JSON without requiring jq.
# Best-effort: grab the first command-like string; fall back to whole payload.
CMD="$INPUT"
if command -v python3 >/dev/null 2>&1; then
  PARSED="$(printf '%s' "$INPUT" | python3 -c '
import sys, json
try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(0)
def find(o):
    if isinstance(o, dict):
        for k in ("command", "cmd", "shellCommand", "script"):
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
  if [ -n "${PARSED:-}" ]; then
    CMD="$PARSED"
  fi
fi

# Dangerous patterns (defensive denylist).
DANGER='rm[[:space:]]+-rf|curl.*\|.*sh|wget.*\|.*sh|:\(\)\{|mkfs|dd[[:space:]]+if=|>[[:space:]]*/dev/sd'

if printf '%s' "$CMD" | grep -Eq "$DANGER"; then
  emit "deny" "block-dangerous: yikici komut deseni engellendi (savunma-only, fail-closed). Gozden gecirin."
  exit 0
fi

# No dangerous pattern found -> allow this specific command.
emit "allow" ""
exit 0
