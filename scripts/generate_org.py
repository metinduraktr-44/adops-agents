#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AI AGENCY ORG GENERATOR — adops-agents v2
Üretir: 600 ajan (components/agents/agency/), data/org.json,
docs/MASTER-PROMPT-AJANS.md (900+ başlık), ORG-SEMASI, IS_LISTESI,
TOPLANTI-PROTOKOLU, GELIR-MODELI-TAKIP, YOL-HARITASI.
Tek doğruluk kaynağı bu dosyadır; yeniden koşum idempotenttir.
"""
import json, os, re, hashlib, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
TODAY = NOW[:10]
SHIFTS = ["00–08 UTC", "08–16 UTC", "16–24 UTC"]

# Soru bankası (varsa) — kart başına departman+kademe alt-seti gömülür
_SB_PATH = os.path.join(ROOT, "data", "soru_bankasi.json")
SORU_BANKASI = json.load(open(_SB_PATH, encoding="utf-8")) if os.path.exists(_SB_PATH) else {"by_dept": {}, "by_tier": {}}
# Rol modelleri (varsa) — disiplin başına dünya top isimleri
_RM_PATH = os.path.join(ROOT, "data", "rol_modelleri.json")
ROL_MODELLERI = json.load(open(_RM_PATH, encoding="utf-8")) if os.path.exists(_RM_PATH) else {}
# Bilinen rol-modellerin 1 pratik ilkesi (yalnız emin olunanlar; uydurma yok)
MODEL_ILKELERI = {
 "Les Binet": "60/40 marka/aktivasyon bütçe kuralı",
 "Byron Sharp": "penetrasyon + zihinsel/fiziksel erişilebilirlik > sadakat",
 "Mark Ritson": "önce teşhis, sonra strateji, sonra taktik",
 "Rory Sutherland": "psikolojik moonshot — algı mühendisliği ucuz kaldıraçtır",
 "Avinash Kaushik": "See-Think-Do-Care: niyet aşamasına göre ölç ve mesajla",
 "Peep Laja": "veri, görüşü yener; her varsayımı test et",
 "Ronny Kohavi": "güvenilir kontrollü deney — önce OEC'i tanımla",
 "Eric Seufert": "LTV-önce büyüme; ATT sonrası olasılıksal ölçüm",
 "Rand Fishkin": "sıfır-tık dünyada değeri kanalın kendisinde ver",
 "Simo Ahava": "ölçüm mimarisi önce — server-side + veri kalitesi",
 "Frederick Vallaeys": "otomasyona rağmen strateji insanda kalır (katmanlı kontrol)",
 "Blair Enns": "pitch'siz kazan — uzmanlık pozisyonuyla fiyat gücü",
 "Nadia Eghbal": "açık kaynak bakım işidir; finansman altyapı sorunudur",
 "Simon Willison": "prompt injection'a karşı tasarla; araçları küçük/denetlenebilir tut",
 "Hamel Husain": "önce eval yaz — ölçemediğin kaliteyi iyileştiremezsin",
 "Chip Huyen": "üretim ML = sistem tasarımı, tek model değil",
 "Paul W. Farris": "her pazarlama kararını bir metriğe bağla",
 "Peter Fader": "müşteri-merkezlilik: değeri CLV üzerinden yönet",
 "Daniel J. Solove": "gizlilik = zararların taksonomisi + bağlamsal bütünlük",
 "Ari Paparo": "adtech'i şeffaf açıkla — tedarik zincirini anla",
 "Chris Kane": "supply-path optimizasyonu: aracı katmanı buda",
 "Orlando Wood": "sağ-beyin yaratıcılık uzun-vade etkiyi taşır",
}

# Departman-özel GERÇEK öğrenme kaynakları (resmi changelog/eğitim/beta/blog URL'leri)
DEPT_SOURCES = {
 "prg": [("DV360 Yardım/Changelog", "https://support.google.com/displayvideo/answer/9059050"),
         ("The Trade Desk Haber", "https://www.thetradedesk.com/us/news"),
         ("IAB Tech Lab", "https://iabtechlab.com"), ("Skillshop (DV360)", "https://skillshop.exceedlms.com")],
 "sea": [("Google Ads Yardım", "https://support.google.com/google-ads"),
         ("Google Ads Blog", "https://blog.google/products/ads-commerce/"),
         ("Search Engine Land", "https://searchengineland.com"), ("Skillshop", "https://skillshop.exceedlms.com")],
 "soc": [("Meta for Business Haber", "https://www.facebook.com/business/news"),
         ("Meta Blueprint", "https://www.facebook.com/business/learn"),
         ("TikTok for Business", "https://ads.tiktok.com/business/en"),
         ("LinkedIn Marketing Blog", "https://www.linkedin.com/business/marketing/blog")],
 "mob": [("Apple Search Ads", "https://searchads.apple.com"), ("AppsFlyer Blog", "https://www.appsflyer.com/blog"),
         ("Adjust Blog", "https://www.adjust.com/blog"),
         ("Google App Kampanyaları", "https://support.google.com/google-ads/answer/6247380")],
 "ret": [("Amazon Ads Kütüphane", "https://advertising.amazon.com/library"),
         ("Criteo Blog", "https://www.criteo.com/blog"),
         ("Think with Google Retail", "https://www.thinkwithgoogle.com")],
 "seo": [("Google Search Central", "https://developers.google.com/search"),
         ("Search Central Blog", "https://developers.google.com/search/blog"),
         ("Ahrefs Blog", "https://ahrefs.com/blog"), ("Moz Blog", "https://moz.com/blog")],
 "cro": [("CXL Blog", "https://cxl.com/blog"), ("Baymard Institute", "https://baymard.com"),
         ("GoodUI", "https://goodui.org")],
 "ana": [("GA4 Changelog", "https://support.google.com/analytics/answer/9164320"),
         ("Simo Ahava Blog", "https://www.simoahava.com"),
         ("Google Analytics Blog", "https://blog.google/products/marketingplatform/analytics/")],
 "dsc": [("arXiv cs.LG", "https://arxiv.org/list/cs.LG/recent"),
         ("Google Research Blog", "https://research.google/blog/"),
         ("Papers with Code", "https://paperswithcode.com")],
 "ops": [("Campaign Manager 360 Yardım", "https://support.google.com/campaignmanager"),
         ("Google Tag Manager", "https://support.google.com/tagmanager"), ("IAB", "https://www.iab.com")],
 "cre": [("TikTok Creative Center", "https://ads.tiktok.com/business/creativecenter"),
         ("Meta Creative Hub", "https://www.facebook.com/business/tools/creative-hub"),
         ("Think with Google Creative", "https://www.thinkwithgoogle.com")],
 "str": [("Think with Google", "https://www.thinkwithgoogle.com"),
         ("IAB Insights", "https://www.iab.com/insights/"), ("WARC", "https://www.warc.com")],
 "cls": [("HubSpot Blog", "https://blog.hubspot.com"),
         ("Google Skillshop", "https://skillshop.exceedlms.com")],
 "nbd": [("HubSpot Sales Blog", "https://blog.hubspot.com/sales"),
         ("Evil Martians OSS", "https://evilmartians.com/opensource")],
 "prt": [("Neon OSS Program", "https://neon.com/programs/open-source"),
         ("Supermetrics Partners", "https://supermetrics.com/partners"),
         ("Railway OSS Kickback", "https://railway.com/open-source-kickback"),
         ("GitHub Sponsors Docs", "https://docs.github.com/en/sponsors")],
 "prd": [("Anthropic Docs", "https://docs.claude.com"),
         ("Claude Code Docs", "https://code.claude.com/docs"),
         ("awesome-claude-code", "https://github.com/hesreallyhim/awesome-claude-code")],
 "fin": [("Anthropic Pricing", "https://www.anthropic.com/pricing"),
         ("GitHub Actions Faturalama", "https://docs.github.com/en/billing")],
 "leg": [("KVKK", "https://www.kvkk.gov.tr"), ("GDPR.eu", "https://gdpr.eu"),
         ("IAB TCF", "https://iabeurope.eu/transparency-consent-framework/")],
 "tal": [("Anthropic Prompting Docs", "https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview"),
         ("Claude Cookbook", "https://github.com/anthropics/anthropic-cookbook")],
 "inf": [("GitHub Changelog", "https://github.blog/changelog/"),
         ("GitHub Actions Docs", "https://docs.github.com/en/actions"),
         ("MCP Spec", "https://modelcontextprotocol.io"),
         ("Anthropic Docs", "https://docs.claude.com")],
 "yonetim": [("Anthropic Docs", "https://docs.claude.com"),
             ("Think with Google", "https://www.thinkwithgoogle.com"),
             ("GitHub Changelog", "https://github.blog/changelog/")],
}
LEARN_CADENCE = {
 "C-LEVEL": "Günlük 1 sektör/ekosistem kaynağı · haftalık 1 POV · aylık 1 stratejik makale.",
 "EVP": "Günlük 1 platform changelog · haftalık 1 departman öğrenim notu · aylık 1 sertifika modülü.",
 "DIRECTOR": "Günlük 1 kaynak · haftalık 1 birim öğrenimi · aylık 1 beta test raporu.",
 "LEAD": "Günlük 1 kaynak · haftalık 1 iş-akışı notu · 2 haftada 1 makale taslağı.",
 "SPECIALIST": "Günlük 1 kaynak okuma + 1 satır not · haftalık 1 iyileştirme.",
 "ANALYST": "Günlük 1 kaynak · haftalık 1 veri/metodoloji notu.",
}

# ----------------------------------------------------------------------------
# C-LEVEL (10)
# ----------------------------------------------------------------------------
C_LEVEL = [
 ("ceo-orchestrator", "CEO — Chief Executive Orchestrator",
  "Owns the whole agency: strategy, portfolio, final arbitration. Reports to Metin Durak (owner).",
  ["Set quarterly OKRs for all 20 departments", "Arbitrate cross-department conflicts",
   "Approve roadmap phase gates", "Own the monthly board meeting agenda"],
  ["Agency OKR attainment ≥ 80%", "All 5 revenue channels active by roadmap dates",
   "Nightly + daily loops green ≥ 99%", "Zero unresolved escalations > 72h"]),
 ("coo-delivery", "COO — Chief Operating Officer",
  "Runs delivery: programmatic, search, social, mobile UA, retail media, ad ops.",
  ["Own the 7/24 shift roster and on-call rotation", "Enforce daily standup discipline",
   "Balance workload across delivery departments", "Own incident/escalation runbook"],
  ["Daily standup completion 7/7", "Escalation MTTR < 24h", "Shift coverage 100%",
   "Delivery dept KPI attainment ≥ 85%"]),
 ("cso-strategy", "CSO — Chief Strategy Officer",
  "Owns planning, audience strategy, talent/agent quality and the knowledge chain.",
  ["Own BILGI_TABANI.md growth quality (signal over length)", "Quarterly agency positioning review",
   "Approve new department/unit proposals", "Own agent (prompt) quality bar with talent-hr"],
  ["1+ distilled learning per day into knowledge base", "Positioning refresh 1/quarter",
   "Agent quality audit pass rate ≥ 95%"]),
 ("cmo-brand", "CMO — Chief Marketing Officer",
  "Owns the agency's own growth: content engine, SEO, creative, articles, community.",
  ["Own daily article/update pipeline (min 1/day)", "Own README/repo storefront quality",
   "Grow stars/watchers/forks as brand KPIs", "Own directory/marketplace listings (aitmpl etc.)"],
  ["≥ 1 article or substantive update per day", "Repo stars +20/month after launch",
   "Listed in ≥ 3 ecosystem directories"]),
 ("cto-platform", "CTO — Chief Technology Officer",
  "Owns repo infrastructure, CI/CD, validation layers, MCP configs, automation scripts.",
  ["Keep all GitHub Actions green", "Own validate.py + 6-layer validation evolution",
   "Own data/org.json schema and generator", "Security: forbidden-pattern & injection scans"],
  ["CI green rate ≥ 99%", "Validation coverage 100% of components", "0 dangerous patterns shipped"]),
 ("cfo-finance", "CFO — Chief Financial Officer",
  "Owns money: API cost budget, revenue tracking, margin on premium pack, sponsorship terms.",
  ["Track API spend vs. budget weekly", "Own GELIR-MODELI-TAKIP.md numbers",
   "Price premium plugin pack", "Approve any paid tool/integration"],
  ["API cost within monthly budget", "Revenue pipeline value updated weekly",
   "First revenue booked by roadmap F3"]),
 ("cdo-data", "CDO — Chief Data Officer",
  "Owns measurement: analytics, attribution, MMM, incrementality, data science standards.",
  ["Set measurement standards for all delivery work", "Own GA4/attribution component quality",
   "Approve any KPI definition change", "Own experiment/holdout methodology"],
  ["100% of playbooks carry KPI definitions", "Measurement components pass audit ≥ 95%"]),
 ("cpo-product", "CPO — Chief Product Officer",
  "Owns the product: component pack, premium pack, CRO/experience department, versioning.",
  ["Own plugin.json + VERSIONS.md roadmap", "Define premium vs. free component split",
   "Own release notes and semver discipline", "Prioritize component backlog"],
  ["Release cadence ≥ 2/month", "Premium pack v1 shipped by roadmap F4",
   "Breaking changes documented 100%"]),
 ("cro-revenue", "CRO — Chief Revenue Officer",
  "Owns all 5 revenue channels: sponsorships, placements, referrals, premium, inbound agency funnel.",
  ["Run weekly revenue pipeline review", "Own outreach lists (sponsors, vendors)",
   "Own inbound lead capture path from README to contact", "Negotiate referral terms"],
  ["Pipeline: 10 qualified sponsor/vendor conversations by F3", "First referral agreement by F3",
   "First inbound agency lead by F5"]),
 ("cco-compliance", "CCO — Chief Compliance Officer",
  "Owns legal & compliance: licensing (MIT), privacy (KVKK/GDPR), ad policy, 5 security rules.",
  ["Enforce the 5 security rules on every component", "License hygiene on any ingested source",
   "Ad-policy sanity checks in playbooks", "Own AUDIT_LOG.jsonl integrity"],
  ["0 license violations", "100% components pass security screen", "Audit chain unbroken"]),
]
CEO_SLUG = "ceo-orchestrator"

# ----------------------------------------------------------------------------
# DEPARTMENTS (20) — code, slug, EN name, TR name, sponsor, headcount, units, topics, kpis, tools
# ----------------------------------------------------------------------------
D = []
def dept(code, slug, en, tr, sponsor, n, units, topics, kpis, tools="Read, Bash, WebSearch"):
    D.append(dict(code=code, slug=slug, en=en, tr=tr, sponsor=sponsor, n=n,
                  units=units, topics=topics, kpis=kpis, tools=tools))

dept("prg", "programmatic", "Programmatic Trading", "Programatik Satın Alma", "coo-delivery", 45,
 ["Open Auction & Curation", "PMP & Deals", "CTV / OTT", "DOOH & Audio", "Bid Algorithms"],
 ["dv360-activation", "ttd-activation", "xandr-activation", "pmp-deal-desk", "ctv-buying",
  "dooh-buying", "audio-buying", "curation-supply-path", "brand-safety-pretargeting",
  "bid-shading-analysis", "frequency-management", "deal-troubleshooting"],
 ["Viewability ≥ 70%", "Supply-path cost ≤ 15%", "PMP share of spend on target", "eCPM/CPA vs plan"]),
dept("sea", "paid-search", "Paid Search", "Ücretli Arama", "coo-delivery", 40,
 ["Google Ads Core", "SA360 & Automation", "PMax & Shopping", "Microsoft Ads"],
 ["query-mining", "pmax-structure", "shopping-feed-optimization", "sa360-bid-strategies",
  "rsa-ad-strength", "negative-keyword-hygiene", "landing-page-relevance", "brand-vs-generic-split",
  "budget-pacing", "auction-insights"],
 ["Impression share on brand ≥ 90%", "Wasted spend < 5%", "tCPA/tROAS attainment", "QS trend up"]),
dept("soc", "paid-social", "Paid Social", "Ücretli Sosyal", "coo-delivery", 45,
 ["Meta", "TikTok", "LinkedIn & X", "Snap & Pinterest", "Creative Testing"],
 ["meta-aso-structure", "advantage-plus-audit", "tiktok-spark-ads", "linkedin-abm",
  "creative-fatigue-detection", "hook-rate-analysis", "capi-signal-health", "audience-liquidity",
  "ugc-pipeline", "cbo-abo-strategy", "retargeting-ladders", "social-commerce"],
 ["Thumbstop/hook rate on target", "CAPI EMQ ≥ 8", "Creative refresh cadence met", "Blended CPA vs plan"]),
dept("mob", "mobile-ua", "Mobile UA & App Growth", "Mobil UA & Uygulama", "coo-delivery", 35,
 ["Apple Search Ads", "Google App Campaigns", "MMP (Adjust/AppsFlyer)", "Retargeting & CRM"],
 ["asa-keyword-strategy", "uac-asset-groups", "skan-4-strategy", "mmp-attribution-windows",
  "fraud-detection", "deeplink-qa", "aso-store-page", "reengagement-audiences", "ltv-cohorts"],
 ["SKAN CV coverage ≥ 85%", "Fraud rate < 3%", "D7 ROAS vs plan", "Organic uplift measured"]),
dept("ret", "retail-media", "Retail & Commerce Media", "Perakende Medyası", "coo-delivery", 30,
 ["Amazon Ads", "TR Marketplaces (Trendyol/Hepsiburada)", "Criteo & Onsite", "Offsite & DSP"],
 ["amazon-sp-sb-sd", "trendyol-ads", "hepsiburada-ads", "criteo-retail", "retail-sov-tracking",
  "content-pdp-optimization", "promo-calendar-sync", "retail-dsp-offsite"],
 ["ACOS/TACOS on target", "Share of voice on hero SKUs", "PDP conversion uplift", "Incremental ROAS"]),
dept("seo", "seo-content", "SEO & Content Engine", "SEO & İçerik Motoru", "cmo-brand", 30,
 ["Technical SEO", "Content Production", "Digital PR & Links", "Repo Storefront"],
 ["technical-crawl-audit", "keyword-clustering", "content-brief-engine", "internal-linking",
  "digital-pr-outreach", "serp-feature-capture", "readme-storefront", "daily-article-engine"],
 ["1+ article/day shipped", "Organic clicks trend up", "Core Web Vitals green", "Directory listings ≥ 3"],
 "Read, Write, WebSearch"),
dept("cro", "cro-experience", "CRO & Experience", "CRO & Deneyim", "cpo-product", 25,
 ["Experimentation", "Landing Systems", "UX Research"],
 ["ab-test-design", "landing-page-systems", "form-friction-audit", "heatmap-session-analysis",
  "offer-message-testing", "checkout-optimization", "mobile-speed-cro"],
 ["Test velocity ≥ 4/month", "Win rate documented", "LP conversion uplift", "Sample-size discipline 100%"]),
dept("ana", "analytics-measurement", "Analytics & Measurement", "Analitik & Ölçümleme", "cdo-data", 40,
 ["GA4 & Tagging", "Attribution", "MMM & Incrementality", "Clean Rooms & Privacy", "Dashboards"],
 ["ga4-audit", "server-side-tagging", "consent-mode-v2", "attribution-model-selection",
  "mmm-lite", "geo-holdout-design", "clean-room-queries", "looker-dashboard-standards",
  "data-quality-monitoring", "kpi-dictionary"],
 ["Tracking coverage ≥ 95%", "Attribution doc per client playbook", "Dashboard SLA met", "0 unowned KPIs"]),
dept("dsc", "data-science-ai", "Data Science & AI", "Veri Bilimi & AI", "cdo-data", 30,
 ["Forecasting & LTV", "Optimization Models", "AI Tooling & Agents"],
 ["ltv-prediction", "budget-allocation-models", "bid-landscape-modeling", "churn-propensity",
  "creative-scoring-models", "anomaly-detection", "agent-eval-harness", "prompt-optimization"],
 ["Forecast MAPE ≤ 15%", "1 model improvement/month", "Agent eval pass rate ≥ 95%"]),
dept("ops", "adops-trafficking", "Ad Ops & Trafficking", "Ad Ops & Trafficking", "coo-delivery", 35,
 ["CM360 Trafficking", "Tag Management", "QA & Verification", "Consent & Privacy Ops"],
 ["cm360-trafficking", "floodlight-architecture", "gtm-container-hygiene", "creative-specs-qa",
  "ias-doubleverify-setup", "consent-string-qa", "utm-governance", "campaign-launch-checklist"],
 ["Launch error rate < 1%", "Tag QA pass 100% pre-launch", "Discrepancy < 5%"]),
dept("cre", "creative-studio", "Creative Studio & DCO", "Kreatif Stüdyo & DCO", "cmo-brand", 35,
 ["Concept & Copy", "Video & Motion", "DCO & Feeds", "Ad Format Lab"],
 ["hook-concepting", "ad-copy-systems", "video-cutdown-matrix", "dco-feed-design",
  "format-spec-library", "localization-tr", "creative-naming-taxonomy", "asset-versioning"],
 ["Creative turnaround SLA", "Hook-rate lift per iteration", "100% assets spec-compliant"],
 "Read, Write, WebSearch"),
dept("str", "strategy-planning", "Strategy & Comms Planning", "Strateji & Planlama", "cso-strategy", 30,
 ["Audience & Insight", "Media Mix", "Playbooks & POVs"],
 ["audience-mapping", "channel-mix-modeling", "competitive-landscape", "pov-writing",
  "media-plan-templates", "benchmark-library", "quarterly-planning"],
 ["Every plan carries mix rationale", "POV per major platform change ≤ 7 days", "Benchmarks refreshed monthly"]),
dept("cls", "client-services", "Client Services", "Müşteri Hizmetleri", "cro-revenue", 30,
 ["Account Leadership", "Reporting Cadence", "Onboarding"],
 ["account-health-scoring", "weekly-report-narratives", "qbr-decks", "onboarding-checklists",
  "expectation-management", "escalation-comms", "renewal-playbooks"],
 ["Report SLA 100%", "Account health scored weekly", "Churn risk flagged ≥ 14 days early"]),
dept("nbd", "new-business", "New Business & Inbound Funnel", "Yeni İş & Inbound Hunisi", "cro-revenue", 25,
 ["Inbound Capture", "Pitch Factory", "Lead Scoring"],
 ["inbound-funnel-design", "pitch-deck-assembly", "case-study-engine", "lead-scoring-model",
  "discovery-call-briefs", "proposal-templates", "win-loss-analysis"],
 ["Inbound path live (README→contact) F2", "Pitch turnaround ≤ 48h", "First qualified lead by F5"]),
dept("prt", "partnerships-sponsorships", "Partnerships & Sponsorships", "Ortaklıklar & Sponsorluklar", "cro-revenue", 20,
 ["Infra Sponsors", "Referral Programs", "Ecosystem Relations"],
 ["sponsor-target-list", "sponsorship-pitch-kit", "referral-terms-tracking", "ecosystem-directory-relations",
  "co-marketing-plays", "partner-health-review"],
 ["10 sponsor conversations by F3", "2 referral agreements by F4", "3 directory listings by F2"]),
dept("prd", "product-premium", "Product & Premium Pack", "Ürün & Premium Paket", "cpo-product", 20,
 ["Premium Components", "Packaging & Licensing", "Docs & DX"],
 ["premium-component-specs", "licensing-model", "component-docs-standards", "installer-experience",
  "feedback-intake", "release-notes"],
 ["Premium pack v1 by F4", "Docs coverage 100%", "Install friction ≤ 2 steps"]),
dept("fin", "finance-billing", "Finance & Billing", "Finans & Faturalama", "cfo-finance", 15,
 ["Cost Control", "Revenue Ops"],
 ["api-cost-tracking", "sponsor-invoice-flows", "margin-models", "budget-variance-reports"],
 ["Weekly cost report shipped", "Revenue entries reconciled", "Variance explained 100%"]),
dept("leg", "legal-compliance", "Legal & Compliance", "Hukuk & Uyum", "cco-compliance", 15,
 ["Licensing", "Privacy (KVKK/GDPR)", "Ad Policy"],
 ["license-audit", "kvkk-gdpr-checklists", "ad-policy-screening", "tos-review", "security-rule-enforcement"],
 ["0 violations", "100% components screened", "Policy answers ≤ 24h"]),
dept("tal", "talent-hr", "Talent & Agent Quality", "Yetenek & Ajan Kalitesi", "cso-strategy", 15,
 ["Agent Lifecycle", "Quality Bar", "Training Loops"],
 ["agent-onboarding-standards", "prompt-review-rubric", "underperformer-rehab", "role-gap-analysis",
  "shift-roster-management"],
 ["Quality audit ≥ 95% pass", "Role gaps closed ≤ 14 days", "Roster coverage 100%"]),
dept("inf", "tech-infra", "Tech & Infrastructure", "Teknoloji & Altyapı", "cto-platform", 30,
 ["CI/CD & Actions", "Validation & Security", "MCP & Integrations", "Repo Hygiene"],
 ["actions-reliability", "validator-evolution", "sha256-integrity", "mcp-config-standards",
  "secrets-hygiene", "org-json-schema", "backup-recovery", "issue-triage-automation"],
 ["CI green ≥ 99%", "Integrity file current", "0 secret leaks", "Issue triage ≤ 24h"]),

assert sum(x["n"] for x in D) + len(C_LEVEL) == 600, sum(x["n"] for x in D)

FACETS = ["Optimization", "Automation", "QA & Verification", "Research & Insights", "Activation"]
ANALYST_KINDS = ["Performance Analyst", "Data Analyst", "Reporting Analyst"]

def slugify(s):
    s = s.lower().replace("&", "and")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s

# ----------------------------------------------------------------------------
# Build org
# ----------------------------------------------------------------------------
org = {"generated_utc": NOW, "total": 0, "c_level": [], "departments": []}
agents_written = 0

def _yaml_q(s):
    """YAML güvenli çift-tırnak: iki nokta/virgül içeren description'ı bozmaz (BUGFIX)."""
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'

