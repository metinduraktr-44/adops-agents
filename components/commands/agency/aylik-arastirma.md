---
name: aylik-arastirma
description: "Run the monthly LLM-agency research archive loop (read prior stamp → refresh → stamp)."
---

# /aylik-arastirma

## TR
Aylık araştırma arşiv döngüsünü çalıştırır: önceki `data/arsiv/YYYY-MM` damgasını okur, paketleri yeniler, AUDIT_LOG + BILGI_TABANI günceller.

## Run
```bash
python3 scripts/monthly_research_refresh.py
```

## Outputs
- `data/arsiv/<YYYY-MM>/snapshot.json` + `NOTES.md`
- `data/ozel_yetenekler.json` (≥100)
- `data/prompt_bank/{title,team,apply}.json` (122 each)
- `docs/CLAUDE-CODE-AKTIVASYON.md` (paste-ready)

## Guardrails
🚩 Do not invent top-100 people lists. 🚩 Do not pad prompts to absurd character counts (K-003).
