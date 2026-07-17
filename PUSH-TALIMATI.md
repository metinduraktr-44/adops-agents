# PUSH TALİMATI

## v2.1 AJANS + SEGMENT-600 GÜNCELLEMESİ (mevcut repoya push — 1 dakika)
Cowork'ün ürettiği `adops-agents-v2.1.zip` içeriğini mevcut klonunun üzerine aç, sonra:
```bash
cd adops-agents
git add -A
git commit -m "v2.1: 600-ajan AI Agency + segment-600 motoru + gelir araştırması"
git push origin main
```
Push sonrası sıra (detay: docs/SEGMENT-600-PLANI.md):
1. Actions → `gunluk-operasyon` → Run workflow (yeşili gör).
2. Actions → `seed-600` → hedef=issues (600 rol issue'su, ~15 dk).
3. Actions → `seed-600` → hedef=prs, start=0/150/300/450 × adet=150 (4 koşum → 600 PR + 600 Actions koşumu).
4. Wiki sekmesinde Home'u BİR KEZ elle oluştur → seed-600 → hedef=wiki (633 sayfa).
5. Actions → `security-audit` → Run (Security sekmesine 626 denetim kaydı).
6. Opsiyonel: `PROJECTS_TOKEN` secret (PAT, scope: project) → seed-600 → hedef=projeler (600 kart).
`ANTHROPIC_API_KEY` secret'ı ekliysen makale hattı tam üretime geçer; değilse iskelet modda döner (döngü kırılmaz).

---

# Bu repoyu yeni bir GitHub reposuna gönder (2 dakika)

## Yol A — GitHub CLI (en kolay)
```bash
# 1) gh yükle+giriş (bir kez):  https://cli.github.com  ->  gh auth login
cd adops-agents
gh repo create adops-agents --public --source=. --remote=origin --push
```

## Yol B — Düz git (arayüzden boş repo açtıysan)
```bash
cd adops-agents
git remote add origin https://github.com/<KULLANICI-ADIN>/adops-agents.git
git branch -M main
git push -u origin main
```

## Push sonrası (opsiyonel ama önerilir)
- **Nightly loop için:** Repo -> Settings -> Secrets and variables -> Actions ->
  `ANTHROPIC_API_KEY` ekle. (⚠️ Ücretli API kredisi harcar. Eklemezsen gece görevi
  yine çalışır; sadece üretim adımını atlar, damga+doğrulama yapar.)
- **Actions'ı aç:** Repo -> Actions -> Enable. `validate-components` her PR'da,
  `nightly-improve` her gece 03:00 (İstanbul) çalışır. Elle test: Actions ->
  nightly-improve -> Run workflow.

## Adı değiştirmek istersen (AdOps Agents -> kendi markan)
```bash
cd adops-agents
grep -rl "adops-agents\|AdOps Agents" . | xargs sed -i 's/AdOps Agents/YENI_AD/g; s/adops-agents/yeni-slug/g'
```
