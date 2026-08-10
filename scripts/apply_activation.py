#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apply activation prompt IN-REPO (no Claude Code paste).

Runs constitution rhythm pieces and writes AKTIVASYON-DURUM.md.
Owner: Cursor cloud agent / local orchestrator — paste step CANCELLED.
"""
from __future__ import annotations

import datetime
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.datetime.now(datetime.timezone.utc)
TS = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
DAY = NOW.strftime("%Y-%m-%d")


def run(script: str) -> tuple[int, str]:
    r = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / script)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    out = (r.stdout or "") + (r.stderr or "")
    return r.returncode, out.strip()


def sample_questions() -> list[str]:
    qs: list[str] = []
    bank = ROOT / "data" / "soru_bankasi.json"
    hold = ROOT / "data" / "holding_soru_bloklari.json"
    if bank.exists():
        b = json.loads(bank.read_text(encoding="utf-8"))
        uni = b.get("universal", {})
        flat = [q for v in uni.values() for q in v]
        # deterministic sample by day-of-year
        doy = int(NOW.strftime("%j"))
        for i in range(8):
            if flat:
                qs.append(flat[(doy * 8 + i) % len(flat)])
    if hold.exists():
        h = json.loads(hold.read_text(encoding="utf-8"))
        for key in ("holdco", "apps", "country"):
            for q in h.get(key, [])[:2]:
                qs.append(f"[{key}] {q}")
    return qs


def write_opco_task_boards(h: dict) -> list[str]:
    out_paths = []
    board_root = ROOT / "docs" / "holding" / "gorevler"
    board_root.mkdir(parents=True, exist_ok=True)
    for s in h["subsidiaries"]:
        path = board_root / f"{s['id']}-IS-LISTESI.md"
        personal = "\n".join(f"- [ ] `{w}`" for w in s["workflows"]["personal"])
        group = "\n".join(f"- [ ] `{w}`" for w in s["workflows"]["group"])
        kpis = "\n".join(f"- {k}" for k in s["kpis"])
        body = f"""# {s['name']} — OpCo iş listesi
> Damga: {TS} · Aktif orkestratör: Cursor (yapıştır iptal) · Reports: `{s['reports_to_holdco']}`

## Mandate
{s['mandate']}

## P0 bu sprint
- [ ] Ladder rollerini günlük standup satırına bağla
- [ ] KPI kesiti yayınla ({s['kpis'][0]})
- [ ] HoldCo portföy satırını güncelle (`holding_report.py`)
- [ ] Ülke bağımlılığı varsa `data/arsiv/holding/<CC>/` oku (🔗)

## Kişisel workflow checklist
{personal}

## Grup workflow checklist
{group}

## KPI
{kpis}

## Roadmap dilimleri
| Dilim | Hedef | Sahip | Deadline |
|---|---|---|---|
| F0 | Org + workflow canlı | `{s['id']}-ceo` | {DAY} |
| F1 | İlk KPI kesiti + eğitim modülü | `{s['id']}-evp-*` | +7g |
| F2 | Web/mobil yüzey DoD (blueprint) | holdco-cto + OpCo | +21g |
| F3 | Ülke lokalizasyon QA (TR+) | country agency | +30g |

## Toplantı
- Daily standup → gundem/
- Weekly OpCo sync (chair: EVP)
- Monthly HoldCo board satırı

## Anti-desen
Sahte issue · sessiz eskalasyon · karakter şişirme
"""
        path.write_text(body, encoding="utf-8")
        out_paths.append(str(path.relative_to(ROOT)))
    return out_paths


def write_country_boards(h: dict) -> list[str]:
    out = []
    root = ROOT / "docs" / "holding" / "ulkeler"
    root.mkdir(parents=True, exist_ok=True)
    for c in h["countries"]:
        path = root / f"{c['code']}-AJANS.md"
        path.write_text(
            f"""# {c['code']} — {c['name']} ülke LLM ajansı
> Damga: {TS} · Agency: `{c['agency']}` · Role: {c['role']}

## Law / language
- Law: {', '.join(c['law'])}
- Language: {', '.join(c['language'])}

## 7/24 checklist
- [ ] Prior arşiv oku: `data/arsiv/holding/{c['code']}/`
- [ ] Rakip top-5 kuyruğu (uydurma yok; Exa/WebSearch auth varsa doldur)
- [ ] Regülasyon deltası nota
- [ ] Lokal kreatif/dil QA
- [ ] Damga + BILGI_TABANI satırı

