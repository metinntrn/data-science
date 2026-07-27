# 📊 Data Processing Pipeline

A modular Python pipeline for profiling, cleaning, and preparing raw datasets for data analysis. The project automatically generates dataset quality reports, standardizes data types, handles missing values, and prepares clean data for downstream analytics.

---

## ✨ Features

- 📄 **Automatic Dataset Profiling**
  - Total rows and columns
  - Missing value analysis
  - Missing value percentages
  - Data type summary
  - Export to Markdown report

- 🧹 **Data Cleaning Pipeline**
  - Removes records with missing `ProductName`
  - Fills missing `Brand` values with `"Generic"`
  - Fills missing `Raw_Weight` values with `"Unknown"`
  - Replaces missing `UnitPrice` values using the median

- 📅 **Automatic Date Conversion**
  - Converts the `OrderDate` column into Pandas datetime format.

- ⚠️ **Exception Handling**
  - Every pipeline step is protected using `try-except` blocks for safer execution.

- 📑 **Markdown Report Generation**
  - Automatically creates a dataset summary in `report.md`.

---

## 📂 Project Structure

```text
project/
│
├── cleaning_pipeline.py  # Main pipeline
├── report.md             # Auto-generated dataset report
├── cleaned_data.csv      # Cleaned dataset (optional)
├── README.md
└── requirements.txt
```

---

## ⚙️ Pipeline Workflow

```
Load Dataset
      │
      ▼
Generate Dataset Report
      │
      ▼
Convert Data Types
      │
      ▼
Clean Missing Values
      │
      ▼
Return Clean Dataset
```

---

## 📋 Data Cleaning Rules

| Column | Action |
|---------|--------|
| ProductName | Remove rows with missing values |
| Brand | Fill with `"Generic"` |
| Raw_Weight | Fill with `"Unknown"` |
| UnitPrice | Fill with median value |
| OrderDate | Convert to datetime |

---

## 📄 Generated Report

The pipeline automatically creates a **report.md** file containing:

- Dataset dimensions
- Missing value counts
- Missing value percentages
- Data types
- Markdown formatted summary table

Example:

```markdown
# Dataset Profile Report

Rows: 10,000

Columns: 15

| Column | Missing | Missing % |
|---------|---------|-----------|
| Brand | 25 | 0.25 |
| UnitPrice | 12 | 0.12 |
```

---

## 🛠️ Technologies

- Python 3.x
- Pandas
- IceCream
- Tabulate

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/project.git
cd project
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the pipeline

```bash
python data_cleaning.py
```

---

## 📤 Output

After execution, the project generates:

```
report.md
```

and returns the cleaned dataframe.

---

## 📌 Future Improvements

- Duplicate detection
- Outlier detection
- Data validation
- Automatic visualization
- Export cleaned data to CSV
- Logging support
- Configuration file support
- Unit testing

---

## 📄 License

This project is intended for educational and portfolio purposes.
