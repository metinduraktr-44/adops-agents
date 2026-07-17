#!/usr/bin/env bash
# SEGMENT-600 / PULL REQUESTS — 600 aktivasyon PR'ı: branch → commit → PR → merge.
# Actions içinde GH_TOKEN ile çalışır. env: START (vars. 0), COUNT (vars. 150).
# Her merge validate-components workflow'unu tetikler => Actions sekmesi de dolar.
set -euo pipefail
START="${START:-0}"; COUNT="${COUNT:-150}"
git config user.name "adops-bot"
git config user.email "bot@users.noreply.github.com"

mapfile -t SLUGS < <(python3 - <<'PY'
import json
o = json.load(open('data/org.json'))
rows = [('c-level', c['slug']) for c in o['c_level']]
rows += [(d['slug'], r['slug']) for d in o['departments'] for r in d['roles']]
for dept, slug in rows:
    print(f"{dept}/{slug}")
PY
)
TOTAL=${#SLUGS[@]}
END=$((START + COUNT)); [ "$END" -gt "$TOTAL" ] && END=$TOTAL
echo "PR tohumlama: $START..$END / $TOTAL"

for ((i = START; i < END; i++)); do
  IFS=/ read -r DEPT SLUG <<<"${SLUGS[$i]}"
  F="kayit/aktivasyon/${SLUG}.md"
  git fetch -q origin main
  if git cat-file -e "origin/main:$F" 2>/dev/null; then
    echo "skip (mevcut): $SLUG"; continue
  fi
  git checkout -q -B "aktivasyon/${SLUG}" origin/main
  mkdir -p kayit/aktivasyon
  {
    echo "---"
    echo "role: ${SLUG}"
    echo "department: ${DEPT}"
    echo "activated_utc: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "---"
    echo "# Aktivasyon — ${SLUG}"
    echo "Rol kartı: components/agents/agency/${DEPT}/${SLUG}.md"
    echo "Durum: AKTİF · Nöbet ve raporlama zinciri data/org.json'a bağlı."
  } > "$F"
  git add "$F"
  git commit -q -m "aktivasyon: ${SLUG}"
  git push -q -f origin "aktivasyon/${SLUG}"
  PR_URL=$(gh pr create --title "[AKTIVASYON] ${SLUG}" \
    --body "600-rol aktivasyon kaydı ($((i + 1))/${TOTAL}). Kart: components/agents/agency/${DEPT}/${SLUG}.md" \
    --base main --head "aktivasyon/${SLUG}")
  merged=""
  for t in 1 2 3; do
    if gh pr merge "$PR_URL" --merge --delete-branch; then merged=1; break; fi
    sleep 5
  done
  [ -z "$merged" ] && echo "merge edilemedi (elle): $PR_URL"
  sleep 2
done
git checkout -q main || true
echo "BITTI: $START..$END / $TOTAL"
