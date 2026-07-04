import pandas as pd
from icecream import ic as print
from tabulate import tabulate
import numpy as np

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
        print(f"Bir hata oluştu (Report): {e}")


def fix_missing_inconsistent_values(df):
    try:
        df_copy = df.copy()
        df_copy = df_copy.map(lambda x: x.casefold() if isinstance(x, str) else x)

        if "watch_time" in df_copy.columns and "video_duration" in df_copy.columns:
            df_copy["watch_time"] = np.where(
                df_copy["watch_time"] > df_copy["video_duration"], 
                df_copy["video_duration"], 
                df_copy["watch_time"]
            )

        # 3. duplicated
        df_copy = df_copy.drop_duplicates()
        
        return df_copy
    except Exception as e:
        print(f"Error in fix_missing_inconsistent_values: {e}")
        return df


def fix_mixing_dtypes(df):
    try:
        df_copy = df.copy()

        # Category row
        if "category" in df_copy.columns:
            df_copy["category"] = df_copy["category"].str.strip()
            kategori_duzeltme = {
                "gamingg": "gaming",
                "ed": "education"
            }
            df_copy["category"] = df_copy["category"].replace(kategori_duzeltme)   

        # Liked row
        if "liked" in df_copy.columns:
            liked_duzeltme = {
                "no": 0,
                "yes": 1,
                "2": np.nan,
                2: np.nan  
            }
            df_copy["liked"] = df_copy["liked"].replace(liked_duzeltme)
            df_copy["liked"] = df_copy["liked"].fillna(0).astype(int)
            
        return df_copy
    except Exception as e:
        print(f"Error in fix_mixing_dtypes: {e}")
        return df


def fix_time_Series(df):
    try:
        df_copy = df.copy()
        
        if "timestamp" in df_copy.columns:
            saniyeler = pd.to_numeric(df_copy["timestamp"], errors="coerce")
            tarih_sayisal = pd.to_datetime(saniyeler, unit="s")
            tarih_metin = pd.to_datetime(df_copy["timestamp"], format="mixed", errors="coerce")
            
            df_copy["timestamp"] = tarih_sayisal.fillna(tarih_metin)
            
        return df_copy
    except Exception as e:
        print(f"Error in fix_time_Series: {e}")
        return df


def main():
    data_path = "../data/youtube recommendation dataset.csv"
    output_md_path = "report.md"  
    
    try:
        df = pd.read_csv(data_path)
        report_to_md(df, output_md_path)
        

        df = fix_missing_inconsistent_values(df)
        df = fix_mixing_dtypes(df)
        df = fix_time_Series(df)
        ,
        df.to_csv("clean_data.csv",index=True)
        
        print("Data cleanup steps completed successfully!")
        print(f"Cleaned data size: {df.shape}")
        print("Data successfully exported")
    except FileNotFoundError:
        print(f"The file was not found in the: {data_path}")
    except Exception as e:
        print(f"General Error: {e}")


if __name__ == "__main__":
    main()
