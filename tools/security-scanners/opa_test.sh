#!/usr/bin/env bash
# tools/security-scanners/opa_test.sh — OPA/Rego policy test wrapper (scaffold).
#
# GUARDRAIL AKTIF — savunma-only, secret-redakte, exploit-yok.
#
# Turkce not: OPA (Open Policy Agent) yuklu ise `.rego` politika testlerini calistirir.
# Yuklu degilse guvenli sekilde bilgilendirir ve exit 0 doner. Hicbir sey kurmaz,
# hicbir ag cagrisi yapmaz. MODE=ASSESS-ONLY.
#
# Usage: tools/security-scanners/opa_test.sh [POLICY_DIR]
#
# TODO / DOC-VERIFY:
# - Verify `opa test` flags and Rego version against official OPA docs before production.
# - Policies live under CONDITIONAL/ or IMPLEMENTATION/ (policy-as-code).
set -u

POLICY_DIR="${1:-CONDITIONAL}"

if ! command -v opa >/dev/null 2>&1; then
  echo "[opa_test] 'opa' not installed — scaffold mode. Install OPA and re-run to test .rego policies."
  echo "[opa_test] would run: opa test \"$POLICY_DIR\" -v   (DOC-VERIFY flags)"
  exit 0
fi

if [ ! -d "$POLICY_DIR" ]; then
  echo "[opa_test] policy dir '$POLICY_DIR' not found — nothing to test (scaffold)."
  exit 0
fi

# Real run only when opa exists AND policies are present. No network.
echo "[opa_test] running: opa test \"$POLICY_DIR\" -v"
opa test "$POLICY_DIR" -v
exit $?
