---
description: Gece holding araştırma döngüsü — ülke arşivi oku → araştır → damgala → yaz. Use for country market / holding research refresh.
---

# Gece Holding Araştırma

1. Prior: `data/arsiv/holding/<CC>/snapshot-*.json` (🔗)
2. `python3 scripts/nightly_holding_research.py`
3. Opsiyonel: WebSearch/Exa (auth varsa) ile competitors_top5 doldur — uydurma yok
4. Rol modelleri: `data/holding_rol_modelleri.json`
5. Soru örnekle: `data/holding_soru_bloklari.json` + 501 banka

K-003: karakter şişirme yok; boş liste > uydurma isim.
