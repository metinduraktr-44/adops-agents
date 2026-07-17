#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SEGMENT-600 / WIKI — org.json'dan 620+ wiki sayfası üretir (wiki-out/).
Yayın: seed-600 workflow'u hedef=wiki ile .wiki.git'e push eder.
ÖN KOŞUL: Wiki'de ilk sayfa (Home) bir kez UI'dan oluşturulmuş olmalı."""
import json, os, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "wiki-out")
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
REPO = os.environ.get("GITHUB_REPOSITORY", "metinduraktr-44/adops-agents")
org = json.load(open(os.path.join(ROOT, "data", "org.json"), encoding="utf-8"))
os.makedirs(OUT, exist_ok=True)
n = 0

def W(name, content):
    global n
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(content)
    n += 1

def role_page(slug, title, tier, reports_to, dept_slug, dept_name, kpis):
    kpi_md = "\n".join(f"- {k}" for k in kpis)
    return (f"# {title}\n\n"
            f"| Alan | Değer |\n|---|---|\n"
            f"| Slug | `{slug}` |\n| Kademe | {tier} |\n| Departman | {dept_name} |\n"
            f"| Raporlar | [[{reports_to}]] |\n"
            f"| Rol kartı | [components/agents/agency/{dept_slug}/{slug}.md]"
            f"(https://github.com/{REPO}/blob/main/components/agents/agency/{dept_slug}/{slug}.md) |\n\n"
            f"## Departman KPI seti\n{kpi_md}\n\n"
            f"_Üretim: {NOW} · Kaynak: data/org.json_\n")

# C-level
clevel_kpis = ["Ajans OKR'ları", "Döngü yeşilliği", "Gelir kanalı ilerlemesi"]
for c in org["c_level"]:
    W(f"{c['slug']}.md", role_page(c["slug"], c["title"], "C-LEVEL", c["reports_to"],
                                   "c-level", "Yönetim", clevel_kpis))

# Departman + roller
dept_links = []
for d in org["departments"]:
    rows = ["| Rol | Kademe | Raporlar |", "|---|---|---|"]
    for r in d["roles"]:
        W(f"{r['slug']}.md", role_page(r["slug"], r["title"], r["tier"], r["reports_to"],
                                       d["slug"], d["name_en"], d["kpis"]))
        rows.append(f"| [[{r['slug']}]] | {r['tier']} | [[{r['reports_to']}]] |")
    page = (f"# {d['name_en']} ({d['code'].upper()}) — {d['name_tr']}\n\n"
            f"Sponsor: [[{d['sponsor']}]] · Kadro: {d['headcount']} · "
            f"Birimler: {', '.join(d['units'])}\n\n" + "\n".join(rows) + f"\n\n_Üretim: {NOW}_\n")
    W(f"DEPT-{d['code'].upper()}.md", page)
    dept_links.append(f"- [[DEPT-{d['code'].upper()}]] — {d['name_en']} ({d['headcount']})")

# Home + Sidebar
W("Home.md",
  f"# AdOps AI Agency Wiki\n\n**{org['total']} ajan** · 6 kademe · 20 departman · 7/24 cron ritmi\n\n"
  f"## Yönetim (C-Level)\n" +
  "\n".join(f"- [[{c['slug']}]] — {c['title']}" for c in org["c_level"]) +
  "\n\n## Departmanlar\n" + "\n".join(dept_links) +
  f"\n\n## Referanslar\n- [Anayasa (924 başlık)](https://github.com/{REPO}/blob/main/docs/MASTER-PROMPT-AJANS.md)\n"
  f"- [Yol haritası](https://github.com/{REPO}/blob/main/docs/YOL-HARITASI.md)\n"
  f"- [Gelir takibi](https://github.com/{REPO}/blob/main/docs/GELIR-MODELI-TAKIP.md)\n\n_Üretim: {NOW}_\n")
W("_Sidebar.md", "# Ajans\n- [[Home]]\n" + "\n".join(dept_links[:20]))
W("_Footer.md", f"AdOps AI Agency · {org['total']} ajan · üretim {NOW}")
print(f"WIKI PAGES: {n}")
assert n >= 600, n
