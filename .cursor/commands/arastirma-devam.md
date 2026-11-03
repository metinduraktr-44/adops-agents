---
name: arastirma-devam
description: Continue the LLM-agency research loop (archive-first, no live skill invoke, pending_research only).
---

# /arastirma-devam

## TR
Arşiv-önce araştırma döngüsü: önceki `data/arsiv` damgasını oku, `title_top100` kuyruğunu **pending bırak**, skill registry damgala, `research_loop.py` çalıştır. Skill'leri canlı çağırma.

## Run
```bash
python3 scripts/research_loop_continue.py
python3 scripts/validate.py
```

## Guardrails
🚩 K-003: isim uydurma yok · 900B blob yok · plaintext secret yok
Security MODE dokunulmaz (ASSESS-ONLY).
