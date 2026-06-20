import pandas as pd
import numpy as np
from icecream import ic as print
  
def load_data(data_path):
    """
    Loads the CSV file using the correct encoding and handles potential file errors.
    """
    try:
        # ISO-8859-1 encoding handles special currency symbols like £ (Pound)
        df = pd.read_csv(data_path, encoding="ISO-8859-1")
        print(f"[SUCCESS] Data loaded successfully. Rows: {df.shape[0]}, Columns: {df.shape[1]}")
        return df
    except Exception as e:
        print(f"[ERROR] Failed to load data: {e}")
        return None

def data_cleaning_pipeline(df):
    """
    Handles missing values and drops completely duplicated rows.
    """
    try:
        copy_df = df.copy()
        # 1. Drop rows where CustomerID is missing
        copy_df = copy_df.dropna(subset=["CustomerID"])
        # 2. Fill missing descriptions with a placeholder
        copy_df["Description"] = copy_df["Description"].fillna("UNKNOWN ITEM")
        # 3. Drop exact duplicate rows
        initial_rows = copy_df.shape[0]
        copy_df = copy_df.drop_duplicates()
        final_rows = copy_df.shape[0]
        print(f"[SUCCESS] Missing values handled & duplicates removed. Duplicates deleted: {initial_rows - final_rows}")
        return copy_df
    except Exception as e:
        print(f"[ERROR] Exception occurred in data cleaning pipeline: {e}")    
        return df

def fix_data_types(df):
    """
    Standardizes column data types (e.g., converting strings to datetime objects).
    """
    try:
        df_copy = df.copy()
        # Convert InvoiceDate from string object to datetime
        df_copy['InvoiceDate'] = pd.to_datetime(df_copy['InvoiceDate'])
        df_copy["CustomerID"]=df["CustomerID"].astype(int)
        print("[SUCCESS] Data types standardized (InvoiceDate converted to Datetime).")
        return df_copy
    except Exception as e:
        print(f"[ERROR] Exception occurred while fixing data types: {e}")
        return df

def filter_erroneous_and_canceled_transactions(df):
    """
    Filters out negative or zero values in Quantity and UnitPrice 
    to remove returns, cancellations, and bad debt adjustments.
    """
    try:
        df_copy = df.copy()
        initial_rows = df_copy.shape[0]
        # Filtering for valid commercial transactions only
        df_copy = df_copy[(df_copy['Quantity'] > 0) & (df_copy['UnitPrice'] > 0)]
        final_rows = df_copy.shape[0]
        deleted_rows = initial_rows - final_rows
        print(f"[SUCCESS] Erroneous & canceled transactions filtered out. Rows removed: {deleted_rows}")
        return df_copy
    except Exception as e:
        print(f"[ERROR] Exception occurred during transaction filtering: {e}")
        return df
def main():
    # Define your file path here
    data_path = "/home/exa/Documents/eda_projects/data/OnlineRetail.csv"
    print("=== DATA CLEANING PIPELINE INITIALIZED ===\n")
    # Step 1: Load
    df = load_data(data_path)
    
    if df is not None:
        # Step 2: Clean missing values and duplicates
        df = data_cleaning_pipeline(df)
        
        # Step 3: Fix data types
        df = fix_data_types(df)
        
        # Step 4: Filter anomalies/cancellations
        cleaned_df = filter_erroneous_and_canceled_transactions(df)
        
        print("\n=== PIPELINE EXECUTION COMPLETED SUCCESSFULLY ===")
        print(f"Final Cleaned Dataset Shape: {cleaned_df.shape}")
        # Optional: Save the clean dataset to a new CSV file
        cleaned_df.to_csv("OnlineRetail_Cleaned.csv", index=False)
        return cleaned_df
if __name__ == "__main__":
    main()
