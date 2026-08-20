---
name: holding-agency-router
description: Routes holding, subsidiary (OpCo), country LLM agency, and web/iOS/Android portfolio work for Performance Growth Holding. Use when the user mentions holding, iştirak, Permergrowth, VizaTrack, Movea, Cigkoftem, hukuk, ülke ajansı, or multi-app surfaces.
---

# Holding Agency Router

## Quick start
1. `data/holding.json`
2. OpCo doc: `docs/holding/istirakler/<id>.md`
3. Expand personal + group workflows from JSON
4. Sample questions from `holding_soru_bloklari` + 501 bank
5. Stamp AUDIT_LOG / BILGI_TABANI

## Commands
- `/holding-konsolide` → portfolio report
- `/gece-holding-arastirma` → nightly archive loop

## Hard rules
Signal > length. Sourced people only. No API key minting without owner account.
