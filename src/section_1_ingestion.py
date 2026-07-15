import pandas as pd

# Load 'financial_Transactions_Cleaned.csv'
df = pd.read_csv('financial_Transactions_Cleaned.csv')

# Update 'Transaction_Type' based on 'Quantity'
df['Transaction_Type'] = df['Quantity'].apply(lambda x: 'Buy' if x > 0 else 'Sell')

# Save 'financial_Transactions_Updated.csv'
df.to_csv('financial_Transactions_Updated.csv', index=False)
