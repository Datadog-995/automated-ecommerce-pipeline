# 🛒 Automated E-Commerce Data Pipeline

## Overview
This repository contains a production-ready Python pipeline designed to ingest, clean, and merge messy, multi-table e-commerce data. It transforms raw, disconnected operational logs into a single, clean, dashboard-ready financial ledger.

📊 Note on Datasets: Due to the large file sizes of the raw Brazilian e-commerce datasets, GitHub may not display the web preview of some ⁠.csv⁠ files. However, the complete datasets are fully intact in the repository and will download normally.


## 🎯 The Business Problem Solved
E-commerce businesses often suffer from disconnected systems (e.g., sales data separated from product catalogs and shipping logs). Manual merging in spreadsheets causes crashes, data loss, and inaccurate revenue reporting. 

**This automated pipeline eliminates manual data entry by:**
1. **Handling Missing Data Safely:** Automatically auditing null delivery dates without deleting valuable transaction rows.
2. **Relational Merging:** Programmatically connecting thousands of raw orders to their specific product SKUs and shipping costs using automated `JOIN` logic.
3. **Business Intelligence Generation:** Instantly calculating total transaction values and grouping top-grossing product categories for executive dashboards.

## 🛠️ Tech Stack & Workflow
* **Language:** Python 3
* **Core Libraries:** `pandas`, `numpy`
* **Workflow:** Automated Data Ingestion -> Null Imputation -> Relational Merge -> Feature Engineering -> CSV/Excel Export

## 🚀 Impact
Processes 100,000+ relational database rows in under 2 seconds, entirely bypassing the need for manual Excel VLOOKUPs, saving hours of weekly administrative overhead and protecting database integrity.
<img width="1600" height="889" alt="Brazilian_ECommerce_Scale" src="https://github.com/user-attachments/assets/c7b039d2-1946-4b43-9bc3-cbaf009aef78" />


###  Web Scraping Success Rate
<img width="1600" height="1600" alt="Price_Extraction_Success (1)" src="https://github.com/user-attachments/assets/c06156d8-d545-43d6-af75-b04abc1e56fd" />
