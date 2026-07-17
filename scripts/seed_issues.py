#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SEGMENT-600 / ISSUES — 600 rol kaydı issue'su açar (idempotent, throttle'lı).
Actions içinde GITHUB_TOKEN ile çalışır. env: START (vars. 0), COUNT (vars. 600)."""
import json, os, time, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOKEN = os.environ["GITHUB_TOKEN"]
REPO = os.environ.get("GITHUB_REPOSITORY", "metinduraktr-44/adops-agents")
START = int(os.environ.get("START", "0"))
COUNT = int(os.environ.get("COUNT", "600"))
API = f"https://api.github.com/repos/{REPO}"

def call(method, url, payload=None, ok=(200, 201)):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.status, json.loads(r.read() or "{}")
        except urllib.error.HTTPError as e:
            if e.code in (403, 429):  # secondary rate limit
                wait = int(e.headers.get("Retry-After", "60"))
                print(f"rate-limit, {wait}s bekleniyor (deneme {attempt+1})")
                time.sleep(wait)
                continue
            return e.code, json.loads(e.read() or "{}")
    raise SystemExit("rate-limit asilamadi")

org = json.load(open(os.path.join(ROOT, "data", "org.json"), encoding="utf-8"))
roster = [("yonetim", "C-LEVEL", c["slug"], c["title"], c["reports_to"], "c-level")
          for c in org["c_level"]]
for d in org["departments"]:
    for r in d["roles"]:
        roster.append((d["code"], r["tier"], r["slug"], r["title"], r["reports_to"], d["slug"]))
print(f"roster: {len(roster)} rol")

# 1) Etiketler
labels = [("rol-kaydi", "0e8a16"), ("c-level", "5319e7"), ("evp", "1d76db"),
          ("director", "0052cc"), ("lead", "006b75"), ("specialist", "fbca04"),
          ("analyst", "d4c5f9")] + [(d["code"], "bfd4f2") for d in org["departments"]] + \
         [("yonetim", "5319e7")]
for name, color in labels:
    call("POST", f"{API}/labels", {"name": name, "color": color}, ok=(201, 422))
print("etiketler hazir")

# 2) Mevcut issue başlıkları (rol-kaydi etiketiyle)
existing = set()
page = 1
while True:
    st, data = call("GET", f"{API}/issues?state=all&labels=rol-kaydi&per_page=100&page={page}")
    if st != 200 or not data:
        break
    existing.update(i["title"] for i in data)
    if len(data) < 100:
        break
    page += 1
print(f"mevcut: {len(existing)}")

# 3) Oluştur
created = skipped = 0
for dept_code, tier, slug, title, reports_to, dept_slug in roster[START:START + COUNT]:
    t = f"[ROL] {slug} — aktivasyon"
    if t in existing:
        skipped += 1
        continue
    body = (f"**Rol:** {title}\n**Kademe:** {tier} · **Departman:** {dept_code.upper()}\n"
            f"**Raporlar:** `{reports_to}`\n"
            f"**Kart:** `components/agents/agency/{dept_slug}/{slug}.md`\n\n"
            f"### Aktivasyon kontrol listesi\n"
            f"- [ ] Rol kartı okundu, KPI seti onaylandı\n"
            f"- [ ] İlk standup satırı gundem/'e düştü\n"
            f"- [ ] Playbook/bileşen bağlantısı IS_LISTESI kuyruğuna eklendi\n")
    st, _ = call("POST", f"{API}/issues",
                 {"title": t, "body": body,
                  "labels": ["rol-kaydi", dept_code, tier.lower().replace("c-level", "c-level")]})
    if st == 201:
        created += 1
    else:
        print(f"HATA {st}: {slug}")
    time.sleep(1.0)
    if created % 50 == 0 and created:
        print(f"{created} olusturuldu...")
print(f"BITTI: olusturulan={created} atlanan={skipped} aralik={START}..{START+COUNT}")
