import pandas as pd
from sqlalchemy import create_engine
import pandera as pa
from pandera import Column, DataFrameSchema
import requests

# 1. Configuration
API_URL = "https://jsonplaceholder.typicode.com/posts"
# Using a local relative path for the DB file
DB_PATH = 'sqlite:///ecommerce_data.db' 
TABLE_NAME = 'products'

# 2. ETL Functions
def extract_data(url):
    print("Extracting...")
    response = requests.get(url)
    return response.json()

def transform_data(raw_data):
    print("Transforming...")
    df = pd.json_normalize(raw_data)
    df = df.drop_duplicates()
    df = df.rename(columns={'title': 'product_name', 'body': 'description'})
    df['id'] = pd.to_numeric(df['id'])
    return df

def validate_and_load(df):
    print("Validating and Loading...")
    schema = DataFrameSchema({
        "id": Column(int),
        "product_name": Column(str),
        "description": Column(str, nullable=True)
    })
    
    try:
        validated_df = schema.validate(df)
        engine = create_engine(DB_PATH)
        validated_df.to_sql(TABLE_NAME, con=engine, if_exists='replace', index=False)
        print("Success: Data validated and loaded.")
    except Exception as e:
        print(f"Pipeline Error: {e}")

# 3. Execution
if __name__ == "__main__":
    raw_data = extract_data(API_URL)
    cleaned_df = transform_data(raw_data)
    validate_and_load(cleaned_df)
    
    # Verification
    engine = create_engine(DB_PATH)
    count = pd.read_sql(f"SELECT COUNT(*) FROM {TABLE_NAME}", engine).iloc[0, 0]
    print(f"Pipeline finished. Total records: {count}")
