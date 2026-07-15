import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('financial_Transactions_Final.csv')

# Identify columns dynamically
date_col = None
cust_col = None
price_col = None

for col in df.columns:
    col_lower = col.lower().replace('_', ' ').replace('  ', ' ').strip()
    if 'date' in col_lower:
        date_col = col
    elif 'customer' in col_lower or 'cust' in col_lower:
        cust_col = col
    elif 'price' in col_lower or 'amount' in col_lower or 'value' in col_lower:
        price_col = col

# Fallback to defaults if not found
if not date_col:
    date_col = 'Date'
if not cust_col:
    cust_col = 'Customer_ID'
if not price_col:
    price_col = 'Price'

# Apply Date Audit Status
def audit_date(val):
    try:
        if pd.isna(val) or str(val).strip() == '':
            return 'Invalid'
        pd.to_datetime(val)
        return 'Valid'
    except Exception:
        return 'Invalid'

date_audit = df[date_col].apply(audit_date)
df['Date Audit Status'] = date_audit
df['Date_Audit_Status'] = date_audit

# Apply Customer ID Audit Status (and padding fix)
def fix_cust_id(val):
    if pd.isna(val) or str(val).strip() == '':
        return np.nan
    try:
        s = str(int(float(val)))
    except ValueError:
        s = str(val).strip()
    return s.zfill(5)

df[cust_col] = df[cust_col].apply(fix_cust_id)

def audit_cust_id(val):
    if pd.isna(val) or str(val).strip() == '' or str(val).lower() == 'nan':
        return 'Invalid'
    s = str(val)
    if s.isdigit() and len(s) == 5:
        return 'Valid'
    return 'Invalid'

cust_audit = df[cust_col].apply(audit_cust_id)
df['Customer ID Audit Status'] = cust_audit
df['Customer_ID_Audit_Status'] = cust_audit

# Price Audit Check (converting negative prices to absolute values)
if price_col in df.columns:
    df[price_col] = pd.to_numeric(df[price_col], errors='coerce')
    df[price_col] = df[price_col].abs()

def audit_price(val):
    if pd.isna(val):
        return 'Invalid'
    try:
        p = float(val)
        if p > 0:
            return 'Valid'
        return 'Invalid'
    except Exception:
        return 'Invalid'

price_audit = df[price_col].apply(audit_price)
df['Price Audit Check'] = price_audit
df['Price_Audit_Check'] = price_audit

# Save as financial_Transactions_Audited.csv
df.to_csv('financial_Transactions_Audited.csv', index=False)
