#!/usr/bin/env bash
# 7/24 CANLI AJANS DÖNGÜSÜ — heartbeat + validate + timestamp (deterministik; LLM opsiyonel).
# Başlat:  bash scripts/live_loop.sh
# Aralık:  LIVE_INTERVAL saniye (varsayılan 300). Durdur: Ctrl-C veya tmux kill-session.
set -uo pipefail
cd "$(dirname "$0")/.."
INTERVAL="${LIVE_INTERVAL:-300}"
PROV="$( { command -v python3 >/dev/null && python3 scripts/llm_client.py 2>/dev/null | head -1; } || echo 'provider: (yok)')"
echo "[live] başladı $(date -u +%FT%TZ) · interval=${INTERVAL}s · ${PROV}"
i=0
while true; do
  i=$((i + 1))
  TS=$(date -u +%FT%TZ)
  OUT=$(python3 scripts/validate.py 2>&1 | tail -1)
  bash scripts/timestamp.sh "live-heartbeat-${i}" >/dev/null 2>&1 || true
  echo "[live] #${i} ${TS} · ${OUT}"
  sleep "${INTERVAL}"
done
