---
description: Daily forecast batch for a title — Brier-calibrated workflow.
---
# /latos-tahmin

Args: `{slug}` + optional date

1. Append to `FORECASTS/{slug}/YYYY-MM-DD.md`
2. Workflow target 200/day — batch size per session, not one-shot 200×600
3. Mark unverified without source URL
4. Update `FORECASTS/CALIBRATION.md` on resolution
