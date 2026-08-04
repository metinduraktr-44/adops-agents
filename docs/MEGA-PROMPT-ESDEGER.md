# MEGA PROMPT EŞDEĞERİ (900B talebinin gerçekçi hali)
> Damga: 2026-08-04T09:52:37Z

## 🚩 Red flag
`≥900.000.000.000 karakter` tek dosya/prompt **üretilemez** ve üretilmemelidir (disk, token, sinyal sıfır).

## Eşdeğer (uygulandı)
1. Yoğun şablon: `data/prompt_bank/{title,team,apply}.json`
2. Runtime genişletme katmanları: `data/prompt_bank/mega/EXPAND-RECIPE.json`
3. Örnek genişletilmiş dosyalar: `data/prompt_bank/mega/T-*.md`
4. Title soru setleri (≥500): `data/title_questions/`
5. Top-100 kuyruk: `data/title_top100_queues.json`

## Nasıl kullanılır
```bash
# title id seç → katmanları oku → soru setinden örnekle → çalıştır
python3 -c "import json;print(json.load(open('data/prompt_bank/mega/EXPAND-RECIPE.json'))['layers'])"
```

Effective prompt depth = model context window, not a vanity character count.
