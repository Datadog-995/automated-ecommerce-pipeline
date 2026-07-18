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