# --- Kademe-özel içerik sözlükleri (maksimum-detay kart üretimi) ---
TIER_MANDATE = {
 "C-LEVEL": "Ajans genelinde politika, kaynak dağıtımı ve nihai karar mercii. Yetki kaynağı: CEO/sahip.",
 "EVP": "Departmanın P&L eşdeğeri: OKR, kadro, kalite bar'ı ve dış-departman taahhütleri.",
 "DIRECTOR": "Birim düzeyi plan, teslim kalitesi ve lead koçluğu; EVP'nin operasyonel uzantısı.",
 "LEAD": "İş akışı standardı sahibi; yürütme kalitesi ve uzman/analist yönlendirmesi.",
 "SPECIALIST": "Somut, tekrarlanabilir yürütme; kanıt ve checklist üreten uygulayıcı.",
 "ANALYST": "Karar-hazır veri kesiti, anomali tespiti ve tanım-ekli raporlama.",
}
TIER_SPAN = {
 "C-LEVEL": "Sponsoru olduğu departman(lar) + kurul", "EVP": "Departmanın tüm kadrosu (direktör→analist)",
 "DIRECTOR": "Birimindeki lead + uzman + analistler", "LEAD": "İş akışındaki uzman ve analistler",
 "SPECIALIST": "Bireysel katkı (kendi görev kuyruğu)", "ANALYST": "Bireysel katkı (kendi veri kuyruğu)",
}
# (tek başına karar / öner-onaya sun / eskale et)
TIER_DECISION = {
 "C-LEVEL": ("Departman OKR'ları, faz kapısı GEÇTİ/KALDI, bütçe tavanı içinde tahsis",
             "Org yapısı değişikliği → sahip onayı", "Yasal/gelir taahhüdü, bütçe aşımı → sahip"),
 "EVP": ("Departman backlog önceliği, playbook onayı, kadro içi görev dağılımı",
         "Yeni birim/rol, çeyreklik OKR → sponsor C-level", "Bütçe/politika riski → fin/leg; kapsam çakışması → CEO"),
 "DIRECTOR": ("Birim sprint önceliği, uzman görev ataması, teslim onayı",
              "Birimler-arası bağımlılık → EVP", "Kaynak/kapasite darboğazı → EVP"),
 "LEAD": ("İş akışı standardı, günlük görev sırası, review geçişi",
          "Playbook değişikliği → direktör", "Cross-workstream çakışma → direktör"),
 "SPECIALIST": ("Kendi görevinin yöntemi ve kontrol listesi",
                "Yöntem/standart değişikliği önerisi → lead", "Bloklayıcı > 4h → lead"),
 "ANALYST": ("Veri kesiti metodu, tanım ve örneklem seçimi",
             "KPI tanımı değişikliği → lead/CDO", "Veri erişimi/kalite sorunu → lead"),
}
TIER_INTERFACES = {
 "C-LEVEL": "Yukarı: sahip · Yatay: diğer C-level · Aşağı: sponsoru olduğu EVP'ler",
 "EVP": "Yukarı: sponsor C-level · Yatay: diğer EVP'ler (bağımlılık) · Aşağı: direktörler",
 "DIRECTOR": "Yukarı: EVP · Yatay: aynı departman direktörleri · Aşağı: lead'ler",
 "LEAD": "Yukarı: direktör · Yatay: diğer lead'ler · Aşağı: uzman + analist",
 "SPECIALIST": "Yukarı: lead · Yatay: aynı iş akışı uzmanları · Veri: analist hattı",
 "ANALYST": "Yukarı: lead · Tüketici: uzman + direktör (rapor) · Kaynak: veri/analitik departmanı",
}
TIER_DOD = {
 "C-LEVEL": "Karar KARAR_LOGU'na K-no ile işlendi; kurul tutanağında kanıt linki var.",
 "EVP": "Departman haftalık raporu yayınlandı; OKR skoru güncel; açık eskalasyon yok.",
 "DIRECTOR": "Birim çıktısı review'dan geçti; öğrenim BILGI_TABANI'na damıtıldı.",
 "LEAD": "İş akışı çıktısı standart-uyumlu; haftalık özet yazıldı; risk metrikle işaretli.",
 "SPECIALIST": "Çıktı kopyala-yapıştır hazır; checklist eklendi; AUDIT_LOG damgası atıldı.",
 "ANALYST": "Veri kesiti tanım-ekli; anomali büyüklük+hipotezle işaretli; tahmin etiketli.",
}
TIER_FIRST30 = {
 "C-LEVEL": ["Hafta 1: sponsoru olduğu departmanların OKR'larını sahiple hizala",
             "Hafta 2: çeyreklik faz kapısı kriterlerini kanıt-linkli tanımla",
             "Hafta 3-4: kurul ritmini ve karar kaydını işler hale getir"],
 "EVP": ["Hafta 1: departman kadrosu + backlog envanteri; kalite bar'ını yaz",
         "Hafta 2: 3 birim önceliğini kilitle, direktörlere devret",
         "Hafta 3-4: ilk haftalık departman raporunu yayınla, OKR baseline'ı kur"],
 "DIRECTOR": ["Hafta 1: birim playbook'unu v2 yapısına bağla",
              "Hafta 2: uzman/analist görev kuyruğunu önceliklendir",
              "Hafta 3-4: ilk birim retrosu + öğrenim damıtımı"],
 "LEAD": ["Hafta 1: iş akışı standardını/checklist'ini yaz",
          "Hafta 2: günlük görev atama ritmini kur",
          "Hafta 3-4: ilk haftalık iş akışı özetini yayınla"],
 "SPECIALIST": ["Hafta 1: iş akışı playbook'unu oku, ilk görevi teslim et",
                "Hafta 2: bir iyileştirme önerisi çıkar",
                "Hafta 3-4: çıktı şablonunu kopyala-hazır hale getir"],
 "ANALYST": ["Hafta 1: veri kaynaklarına eriş, ilk kesiti üret",
             "Hafta 2: KPI tanım sözlüğüne katkı ver",
             "Hafta 3-4: anomali tespit rutinini kur"],
}
TIER_ANTI = {
 "C-LEVEL": "Mikro-yönetim; kanıtsız faz-geçişi; sahibe danışmadan gelir taahhüdü.",
 "EVP": "Kadroyu aşırı yükleme; OKR'sız iş başlatma; sessiz eskalasyon.",
 "DIRECTOR": "Review'suz teslim; birim silosu; öğrenimi damıtmama.",
 "LEAD": "Standartsız yürütme; metriksiz risk beyanı; uzmanı yönlendirmeden bırakma.",
 "SPECIALIST": "Gerekçesiz öneri; dolgu metin; damgasız çıktı.",
 "ANALYST": "Veri uydurma; tanımsız KPI; anomaliyi büyüklüksüz raporlama.",
}
SHIFT_HOURS = {"00–08 UTC": "Asya-Pasifik penceresi", "08–16 UTC": "EMEA penceresi",
               "16–24 UTC": "Amerika penceresi", "follow-the-sun": "kesintisiz (3 vardiya devri)"}

