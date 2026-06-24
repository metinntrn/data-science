import pandas as pd
from icecream import ic as print
from tabulate import tabulate

def report_to_md(df, output_md_path):
    try:
        md_content = f"# 📊 Dataset Profile Report\n\n"
        md_content += f"- **Total Number of Rows:** {df.shape[0]}\n"
        md_content += f"- **Total Number of Columns:** {df.shape[1]}\n\n"
        md_content += "--- \n\n"
        md_content += "## 🔍 Column Analysis Details (Horizontal View)\n\n"
        
        ozet_df = pd.DataFrame({
            "Veri Tipi (dtypes)": df.dtypes.astype(str),
            "Missing Data": df.isnull().sum(),
            "Missing Data Rate (%)": ((df.isnull().sum() / len(df)) * 100).round(2)
        })
        
        ozet_df_yan = ozet_df.T
        tablo_markdown = ozet_df_yan.to_markdown(index=True)
        
        md_content += tablo_markdown
        md_content += "\n\n---\n*Note: This report is auto-generated using Python Pandas.*"
        
        with open(output_md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
            
        print(f"Report successfully exported with the name '{output_md_path}'!")
        
    except Exception as e:
        print(f"Error (Report): {e}")
        return None

def data_type_conver(df):
    try:
        if "OrderDate" in df.columns:
            df["OrderDate"] = pd.to_datetime(df["OrderDate"])
            print("Date conversion done!")
        else:
            print("⚠️ 'OrderDate' column not found!")
        return df
    except Exception as e:
        print(f"❌ Date Error: {e}")
        return df

def data_cleaning_pipeline(df):
    try:
        df = df.copy()
        df = df.dropna(subset=["ProductName"])
        
        df["Brand"] = df["Brand"].fillna("Generic")
        df["Raw_Weight"] = df["Raw_Weight"].fillna("Unknown")
        
        if "UnitPrice" in df.columns:
            df["UnitPrice"] = df["UnitPrice"].fillna(df["UnitPrice"].median())
        
        print("Data cleaning done!")
        return df
    except Exception as e:
        print(f"❌ Cleaning Error: {e}")
        return df

def main():
    data_path = "../data/online_retail_real_world.csv"
    output_md_path = "./report.md" 
    
    try:
        df = pd.read_csv(data_path)
        print("Data loaded successfully.")
        
        report_to_md(df, output_md_path)
        
        df = data_type_conver(df)
        df_cleaned = data_cleaning_pipeline(df)
        
    except FileNotFoundError:
        print(f"❌ Error: No data set found at '{data_path}'!")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    main()
