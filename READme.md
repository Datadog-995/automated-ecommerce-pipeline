# Automated E-commerce ETL Pipeline

This project is an automated Data Engineering pipeline designed to streamline product data management.

## Project Workflow
1. **Extract**: Fetches raw JSON product data from a live API.
2. **Transform**: Normalizes, cleans, and standardizes data using `Pandas`.
3. **Validate**: Enforces a strict schema contract with `Pandera` to ensure data quality.
4. **Load**: Persists the clean data into a SQLite database.
5. **Verify**: Automates a "Health Report" to confirm data integrity.

## How to run
This project is built to run in a Google Colab environment. Simply upload the `.ipynb` file to Colab, mount your Google Drive, and run the cells sequentially. Alternatively, the included `ecommerce_etl_pipeline.py` script can be run in any standard Python environment.
