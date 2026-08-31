---
description: Generate prompt index batch — 122-slot progressive expansion.
---
# /latos-prompt-uret

Args: `{title|team|execution}` + `{slug}`

1. Expand `PROMPTS/{KIND}/{slug}/P###.md` batch
2. Cross-ref `data/prompt_bank/` baseline
3. 🚩 900M chars/prompt = impossible — dense templates + `/devam`
