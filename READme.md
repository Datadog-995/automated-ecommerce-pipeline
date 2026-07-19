# Automated E-commerce ETL Pipeline

This project is an automated Data Engineering pipeline designed to streamline product data management.

### Project Workflow

1. **Extract**: Fetches raw JSON product data from a live API.
2. **Transform**: Normalizes, cleans, and standardizes data using `Pandas`.
3. **Validate**: Enforces a strict schema contract with `Pandera` to ensure data quality.
4. **Load**: Persists the clean data into a SQLite database.
5. **Verify**: Automates a "Health Report" to confirm data integrity.

```mermaid
graph LR
    A[Extract] --> B[Transform]
    B --> C[Validate]
    C --> D[Load]
    D --> E[Verify]

# Data Integrity Audit: Financial Transactions

This repository contains an end-to-end audit and remediation pipeline for a dataset plagued by systemic data entry errors.

## Problem Solved: Data Auditing
The dataset contained significant integrity failures that I resolved to ensure report accuracy:
* **The "01/01/1900" Problem:** Thousands of rows contained default system date errors. I implemented a flagging system (`audited_dates`) to quarantine these records, preserving the audit trail for investigation.
* **Negative Financials:** I identified erroneous negative prices caused by system glitches, re-calculating values based on unit prices to restore financial integrity.
* **Missing Attributes:** Standardized "UNKNOWN" and "NaN" entries across categorical columns (Payment Methods, Locations) to ensure consistent grouping for business intelligence.

## Key Insights & Visualizations
*After cleaning, I generated the following reports to validate the dataset's integrity:*

![Revenue by Product](revenue_by_product.png)
![Payment Methods](payment_methods.png)
![Monthly Sales Trends](monthly_sales_trend.png)

## Repository Contents
* `raw_financial_transactions.csv`: The original, uncleaned source data.
* `CLEAN-Financial_Transactions.csv`: The finalized, cleaned dataset ready for analysis.
* `History-Openrefine-Financial_transactions.json`: Audit trail of transformation steps.
* `financial_Transactions_csv.ipynb`: The technical notebook used for verification.
