# LLM ENV
> TR: Anahtarlar sadece lokal `.env.local` — asla commit etme.

## Setup
```bash
# .env.local (gitignored)
OPENROUTER_API_KEY=sk-or-v1-...
OPENROUTER_MODEL=anthropic/claude-sonnet-4
LLM_PROVIDER=openrouter
```

## Test
```bash
python3 scripts/llm_client.py   # expect: reply PONG
FORCE_LLM_ARTICLE=1 python3 scripts/daily_ops.py
```

## Priority
1. OPENROUTER_API_KEY (preferred)
2. ANTHROPIC_API_KEY (fallback)
3. none → deterministic skeleton (loop never breaks)
