# 🛒 Automated E-Commerce Data Pipeline

## Overview
This repository contains a production-ready Python pipeline designed to ingest, clean, and merge messy, multi-table e-commerce data. It transforms raw, disconnected operational logs into a single, clean, dashboard-ready financial ledger.

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
