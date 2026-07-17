#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SEGMENT-600 / PROJECTS — Projects v2 panosuna 600 draft kart ekler.
🚩 ÖN KOŞUL: Actions'ın GITHUB_TOKEN'ı Projects v2'ye ERİŞEMEZ.
Classic PAT (scope: project) veya fine-grained token (Projects: Read+write)
PROJECTS_TOKEN secret'ı olarak eklenmelİ. env: START, COUNT."""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOKEN = os.environ.get("PROJECTS_TOKEN", "").strip()
if not TOKEN:
    raise SystemExit("PROJECTS_TOKEN secret'ı yok — Settings→Secrets→Actions'a ekle (scope: project).")
OWNER = os.environ.get("GITHUB_REPOSITORY", "metinduraktr-44/x").split("/")[0]
START = int(os.environ.get("START", "0"))
COUNT = int(os.environ.get("COUNT", "600"))
TITLE = "AdOps Ajans — 600 Rol Panosu"

def gql(query, variables=None):
    body = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request("https://api.github.com/graphql", data=body,
        headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        out = json.loads(r.read())
    if out.get("errors"):
        raise SystemExit(f"GraphQL hata: {out['errors']}")
    return out["data"]

owner_id = gql('query($l:String!){user(login:$l){id}}', {"l": OWNER})["user"]["id"]

# Mevcut panoyu bul ya da oluştur
projs = gql('query($l:String!){user(login:$l){projectsV2(first:20){nodes{id title}}}}',
            {"l": OWNER})["user"]["projectsV2"]["nodes"]
proj = next((p for p in projs if p["title"] == TITLE), None)
if not proj:
    proj = gql('mutation($o:ID!,$t:String!){createProjectV2(input:{ownerId:$o,title:$t}){projectV2{id title}}}',
               {"o": owner_id, "t": TITLE})["createProjectV2"]["projectV2"]
    print("pano olusturuldu:", TITLE)
pid = proj["id"]

# Mevcut kart başlıkları (idempotency)
existing, cursor = set(), None
while True:
    d = gql('query($p:ID!,$c:String){node(id:$p){... on ProjectV2{items(first:100,after:$c){nodes{content{... on DraftIssue{title}}} pageInfo{hasNextPage endCursor}}}}}',
            {"p": pid, "c": cursor})["node"]["items"]
    for it in d["nodes"]:
        if it["content"] and it["content"].get("title"):
            existing.add(it["content"]["title"])
    if not d["pageInfo"]["hasNextPage"]:
        break
    cursor = d["pageInfo"]["endCursor"]
print(f"mevcut kart: {len(existing)}")

org = json.load(open(os.path.join(ROOT, "data", "org.json"), encoding="utf-8"))
roster = [("C-LEVEL", "yonetim", c["slug"], c["reports_to"]) for c in org["c_level"]]
for dd in org["departments"]:
    roster += [(r["tier"], dd["code"], r["slug"], r["reports_to"]) for r in dd["roles"]]

created = 0
for tier, code, slug, boss in roster[START:START + COUNT]:
    t = f"[{code.upper()}·{tier}] {slug}"
    if t in existing:
        continue
    gql('mutation($p:ID!,$t:String!,$b:String!){addProjectV2DraftIssue(input:{projectId:$p,title:$t,body:$b}){projectItem{id}}}',
        {"p": pid, "t": t, "b": f"Raporlar: {boss} · Kart: components/agents/agency/"})
    created += 1
    time.sleep(0.8)
    if created % 50 == 0:
        print(f"{created} kart...")
print(f"BITTI: {created} yeni kart (pano: {TITLE})")
