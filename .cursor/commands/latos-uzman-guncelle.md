---
description: Update expert queue for a title — sourced + pending_research only.
---
# /latos-uzman-guncelle

Args: `{slug}`

1. Read `data/title_top100_queues.json` discipline queue if mapped
2. Update `EXPERTS/{slug}/top100_YYYY-MM-DD.md`
3. READ→DELTA→DIFF→WRITE→DIGEST prior archive
4. No invented names — URL or `pending_research`
5. Human approval before marking `sourced`