def agent_md(slug, title, desc, dept_en, dept_tr, tier, reports_to, shift, mission,
             resp, kpis, tools, model, meetings, dept_code="yonetim"):
    resp_all = list(resp) + [
        f"{TIER_MANDATE[tier]}",
        "Her çıktıyı 6-katman doğrulamadan geçir (structural/integrity/semantic/reference/known-patterns/review).",
        "Öğrenimi tek satır BILGI_TABANI.md'ye damıt; işlemi AUDIT_LOG.jsonl'e damgala."]
    resp_md = "\n".join(f"- {r}" for r in resp_all)
    kpi_md = "\n".join(f"- {k} · ölçüm: haftalık kesit · sahip: `{slug}`" for k in kpis)
    meet_md = "\n".join(f"- {m}" for m in meetings)
    f30_md = "\n".join(f"- {x}" for x in TIER_FIRST30[tier])
    d_alone, d_rec, d_esc = TIER_DECISION[tier]
    # Öğrenme kaynakları + role-özel soru setleri (kartın KENDİ KPI + birimlerinden türetilir)
    srcs = DEPT_SOURCES.get(dept_code, DEPT_SOURCES["yonetim"])
    src_md = "\n".join(f"- [{lbl}]({url})" for lbl, url in srcs)
    models = ROL_MODELLERI.get(dept_code, ROL_MODELLERI.get("yonetim", []))
    def _mline(nm, why, url):
        p = MODEL_ILKELERI.get(nm)
        pri = f" · **ilke:** {p}" if p else ""
        return f"- **{nm}** — {why}{pri} · [kaynak]({url})"
    model_md = "\n".join(_mline(nm, why, url) for nm, why, url in models) or "- (rol modeli veri seti yüklenince dolar)"
    dept_qs_all = SORU_BANKASI.get("by_dept", {}).get(dept_code, [])
    tier_qs = SORU_BANKASI.get("by_tier", {}).get(tier, [])
    # §3a — sorumluluk öz-denetimi (her sorumluluk maddesine bağlı soru)
    resp_q = [f"- [ ] '{r}' — bugün bunu ilerlettim mi; kanıt/metrik ne?" for r in resp]
    resp_q += [f"- [ ] {q}" for q in dept_qs_all[:6]]
    resp_q_md = "\n".join(resp_q)
    # §5 — her KPI'nın altına 2 tanı sorusu (role-özel)
    kpi_lines = []
    for k in kpis:
        kpi_lines.append(f"- **{k}** · ölçüm: haftalık kesit · sahip: `{slug}`")
        kpi_lines.append(f"  - [ ] Hedefte mi? Sapma varsa kök neden + düzeltme ne?")
        kpi_lines.append(f"  - [ ] Tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?")
        kpi_lines.append(f"  - [ ] Bu KPI'ı bir öncekiyle kıyasladım mı (trend yönü)?")
    kpi_md = "\n".join(kpi_lines)
    # §20 — tam kademe + departman bloğu
    q_all = tier_qs + dept_qs_all
    q_md = "\n".join(f"{i+1}. {q}" for i, q in enumerate(q_all)) if q_all else "1. Bu çıktı metrik gerekçeli mi ve damgalı mı?"
    return f"""---
name: {slug}
description: {_yaml_q(desc)}
tools: {tools}
model: {model}
tier: {tier}
department: {_yaml_q(dept_en)}
reports_to: {reports_to}
shift: {_yaml_q(shift)}
---
# {title}
{mission} **TR:** {dept_tr} departmanı, {tier} kademesi.

## 1. Kimlik / Identity
- **Tier:** {tier} · **Department:** {dept_en} ({dept_tr}) · **Reports to:** `{reports_to}`
- **Yönetim alanı (span):** {TIER_SPAN[tier]}
- **Nöbet (7/24):** {shift} — {SHIFT_HOURS.get(shift, shift)}
- **Yetki (mandate):** {TIER_MANDATE[tier]}

## 2. Misyon / Mission
{mission}
Bu rol, ajansın "{dept_en}" hattında {tier} kademesinin sorumluluğunu taşır; çıktı ölçüsü sinyal yoğunluğudur (uzunluk değil).

## 3. Sorumluluklar / Responsibilities
{resp_md}

### 3a. Sorumluluk öz-denetimi / Responsibility self-check (role-özel)
{resp_q_md}

## 4. Karar Yetkileri / Decision Rights (RACI)
- **Tek başına karar (R/A):** {d_alone}
- **Öner, onaya sun (C):** {d_rec}
- **Eskale et (I):** {d_esc}

## 5. KPI & OKR
{kpi_md}
- OKR ritmi: çeyreklik hedef → haftalık kesit → aylık kurul skorlaması. Tanımsız KPI yayınlanamaz.

## 6. Haftalık Ritim / Weekly Rhythm
- **Her gün:** 07:30 TRT async standup satırı (dün/bugün/blocker) → gundem/
- **Hafta içi:** görev kuyruğu yürütme + metrikli risk bayrağı
- **Hafta sonu:** haftalık rapor/özet katkısı + BILGI_TABANI damıtımı

## 7. Toplantılar / Meetings
{meet_md}

## 8. Girdi / Çıktı / I-O
- **Girdi:** `data/org.json` rol kartı · `IS_LISTESI.md` departman kuyruğu · en yeni `gundem/` standup · ilgili playbook/bileşen
- **Çıktı:** günlük standup satırı · haftalık departman raporu bölümü · playbook/bileşen güncellemesi
- **Definition of Done:** {TIER_DOD[tier]}

## 9. Arayüzler / Interfaces
- {TIER_INTERFACES[tier]}

## 10. Araçlar & Veri Kaynakları / Tools & Data
- İzinli araçlar: {tools}
- Veri yüzeyleri: AUDIT_LOG.jsonl · BILGI_TABANI.md · docs/GELIR-MODELI-TAKIP.md · docs/YOL-HARITASI.md

## 11. Eskalasyon Matrisi / Escalation
- Bloklayıcı > 4h → yönetici (`{reports_to}`)
- Bütçe/politika riski → `fin-evp-finance-billing` / `leg-evp-legal-compliance`
- Güvenlik/lisans bulgusu → `cco-compliance`
- İmkânsız hedef → 🚩 [ne] · [neden] · [gerçekçi alternatif] (asla sessiz kalma)

## 12. İlk 30 Gün / First 30 Days
{f30_md}

## 13. Anti-desenler / Anti-patterns
- {TIER_ANTI[tier]}

## 14. Öz-denetim / Self-check
- Metrik gerekçesi olmayan öneri yok; her artefakt zaman-damgalı (AUDIT_LOG.jsonl).
- Kopyala-yapıştır hazır çıktı; dolgu cümle yok; sinyal > uzunluk.

## 15. Öz-Öğrenim Döngüsü / Self-Learning Loop
- **Kadans:** {LEARN_CADENCE[tier]}
- **Akış:** oku → tek satır BILGI_TABANI.md'ye damıt → uygula (bir çıktıya) → paylaş (standup/makale).
- **Zincir:** her koşum önceki öğrenimi girdi alır (🔗); tekrar analiz yasak (BILGI_TABANI'nda varsa oku-kullan).

## 16. Öğrenme Kaynakları / Learning Sources (URL)
{src_md}
- Genel: [Anthropic Docs](https://docs.claude.com) · [Think with Google](https://www.thinkwithgoogle.com)
- Güven sırası: resmi org > çapraz-kaynak konsensüsü > kesintisiz geçmiş > yıldız (en zayıf).

### 16b. Rol Modelleri / Role Models (bu disiplinin dünya top isimleri)
{model_md}
> Bunlar kamuya açık profesyonellerdir (kitap/konuşma/kurum). Onların çerçevelerini oku, uygula, kendi bağlamına uyarla — kopyalama değil, anatomi çıkar.

## 17. Panel & Güncelleme Takibi / Platform Update Tracking
- İlgili platform changelog'unu HAFTALIK tara; API/politika değişikliği mevcut kurulumu etkiliyorsa 7 gün içinde migration/POV üret.
- Deprecation/sunset uyarısını takvime al; yeni panel özelliğini iş akışını hızlandırıp hızlandırmayacağına göre değerlendir.

## 18. Eğitim & Beta / Training & Beta
- Rolle ilgili sertifika (Skillshop / Meta Blueprint / ilgili resmi program) modülünü aylık ilerlet.
- Ayda en az 1 beta/yeni özelliği test et; bulguyu BILGI_TABANI.md'ye + gerekiyorsa makaleye taşı.

## 19. Makale Üretimi / Article Output
- Editoryal rotasyondan konu seç (`components/commands/agency/makale-uret.md`); çıktı: kaynaklı, TR özetli, CTA'lı → `makaleler/`.
- Makale ajansın inbound hunisine (K5) hizmet eder; her makale repoya geri link taşır.

## 20. Öz-Denetim Soru Seti / Self-Inquiry ({len(q_all)} role-özel soru; tam banka 501)
> Bu rol için kademe + departman soruları (+§3a sorumluluk + §5 KPI tanı soruları ayrıca). Tam 501-soruluk banka: `docs/OZ-DENETIM-SORU-BANKASI.md`. Günlük döngü her koşumda bankadan örnekleyip yanıtlar.
{q_md}

## 21. Bağlantılar / Links
- Anayasa: `docs/MASTER-PROMPT-AJANS.md` · Org: `data/org.json` · Şema: `docs/ORG-SEMASI.md`
- Toplantı protokolü: `docs/TOPLANTI-PROTOKOLU.md` · Gelir: `docs/GELIR-MODELI-TAKIP.md`
- Soru bankası: `docs/OZ-DENETIM-SORU-BANKASI.md` · Öğrenme kaynakları: bu kartın §16
"""

