# FORECAST CALIBRATION

> Damga: 2026-08-27T20:16:49Z · Tetlock + Brier practices

## Targets (progressive — not one-shot)
- Per title: **200 forecasts/day** workflow via `/latos-tahmin` + Cloud Agent
- 🚩 Claiming 200×600 titles in one commit = impossible

## Brier score reference
- Superforecaster benchmark ~0.166
- General public ~0.259
- Track in `FORECASTS/CALIBRATION.md` after resolutions

## Template (`FORECASTS/{title}/YYYY-MM-DD.md`)
```yaml
forecasts:
  - id: F001
    claim: "..."
    probability: 0.65
    resolve_by: 2026-08-27
    status: open
    source_url: required-or-unverified
```

## Recalibration gate
If Brier worsens 2 weeks → human review + adjust base rates.
