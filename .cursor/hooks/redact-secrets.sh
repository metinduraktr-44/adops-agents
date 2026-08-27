#!/usr/bin/env bash
# Redact common secret-shaped tokens from read paths (best-effort).
set -euo pipefail
# Hook environments vary; if a file path is provided, scan it.
TARGET="${CURSOR_FILE_PATH:-${1:-}}"
if [[ -n "$TARGET" && -f "$TARGET" ]]; then
  python3 scripts/secret_scan.py --redact-check "$TARGET" || true
fi
exit 0
