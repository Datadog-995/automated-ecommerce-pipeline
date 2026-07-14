import os
import pandas as pd
import numpy as np

def run_ecommerce_pipeline(data_path):
    print("🚀 Starting Automated E-Commerce Data Pipeline...")
    
    # --- PHASE 1: Data Ingestion & Cleaning (Orders) ---
    print("[1/4] Loading and cleaning orders dataset...")
    orders_df = pd.read_csv(os.path.join(data_path, "olist_orders_dataset.csv"))
    
    date_cols = ['order_purchase_timestamp', 'order_approved_at', 'order_delivered_customer_date']
    for col in date_cols:
        orders_df[col] = pd.to_datetime(orders_df[col], errors='coerce')
        
    orders_df['order_approved_at'] = orders_df['order_approved_at'].fillna(orders_df['order_purchase_timestamp'])
    orders_df['delivery_audit_flag'] = np.where(
        orders_df['order_delivered_customer_date'].isna(), 'Flagged: Missing Delivery', 'Verified Complete'
    )
    
    # --- PHASE 2: Relational Merge (Financials) ---
    print("[2/4] Merging financial data and calculating transaction values...")
    items_df = pd.read_csv(os.path.join(data_path, "olist_order_items_dataset.csv"))
    master_df = pd.merge(orders_df, items_df, on='order_id', how='inner')
    master_df['total_transaction_value'] = master_df['price'] + master_df['freight_value']
    
    # --- PHASE 3: Product Enrichment ---
    print("[3/4] Connecting product catalog for business intelligence...")
    products_df = pd.read_csv(os.path.join(data_path, "olist_products_dataset.csv"))
    final_pipeline_df = pd.merge(master_df, products_df, on='product_id', how='left')
    
    # --- PHASE 4: Exporting Final Deliverable ---
    print("[4/4] Exporting clean, dashboard-ready master file...")
    final_pipeline_df.to_csv("clean_ecommerce_master.csv", index=False)
    
    print("✅ Pipeline Execution Complete. Data is ready for analysis.")

if __name__ == "__main__":
    # Point this to wherever the raw files are stored
    run_ecommerce_pipeline(".")
