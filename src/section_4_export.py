import pandas as pd
import numpy as np

# Load 'financial_Transactions_Audited.csv'
df = pd.read_csv('financial_Transactions_Audited.csv')

# Determine the correct column names dynamically
category_col = 'Product_Category' if 'Product_Category' in df.columns else ('product_category_name' if 'product_category_name' in df.columns else 'Category')
status_col = 'Transaction_Status' if 'Transaction_Status' in df.columns else 'Status'

# Define 'median_prices' dictionary dynamically from the actual audited dataset
median_prices = df.dropna(subset=['Price']).groupby(category_col)['Price'].median().to_dict()
print("Defined median_prices:", median_prices)

# Create Imputation Audit columns
df['Price_Imputed'] = df['Price'].isna().astype(int)
df['Quantity_Imputed'] = df['Quantity'].isna().astype(int)

# Impute missing 'Price'
df['Price'] = df.apply(
    lambda row: median_prices.get(row[category_col], df['Price'].median()) if pd.isna(row['Price']) else row['Price'],
    axis=1)

# Impute missing 'Quantity'
quantity_median = df['Quantity'].median()
if pd.isna(quantity_median):
    quantity_median = 1
df['Quantity'] = df['Quantity'].fillna(quantity_median)

# Clean up 'Unknown' 'Transaction_Status'
non_unknown_status = df[df[status_col] != 'Unknown'][status_col].dropna()
if not non_unknown_status.empty:
    status_mode = non_unknown_status.mode()[0]
else:
    status_mode = 'Completed'
df[status_col] = df[status_col].replace('Unknown', status_mode)
df[status_col] = df[status_col].fillna(status_mode)

# Recalculate 'Transaction_Type'
df['Transaction_Type'] = df.apply(
    lambda row: 'Refund' if row['Quantity'] < 0 or row[status_col] in ['Refunded', 'Cancelled'] else 'Purchase',
    axis=1
)

# Save the final file as 'financial_Transactions_Final_Clean.csv'
df.to_csv('financial_Transactions_Final_Clean.csv', index=False)