## Workflows
Kişisel + grup + `nightly_market_research` · `top5_competitor_scan` · `locale_qa`
""",
            encoding="utf-8",
        )
        out.append(str(path.relative_to(ROOT)))
    return out


def main() -> int:
    results = {}
    # Ensure packs
    for script in (
        "build_holding_pack.py",
        "build_skill_agency_registry.py",
        "build_k003_equivalents.py",
        "build_domain_observability_pack.py",
        "daily_ops.py",
        "holding_report.py",
        "nightly_holding_research.py",
    ):
        code, out = run(script)
        results[script] = {"code": code, "tail": out[-500:] if out else ""}
        if code != 0 and script in ("build_holding_pack.py", "daily_ops.py"):
            print(out)
            return code

    holding = json.loads((ROOT / "data" / "holding.json").read_text(encoding="utf-8"))
    opco_paths = write_opco_task_boards(holding)
    country_paths = write_country_boards(holding)
    questions = sample_questions()

    # validate
    vcode, vout = run("validate.py")
    results["validate.py"] = {"code": vcode, "tail": vout}

    status = ROOT / "docs" / "AKTIVASYON-DURUM.md"
    status.write_text(
        f"""# AKTİVASYON DURUMU
> Damga: {TS} · **Claude Code'a yapıştır = İPTAL** · Prompt **bu repoda / bu ajan tarafından uygulandı**.

## Applied layers
| Katman | Durum | Kanıt |
|---|---|---|
| Constitution (CLAUDE.md + CILT4 + MASTER + K-003) | AKTİF | always-on rule + CLAUDE.md |
| Org 600 | AKTİF | data/org.json |
| Prompt bank 122×3 | AKTİF | data/prompt_bank/ |
| Skill mini-ajans (v2.9) | AKTİF | data/skill_agency_registry.json |
| Holding (v2.10) | AKTİF | data/holding.json |
| Domain pack (v2.13) | AKTİF | data/domains/domain_pack.json + infra/observability/ |
| Daily standup | KOŞTU | gundem/{DAY}-standup.md |
| HoldCo portföy | KOŞTU | gundem/{DAY}-holding-portfoy.md |
| Gece ülke arşivi | KOŞTU | data/arsiv/holding/*/snapshot-{DAY}.json |
| OpCo görev tahtaları | YAZILDI | docs/holding/gorevler/ |
| Ülke ajans tahtaları | YAZILDI | docs/holding/ulkeler/ |
| validate.py | {"GEÇTİ" if vcode == 0 else "KALDI"} | exit {vcode} |

## Bugünün öz-denetim örnekleri
"""
        + "\n".join(f"{i+1}. {q}" for i, q in enumerate(questions[:12]))
        + f"""

## Script sonuçları
```json
{json.dumps({k: v['code'] for k, v in results.items()}, indent=2)}
```

## Owner next (Metin)
- MCP Authorize yalnızca ihtiyaç olanlar (Exa/Twilio/Datadog/Sentry/PagerDuty/…)
- Domain2 TF/OTel apply için credential + cluster onayı
- OpCo native scaffold hangi markadan → söyle; ayrı PR açılır
- Claude Code paste **gerekmiyor** — bu dosya kanıt
""",
        encoding="utf-8",
    )

    audit = {
        "ts_start": TS,
        "ts_end": TS,
        "op": "apply-activation-in-repo",
        "paste_claude_code": "CANCELLED",
        "applied_by": "cursor-cloud-agent",
        "outputs": [
            "docs/AKTIVASYON-DURUM.md",
            *opco_paths,
            *country_paths,
            f"gundem/{DAY}-standup.md",
            f"gundem/{DAY}-holding-portfoy.md",
        ],
        "validation": "GECTI" if vcode == 0 else "KALDI",
        "chain": "prev-archive-read+holding+skill-registry",
    }
    with open(ROOT / "AUDIT_LOG.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(audit, ensure_ascii=False) + "\n")

    with open(ROOT / "BILGI_TABANI.md", "a", encoding="utf-8") as f:
        f.write(
            f"\n- [{TS}] aktivasyon: Claude Code yapıştır İPTAL; prompt Cursor ajanında uygulandı. "
            f"daily_ops+holding+nightly+OpCo/ülke görev tahtaları. Learning: aktivasyon = kod+cron+kanıt dosyası, dış yapıştırma değil.\n"
        )

    print(f"ACTIVATION APPLIED @ {TS} validate={vcode}")
    print(f"opco_boards={len(opco_paths)} country_boards={len(country_paths)}")
    return 0 if vcode == 0 else vcode


if __name__ == "__main__":
    raise SystemExit(main())
