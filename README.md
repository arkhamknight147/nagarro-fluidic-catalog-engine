# 🦅 Nagarro | Fluidic Catalog Intake Engine
### Autonomous Multi-Agent B2B Data Supply Chain Accelerator

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://nagarro-fluidic-catalog-engine.streamlit.app/)
[![Platform](https://img.shields.io/badge/Platform-Nagarro_NIA_Framework-0052CC.svg)](https://www.nagarro.com/en/services/data-analytics-intelligence/nia-genai-accelerator)
[![Governance](https://img.shields.io/badge/Governance-XMDM360_Compliance-green.svg)](https://www.nagarro.com/en/services/data-analytics-intelligence)

This enterprise-grade proof of concept bridges the critical operational value gap that global Enterprise Retail and Consumer Packaged Goods (CPG) clients encounter immediately following major cloud and e-commerce migrations (e.g., migrations to SAP Commerce Cloud or Shopify Plus).

---

## 📑 Strategic & Technical Documentation

For an in-depth breakdown of the business case, strategic alignment, and product specifications, explore the repository documentation:
* 📄 **[Problem Statement & Solution Strategy](docs/problem_solution_fluidic_catalog.md)** — Analysis of the product data supply chain bottleneck, Chloe's user journey, and Nagarro strategic alignment.
* 📋 **[Product Requirement Document (PRD)](docs/prd_fluidic_catalog.md)** — Full functional and non-functional requirements, agent system specs, OKRs, and risk matrices.

---

## 📊 The Core Enterprise Friction Statement

Following large-scale infrastructure modernizations, retail enterprises face severe operational latency because their downstream partner ingestion pipelines remain siloed. Merchandisers spend thousands of unbillable manual hours sanitizing, reformatting, and fixing unstructured product catalog data arriving from hundreds of diverse B2B supplier pools. 

This manual friction delays product time-to-market by weeks, corrupts downstream forecasting metrics (such as Nagarro's Forecastra AI), and prevents organizations from capturing the promised ROI of their unified cloud investments.

---

## 🛠️ The Fluidic Intelligence Solution

Built explicitly upon Nagarro's signature **Fluidic Intelligence Operating Paradigm**, this accelerator sits upstream of production enterprise architectures to eliminate ingestion friction using a decentralized team of specialized AI agents running within the **Nagarro NIA Framework Core**:

```
[ Unstandardized B2B Supplier Data ]
         (Flat CSVs, Messy Excel, PDFs)
                       │
                       ▼
┌────────────────────────────────────────────────────────┐
│ FLUIDIC CATALOG ENGINE (NIA AGENT LAYER)               │
│                                                        │
│  ┌──────────────────────────────────────────────────┐  │
│  │ 1. Supervisor Orchestrator Agent (State Routing) │  │
│  └──────────┬────────────────────────────┬──────────┘  │
│             ▼                            ▼             │
│  ┌──────────────────────┐    ┌──────────────────────┐  │
│  │ 2. Multimodal Parser │    │ 3. Schema Mapping    │  │
│  │    Agent (OCR/Token) │    │    Agent (Zero-Shot) │  │
│  └──────────┬───────────┘    └──────────┬───────────┘  │
└─────────────┼───────────────────────────┼──────────────┘
              ▼                           ▼
┌────────────────────────────────────────────────────────┐
│ 4. Deterministic Compliance Node (XMDM360 Logic Gate)  │
└───────────────────────────┬────────────────────────────┘
                            │
                   ┌────────┴────────┐
           Verified = True    Verified = False
                   ▼                 ▼
       [ Core ERP Sync API ]   [ Human Intercept Canvas ]
```

### Agent Specifications:
1. **Supervisor Orchestrator Agent (NIA Native):** Manages processing states across worker threads, handling batch scaling and exception dependencies.
2. **Multimodal File-Parser Agent:** Contextually parses unstructured document structures (`.xlsx`, `.csv`, `.pdf`), converting messy layouts into uniform raw tokens.
3. **Schema Mapping Agent (OpenAI LLM Node):** Translates arbitrary supplier headers (e.g., `Ref_Num`, `DealerCost`, `MSRP_Price`) and contextually aligns them with master catalog standards using zero-shot semantic matching.
4. **Anomaly & Compliance Agent (Deterministic XMDM360 Node):** Bypasses probabilistic models to execute absolute code-level logic verification (e.g., enforcing profit margin floors and catching zero/negative price anomalies).

---

## ⚡ Live Verification & Quick Start

### 1. Direct Access Cloud Deployment
Interact with the live, multi-agent pipeline in production here:  
👉 **[https://nagarro-fluidic-catalog-engine.streamlit.app/](https://nagarro-fluidic-catalog-engine.streamlit.app/)**

### 2. Ready-to-Test 50-SKU Dataset
A dedicated validation file containing edge cases (such as intentional negative margins and zero-price anomalies in rows 1045–1047) is available in the root folder:  
📁 **[`nagarro_50_sku_test_dataset.csv`](nagarro_50_sku_test_dataset.csv)**

### 3. Local Machine Installation
To clone and run this application locally inside a sandboxed environment:

```powershell
# 1. Clone repository
git clone https://github.com/arkhamknight147/nagarro-fluidic-catalog-engine.git
cd nagarro-fluidic-catalog-engine

# 2. Build and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch local Streamlit engine
streamlit run app.py
```

---

## 🎯 Target Business Impact

* **Cycle Time Reduction:** Ingestion cycle compressed from 5 business days to under 15 minutes ($>90\%$ reduction).
* **Manual Effort Savings:** Manual data sanitation work for category managers reduced by at least $80\%$.
* **Schema Accuracy:** $>92\%$ zero-shot column mapping precision on unseen supplier layouts.
* **Downstream Data Integrity:** $100\%$ validation clearance rate before data reaches production core ERP/PIM systems.