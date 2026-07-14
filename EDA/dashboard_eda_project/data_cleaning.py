from pathlib import Path
import pandas as pd
from icecream import ic

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        ic("Data successfully loaded.")
        return df
    except FileNotFoundError as e:
        ic(f"File not found error: {e}")
        return None

def convert_date_time(df):
    try:
        df["Date"] = pd.to_datetime(df["Date"])
        ic("Date column converted to datetime format.")
        return df
    except Exception as e:
        ic(f"Date conversion error: {e}")
        return df

def handle_missing_values(df):
    try:
        df["Sale_Event"] = df["Sale_Event"].fillna("Regular Day")
        ic("Missing values in 'Sale_Event' filled with 'Regular Day'.")
        return df
    except Exception as e:
        ic(f"Missing value handling error: {e}")
        return df

def remove_outliers(df):
    try:
        target_column = 'Discount_Pct'
        Q1 = df[target_column].quantile(0.25)
        Q3 = df[target_column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df_clean = df[(df[target_column] >= lower_bound) & (df[target_column] <= upper_bound)]
        df.drop("Unnamed",inplace=True)
        ic(f"Original Row Count: {len(df)}")
        ic(f"Cleaned Row Count: {len(df_clean)}")
        ic(f"Removed Outliers: {len(df) - len(df_clean)}")
        return df_clean  
    except Exception as e:
        ic(f"Outlier removal error: {e}")
        return df

def main():
    try:
        BASE_DIR = Path(__file__).resolve().parent
        csv_path = BASE_DIR / ".." / "data" / "apple_products_pricing_2020_2026.csv"
        ic(f"Target file path: {csv_path}")
        
        if csv_path.exists():
            df = load_data(csv_path)
            if df is not None:
                df = convert_date_time(df)
                df = handle_missing_values(df)
                df_final = remove_outliers(df)
                ic("Data pipeline completed successfully.")
                df_final.to_csv("cleaned_data.csv",index=True)
        else:
            ic("Data path error: File does not exist at the specified path.")
    except Exception as e:
        ic(f"Unexpected error in main: {e}")

if __name__ == "__main__":
    main()
