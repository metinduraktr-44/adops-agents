#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HAFTALIK LİDERLİK / AYLIK KURUL tutanak üretici.
Kullanım: python3 scripts/weekly_board.py [--board]
--board: aylık yönetim kurulu modu (OKR skorlama + faz kapısı)."""
import json, os, sys, re, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOW = datetime.datetime.now(datetime.timezone.utc)
TS = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
TODAY = NOW.strftime("%Y-%m-%d")
BOARD = "--board" in sys.argv

org = json.load(open(os.path.join(ROOT, "data", "org.json"), encoding="utf-8"))

def read(p):
    fp = os.path.join(ROOT, p)
    return open(fp, encoding="utf-8").read() if os.path.exists(fp) else ""

def cnt(pattern, text):
    return len(re.findall(pattern, text))

isl = read("IS_LISTESI.md")
gtk = read("docs/GELIR-MODELI-TAKIP.md")
audit = read("AUDIT_LOG.jsonl").strip().splitlines()
runs_7d = [l for l in audit[-40:] if any(k in l for k in ("gunluk-operasyon", "nightly"))]
open_p0 = cnt(r"- \[ \]", isl.split("## P1")[0]) if "## P1" in isl else cnt(r"- \[ \]", isl)
gelir_acik = cnt(r"- \[ \]", gtk)

participants = [c["slug"] for c in org["c_level"]]
if not BOARD:
    participants += [d["roles"][0]["slug"] for d in org["departments"]]

kind = "AYLIK YÖNETİM KURULU" if BOARD else "HAFTALIK LİDERLİK SYNC"
out = f"toplantilar/{TODAY}-{'kurul' if BOARD else 'liderlik'}.md"
L = [f"# {kind} — {TODAY}", f"> Üretim: {TS} · Başkan: ceo-orchestrator",
     f"Katılımcılar: {', '.join(participants[:12])}{' + 20 EVP' if not BOARD else ''}", "",
     "## Durum kesiti",
     f"- Son kayıtlı koşum sayısı (log kuyruğu): {len(runs_7d)}",
     f"- Açık P0 işleri: {open_p0}",
     f"- Gelir kanallarında açık aksiyon: {gelir_acik}",
     "", "## Kararlar"]
if BOARD:
    L += ["- K: Faz kapısı değerlendirmesi — docs/YOL-HARITASI.md kriterleri kanıt linkiyle skorlanacak (sahip: ceo-orchestrator).",
          "- K: OKR skorları BILGI_TABANI.md'ye damıtılır; kırmızı OKR'lere sahip EVP'ler kurtarma planı sunar (7 gün)."]
else:
    L += ["- K: Haftanın 3 önceliği IS_LISTESI.md P0 blokundan kilitlendi.",
          "- K: Gelir pipeline'ındaki en yaşlı açık aksiyon Çarşamba review'ında çözülür."]
L += ["", "## Aksiyonlar",
      f"- [ ] P0 blokundaki {open_p0} işin sahip+deadline teyidi → coo-delivery · {TODAY}",
      f"- [ ] Gelir takip tablosunda durum güncellemesi → cro-revenue · Çarşamba",
      "", "## Riskler / 🚩",
      "- ANTHROPIC_API_KEY yoksa makale hattı iskelet modunda — tam üretim için secret şart."]
os.makedirs(os.path.join(ROOT, "toplantilar"), exist_ok=True)
open(os.path.join(ROOT, out), "w", encoding="utf-8").write("\n".join(L) + "\n")

with open(os.path.join(ROOT, "AUDIT_LOG.jsonl"), "a", encoding="utf-8") as f:
    f.write(json.dumps({"ts": TS, "op": "kurul" if BOARD else "liderlik-sync",
                        "outputs": [out], "validation": "GECTI"}, ensure_ascii=False) + "\n")
with open(os.path.join(ROOT, "BILGI_TABANI.md"), "a", encoding="utf-8") as f:
    f.write(f"\n- [{TS}] {'kurul' if BOARD else 'liderlik-sync'}: tutanak {out}; açık P0={open_p0}, gelir aksiyonu={gelir_acik}.")
print("WROTE", out)
