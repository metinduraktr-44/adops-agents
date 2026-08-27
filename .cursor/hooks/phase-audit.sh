#!/usr/bin/env bash
# Cursor stop hook — security phase audit (FAIL-OPEN, advisory).
#
# GUARDRAIL AKTIF — savunma-only, secret-redakte, exploit-yok.
#
# Turkce not: Ajan durdugunda guvenlik-yonetisim OS fazini denetler:
# SECURITY_STATE.md ve .cursor/plans/security-master-plan.md icindeki acik
# maddeleri sayar, ARCHIVE/security-audit.log'a ozet yazar. Bloklamaz
# (advisory-only); her zaman {} doner ve exit 0.
#
# I/O: reads JSON on stdin, writes {} to stdout, exits 0.
set -u

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
PLAN="$REPO_ROOT/.cursor/plans/security-master-plan.md"
STATEF="$REPO_ROOT/SECURITY_STATE.md"
LOG_DIR="$REPO_ROOT/ARCHIVE"
LOG="$LOG_DIR/security-audit.log"

# Drain stdin so we are a well-behaved hook.
cat >/dev/null 2>&1 || true

TS="$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo unknown)"
OPEN="?"
if [ -f "$PLAN" ]; then
  OPEN="$(grep -c '\- \[ \]' "$PLAN" 2>/dev/null || echo '?')"
fi

# Best-effort advisory log; never fail the stop.
{
  mkdir -p "$LOG_DIR" 2>/dev/null || true
  printf '%s phase-audit open_items=%s plan=%s state=%s\n' \
    "$TS" "$OPEN" \
    "$( [ -f "$PLAN" ] && echo present || echo missing )" \
    "$( [ -f "$STATEF" ] && echo present || echo missing )" \
    >>"$LOG" 2>/dev/null || true
} 2>/dev/null || true

# Advisory only — never block the stop.
printf '{}'
exit 0
