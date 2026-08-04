#!/usr/bin/env bash
# Live terminal ops — her katmanı stdout'a basar (TR not: canlı döngü).
# Usage: ./scripts/live_ops.sh            # tek tick
#        ./scripts/live_ops.sh --loop 120 # N sn aralıkla sürekli
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
# Load local secrets (gitignored) — never echo values
set -a
[[ -f "$ROOT/.env.local" ]] && . "$ROOT/.env.local"
[[ -f "$ROOT/.env" ]] && . "$ROOT/.env"
set +a
INTERVAL="${2:-120}"
LOOP=0
[[ "${1:-}" == "--loop" ]] && LOOP=1

banner() {
  echo ""
  echo "╔══════════════════════════════════════════════════════════════╗"
  echo "║  $1"
  echo "╚══════════════════════════════════════════════════════════════╝"
}

tick() {
  local ts
  ts="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  banner "LIVE TICK $ts"
  echo "[cwd] $ROOT"
  echo "[branch] $(git branch --show-current 2>/dev/null || echo '?')"
  echo "[commit] $(git rev-parse --short HEAD 2>/dev/null || echo '?')"
  if [[ -n "${OPENROUTER_API_KEY:-}" ]]; then
    echo "[llm] OPENROUTER set model=${OPENROUTER_MODEL:-default}"
  elif [[ -n "${ANTHROPIC_API_KEY:-}" ]]; then
    echo "[llm] ANTHROPIC set"
  else
    echo "[llm] NO KEY (skeleton mode)"
  fi

  banner "1/8 apply_activation.py"
  python3 -u scripts/apply_activation.py
  echo "exit=$?"

  banner "2/8 build_k003_equivalents.py"
  python3 -u scripts/build_k003_equivalents.py
  echo "exit=$?"

  banner "3/8 holding_report.py"
  python3 -u scripts/holding_report.py
  echo "exit=$?"

  banner "4/8 nightly_holding_research.py"
  python3 -u scripts/nightly_holding_research.py
  echo "exit=$?"

  banner "5/8 daily_ops.py"
  python3 -u scripts/daily_ops.py
  echo "exit=$?"

  banner "6/8 validate.py"
  python3 -u scripts/validate.py
  echo "exit=$?"

  banner "7/8 durum özeti"
  echo "--- AKTIVASYON-DURUM.md (ilk 40 satır) ---"
  head -n 40 docs/AKTIVASYON-DURUM.md 2>/dev/null || echo "(yok)"
  echo "--- holding.json özet ---"
  python3 - <<'PY'
import json
from pathlib import Path
h=json.loads(Path("data/holding.json").read_text(encoding="utf-8"))
print(f"holding={h.get('name')} opcos={len(h.get('subsidiaries',[]))} countries={len(h.get('country_agencies',[]))}")
for s in h.get("subsidiaries",[]):
    print(f"  · {s['id']}: {s['name']}")
for c in h.get("country_agencies",[]):
    print(f"  · country {c.get('code',c.get('id','?'))}: {c.get('name','')}")
PY
  echo "--- title_questions ---"
  python3 - <<'PY'
from pathlib import Path
p=Path("data/title_questions")
files=sorted(p.glob("*.json")) if p.exists() else []
print(f"files={len(files)}")
if files:
    import json
    d=json.loads(files[0].read_text(encoding="utf-8"))
    titles=d.get("titles") or d.get("by_title") or d
    if isinstance(titles, dict):
        first=next(iter(titles.values()))
        n=len(first) if isinstance(first, list) else "?"
        print(f"sample_file={files[0].name} first_title_q_count={n}")
    print(f"top100_queue={'OK' if Path('data/title_top100_queues.json').exists() else 'MISSING'}")
PY
  echo "--- AUDIT_LOG son 3 ---"
  tail -n 3 AUDIT_LOG.jsonl 2>/dev/null || echo "(yok)"

  banner "8/8 LIVE OK @ $ts"
}

if [[ "$LOOP" -eq 1 ]]; then
  echo "[LIVE] continuous loop interval=${INTERVAL}s started $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  while true; do
    tick
    echo "[LIVE] sleeping ${INTERVAL}s …"
    sleep "$INTERVAL"
  done
else
  tick
fi
