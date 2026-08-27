#!/usr/bin/env bash
# Fail-closed block for dangerous shell patterns. Defense-only.
set -euo pipefail
CMD="${CURSOR_SHELL_COMMAND:-${1:-}}"
if [[ -z "$CMD" && ! -t 0 ]]; then
  CMD=$(cat || true)
fi
PATTERNS=(
  'rm[[:space:]]+-rf[[:space:]]+/'
  'curl[^
]*\|[[:space:]]*bash'
  'curl[^
]*\|[[:space:]]*sh'
  'wget[^
]*\|[[:space:]]*bash'
  'wget[^
]*\|[[:space:]]*sh'
  'base64[[:space:]]+-d[^
]*\|[[:space:]]*sh'
  'mkfs\.'
  ':(){:|:&};:'
)
for pat in "${PATTERNS[@]}"; do
  if echo "$CMD" | grep -Eiq "$pat"; then
    echo "[block-dangerous] refused pattern: $pat" >&2
    exit 2
  fi
done
exit 0
