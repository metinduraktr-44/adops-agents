# tools/security-scanners

Defense-only scaffolding.

| Tool | Path | Purpose |
|---|---|---|
| secret_scan | `scripts/secret_scan.py` | Detect secret-shaped tokens; redact |
| ethics_check | `scripts/ethics_check.py` | Block exploit-oriented generated content |
| validate | `scripts/validate.py` | Repo structural gate |

## Spec validate (security)

```bash
python3 tools/security-scanners/run_checks.py
```

Exit non-zero on findings. No exploit payloads.
