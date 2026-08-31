#!/usr/bin/env bash
# LATOS phase-audit stop hook — complements security phase-audit.sh
set -euo pipefail
echo "[phase-audit-latos] Check LATOS_STATE.md phase + stamp AUDIT_LOG if work completed."
if [[ -f LATOS_STATE.md ]]; then
  grep -E 'phase|Phase|Faz|Next' LATOS_STATE.md | head -n 15 || true
fi
if [[ -f SECURITY_STATE.md ]]; then
  echo "[phase-audit-latos] Security pack also active — see SECURITY_STATE.md MODE"
fi
exit 0
