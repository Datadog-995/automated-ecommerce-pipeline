# Automated E-commerce ETL Pipeline
> 📊 **Portfolio Focus:** This project demonstrates my ability to design, build, and deploy an automated, production-ready ETL pipeline. It showcases programmatic data extraction, robust schema validation using Pandera, and structured database storage, moving beyond manual data auditing into scalable data engineering.

### Project Workflow

1. **Extract**: Fetches raw JSON product data from a live API.
2. **Transform**: Normalizes, cleans, and standardizes data using `Pandas`.
3. **Validate**: Enforces a strict schema contract with `Pandera` to ensure data quality.
4. **Load**: Persists the clean data into a SQLite database.
5. **Verify**: Automates a "Health Report" to confirm data integrity.



# Data Integrity Audit: Financial Transactions

This repository contains an end-to-end audit and remediation pipeline for a dataset plagued by systemic data entry errors.

## Problem Solved: Data Auditing

The dataset contained significant integrity failures that I resolved to ensure report accuracy:
* **The "01/01/1900" Problem:** Thousands of rows contained default system date errors. I implemented a flagging system (`audited_dates`) to quarantine these records, preserving the audit trail for investigation.
* **Negative Financials:** I identified erroneous negative prices caused by system glitches, re-calculating values based on unit prices to restore financial integrity.
* **Missing Attributes:** Standardized "UNKNOWN" and "NaN" entries across categorical columns (Payment Methods, Locations) to ensure consistent grouping for business intelligence.

## Key Insights & Visualizations
*After cleaning, I generated the following reports to validate the dataset's integrity:*
#### 1. Top 10 Selling Products by Total Revenue
<img width="1200" height="600" alt="top_selling_products (1)" src="https://github.com/user-attachments/assets/72cd4ea4-8022-4ddd-869f-fcd5a300610d" />

#### 2. Payment Methods Breakdown
<img width="800" height="500" alt="payment_methods (1)" src="https://github.com/user-attachments/assets/9f2ce8ba-c73a-45f2-a722-ee7844013e20" />

## Repository Contents
* `raw_financial_transactions.csv`: The original, uncleaned source data.
* `CLEAN-Financial_Transactions.csv`: The finalized, cleaned dataset ready for analysis.
* `History-Openrefine-Financial_transactions.json`: Audit trail of transformation steps.
* `financial_Transactions_csv.ipynb`: The technical notebook used for verification.