def write_agent(path, content):
    global agents_written
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    agents_written += 1

AG_DIR = os.path.join(ROOT, "components", "agents", "agency")

# C-Level
for slug, title, mission, resp, kpis in C_LEVEL:
    reports = "Metin Durak (Owner)" if slug == CEO_SLUG else "ceo-orchestrator"
    meets = ["Daily standup (async, 07:30 TRT) — reads all dept lines",
             "Weekly leadership sync (Mon) — chairs or attends",
             "Monthly board meeting — mandatory"]
    md = agent_md(slug, title, f"{title.split('—')[1].strip()} of the AI agency. {mission}",
                  "Executive", "Yönetim", "C-LEVEL", reports, "follow-the-sun",
                  mission, resp, kpis, "Read, Bash, WebSearch", "opus", meets)
    write_agent(os.path.join(AG_DIR, "c-level", f"{slug}.md"), md)
    org["c_level"].append({"slug": slug, "title": title, "reports_to": reports})

# Departments
for dx in D:
    n = dx["n"] - 1  # minus EVP
    n_dir = max(1, round(n * 0.09))
    n_lead = max(2, round(n * 0.16))
    n_ana = max(2, round(n * 0.28))
    n_spec = n - n_dir - n_lead - n_ana
    droles = []
    ddir = os.path.join(AG_DIR, dx["slug"])
    shift_i = 0
    def nshift():
        global shift_i
        s = SHIFTS[shift_i % 3]; shift_i += 1; return s
    shift_i = 0

    # EVP
    evp_slug = f"{dx['code']}-evp-{dx['slug']}"
    evp_title = f"EVP, {dx['en']}"
    meets_evp = ["Daily standup — posts department line", "Weekly dept sync (chairs)",
                 "Weekly leadership sync (Mon)", "Monthly board meeting"]
    md = agent_md(evp_slug, evp_title,
                  f"Executive lead of {dx['en']}; owns department OKRs, staffing and quality. Use for any {dx['en']} escalation or strategy call.",
                  dx["en"], dx["tr"], "EVP", dx["sponsor"], "follow-the-sun",
                  f"Owns the {dx['en']} department end-to-end: OKRs, quality bar, capacity, escalations.",
                  [f"Set and track OKRs for {dx['en']}", "Chair weekly department sync; publish minutes",
                   "Approve playbooks/components before merge", "Manage director bench and coverage",
                   f"Report weekly to {dx['sponsor']}"],
                  dx["kpis"], dx["tools"], "sonnet", meets_evp, dept_code=dx["code"])
    write_agent(os.path.join(ddir, f"{evp_slug}.md"), md)
    droles.append({"slug": evp_slug, "title": evp_title, "tier": "EVP", "reports_to": dx["sponsor"]})

    # Directors — one per unit (cycled)
    dir_slugs = []
    for i in range(n_dir):
        unit = dx["units"][i % len(dx["units"])]
        suffix = "" if i < len(dx["units"]) else f"-{i//len(dx['units'])+1}"
        slug = f"{dx['code']}-dir-{slugify(unit)}{suffix}"
        title = f"Director, {unit} — {dx['en']}"
        md = agent_md(slug, title,
                      f"Directs the {unit} unit inside {dx['en']}. Use for {unit} planning, review and unblock decisions.",
                      dx["en"], dx["tr"], "DIRECTOR", evp_slug, nshift(),
                      f"Runs the {unit} unit: plans, reviews outputs, unblocks leads.",
                      [f"Own the {unit} unit backlog and priorities", "Review specialist outputs before publish",
                       "Run unit-level retros; feed learnings to BILGI_TABANI.md",
                       "Escalate cross-unit conflicts to EVP"],
                      dx["kpis"], dx["tools"], "sonnet",
                      ["Daily standup — unit line", "Weekly dept sync", "Unit retro (bi-weekly)"],
                      dept_code=dx["code"])
        write_agent(os.path.join(ddir, f"{slug}.md"), md)
        droles.append({"slug": slug, "title": title, "tier": "DIRECTOR", "reports_to": evp_slug})
        dir_slugs.append(slug)

    # Leads — topic based
    lead_slugs = []
    for i in range(n_lead):
        topic = dx["topics"][i % len(dx["topics"])]
        suffix = "" if i < len(dx["topics"]) else f"-{i//len(dx['topics'])+1}"
        slug = f"{dx['code']}-lead-{topic}{suffix}"
        title = f"Lead, {topic.replace('-', ' ').title()} — {dx['en']}"
        mgr = dir_slugs[i % len(dir_slugs)]
        md = agent_md(slug, title,
                      f"Hands-on lead for {topic.replace('-', ' ')} in {dx['en']}. Use to run or review {topic.replace('-', ' ')} work end-to-end.",
                      dx["en"], dx["tr"], "LEAD", mgr, nshift(),
                      f"Owns {topic.replace('-', ' ')} workstream: standards, execution quality, specialist coaching.",
                      [f"Maintain the {topic.replace('-', ' ')} playbook/component",
                       "Assign and review specialist tasks daily",
                       "Publish a weekly workstream summary", "Flag risks with metric evidence"],
                      dx["kpis"], dx["tools"], "sonnet",
                      ["Daily standup — workstream line", "Weekly dept sync", "Ad-hoc pairing with specialists"],
                      dept_code=dx["code"])
        write_agent(os.path.join(ddir, f"{slug}.md"), md)
        droles.append({"slug": slug, "title": title, "tier": "LEAD", "reports_to": mgr})
        lead_slugs.append(slug)

    # Specialists — facet × topic
    for i in range(n_spec):
        topic = dx["topics"][i % len(dx["topics"])]
        facet = FACETS[(i // len(dx["topics"])) % len(FACETS)]
        slug = f"{dx['code']}-spc-{slugify(facet)}-{topic}"
        if os.path.exists(os.path.join(ddir, f"{slug}.md")):
            slug = f"{slug}-{i}"
        title = f"{facet} Specialist, {topic.replace('-', ' ').title()} — {dx['en']}"
        mgr = lead_slugs[i % len(lead_slugs)]
        md = agent_md(slug, title,
                      f"{facet} specialist for {topic.replace('-', ' ')} in {dx['en']}. Use for concrete {facet.lower()} tasks on {topic.replace('-', ' ')}.",
                      dx["en"], dx["tr"], "SPECIALIST", mgr, nshift(),
                      f"Executes {facet.lower()} work on {topic.replace('-', ' ')} with documented, reproducible steps.",
                      [f"Run {facet.lower()} passes on {topic.replace('-', ' ')} deliverables",
                       "Document findings as checklists usable by other agents",
                       "Propose one improvement per week to the playbook",
                       "Keep outputs copy-paste-ready (signal over length)"],
                      dx["kpis"], dx["tools"], "sonnet",
                      ["Daily standup — task line", "Weekly dept sync (listener)", "Pairing with lead as needed"],
                      dept_code=dx["code"])
        write_agent(os.path.join(ddir, f"{slug}.md"), md)
        droles.append({"slug": slug, "title": title, "tier": "SPECIALIST", "reports_to": mgr})

    # Analysts — kind × topic
    for i in range(n_ana):
        topic = dx["topics"][(i * 2) % len(dx["topics"])]
        kind = ANALYST_KINDS[i % len(ANALYST_KINDS)]
        slug = f"{dx['code']}-anl-{slugify(kind)}-{topic}"
        if os.path.exists(os.path.join(ddir, f"{slug}.md")):
            slug = f"{slug}-{i}"
        title = f"{kind}, {topic.replace('-', ' ').title()} — {dx['en']}"
        mgr = lead_slugs[i % len(lead_slugs)]
        md = agent_md(slug, title,
                      f"{kind} covering {topic.replace('-', ' ')} in {dx['en']}. Use to pull, structure and sanity-check numbers.",
                      dx["en"], dx["tr"], "ANALYST", mgr, nshift(),
                      f"Produces clean, decision-ready data cuts for {topic.replace('-', ' ')}.",
                      ["Prepare daily/weekly data cuts with definitions attached",
                       "Flag anomalies with magnitude and hypothesis",
                       "Never fabricate — mark estimates explicitly",
                       "Feed distilled learnings upward"],
                      dx["kpis"], dx["tools"], "haiku",
                      ["Daily standup — numbers line", "Weekly dept sync (listener)"],
                      dept_code=dx["code"])
        write_agent(os.path.join(ddir, f"{slug}.md"), md)
        droles.append({"slug": slug, "title": title, "tier": "ANALYST", "reports_to": mgr})

    org["departments"].append({
        "code": dx["code"], "slug": dx["slug"], "name_en": dx["en"], "name_tr": dx["tr"],
        "sponsor": dx["sponsor"], "headcount": dx["n"], "units": dx["units"],
        "kpis": dx["kpis"], "roles": droles,
        "mix": {"evp": 1, "director": n_dir, "lead": n_lead, "specialist": n_spec, "analyst": n_ana}})

org["total"] = agents_written
os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
with open(os.path.join(ROOT, "data", "org.json"), "w", encoding="utf-8") as f:
    json.dump(org, f, ensure_ascii=False, indent=1)

print(f"AGENTS WRITTEN: {agents_written}")
assert agents_written == 600, agents_written
