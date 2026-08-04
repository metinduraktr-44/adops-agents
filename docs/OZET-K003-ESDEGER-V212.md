# ÖZET — K-003 talep eşdeğerleri v2.12
> Damga: 2026-08-04T08:49:12Z

## Yapılan
1. **Title soruları:** 600 slug × ≥500 soru (max 500) → `data/title_questions/`
2. **Top-100 kuyruk:** 21 disiplin × 100 slot (kaynaklı + pending_query) → `data/title_top100_queues.json`
3. **Mega prompt:** expander recipe + sample files → `data/prompt_bank/mega/` · `docs/MEGA-PROMPT-ESDEGER.md`

## Yapılmayan (bilinçli 🚩)
- 900B karakterlik tek prompt dosyası
- Uydurma kişi isimleri
- 600 MD kartına 500'er soru gömmek

## Kullanım
- Soru: `data/title_questions/<dept>.json` → `roles[<slug>].questions`
- Uzman: yalnızca `status=sourced`; pending için aylık araştırma
- Prompt: dense bank + EXPAND-RECIPE katmanları
