#!/usr/bin/env bash
# Stop hook: remind phase/MODE audit stamp.
set -euo pipefail
echo "[phase-audit] Check SECURITY_STATE.md MODE + stamp AUDIT_LOG if work completed."
if [[ -f SECURITY_STATE.md ]]; then
  grep -E 'MODE|Faz|Active' SECURITY_STATE.md | head -n 20 || true
fi
exit 0
