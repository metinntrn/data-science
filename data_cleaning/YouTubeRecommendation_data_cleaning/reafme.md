# 📊 YouTube Recommendation Dataset - Data Cleaning & Profiling Pipeline

A modular Python pipeline for profiling, cleaning, and standardizing a noisy YouTube recommendation dataset. The project demonstrates practical data preprocessing techniques used in real-world data science workflows, automatically transforming inconsistent raw data into a clean, analysis-ready dataset.

---

## 🚀 Overview

Real-world datasets rarely come clean. They often include:

- Missing values
- Duplicate records
- Inconsistent categorical labels
- Mixed data types
- Invalid timestamps
- Logical anomalies

This project automates the entire preprocessing workflow while generating a detailed Markdown profiling report before any modifications are applied.

The cleaned dataset is suitable for:

- 📈 Exploratory Data Analysis (EDA)
- 🤖 Machine Learning
- 🎯 Recommendation Systems
- 📊 Business Intelligence
- 🧹 Feature Engineering

---

# ✨ Features

- 📄 Automatic dataset profiling
- 📊 Markdown report generation
- 🧹 Missing value analysis
- 🔄 Duplicate removal
- 🏷️ Category standardization
- ⏱ Mixed datetime parsing
- 📉 Outlier correction
- ⚠️ Robust exception handling
- 🧩 Modular pipeline architecture

---

# 🏗 Pipeline Workflow

```
Raw Dataset
      │
      ▼
Dataset Profiling
(report.md)
      │
      ▼
Fix Missing & Inconsistent Values
      │
      ▼
Standardize Categories
      │
      ▼
Fix Mixed Data Types
      │
      ▼
Parse Mixed Timestamp Formats
      │
      ▼
Export Clean Dataset
(clean_data.csv)
```

---

# 🔍 Pipeline Stages

## 1. Dataset Profiling

Before cleaning begins, the pipeline generates an automatic Markdown report containing:

- Total rows
- Total columns
- Data types
- Missing values
- Missing percentages

Output:

```
report.md
```

---

## 2. Missing & Inconsistent Value Handling

The pipeline first creates a copy of the dataset before applying transformations.

Operations include:

- Convert every string to lowercase using `casefold()`
- Remove duplicate rows
- Correct logical inconsistencies

Example:

```
watch_time > video_duration
```

is automatically corrected as

```
watch_time = video_duration
```

using NumPy's vectorized `where()` function.

---

## 3. Category Standardization

The pipeline removes unwanted whitespace and fixes inconsistent category labels.

Example

| Original | Cleaned |
|-----------|----------|
| gamingg | gaming |
| ed | education |
| tech | tech |

---

## 4. Mixed Data Type Resolution

The **liked** column contains multiple data representations.

Original values

```
yes
no
1
0
2
NaN
```

are standardized into binary integers.

| Raw | Output |
|------|--------|
| yes | 1 |
| no | 0 |
| 1 | 1 |
| 0 | 0 |
| 2 | 0 |
| NaN | 0 |

---

## 5. Time Series Harmonization

The timestamp column contains both

- Unix timestamps
- Standard datetime strings

The pipeline detects both formats automatically.

Processing strategy:

- Numeric values → `pd.to_datetime(..., unit="s")`
- Text values → `pd.to_datetime(..., format="mixed")`
- Merge both results into a single datetime column.

---

# 📄 Generated Files

The project automatically generates:

```
report.md
```

Dataset profiling report.

```
clean_data.csv
```

Fully cleaned dataset.

---

# 📂 Project Structure

```
project/
│
├── README.md
├── main.py
├── report.md
├── clean_data.csv
└── data/
    └── youtube recommendation dataset.csv
```

---

# 📊 Dataset

**Dataset:** YouTube Recommendation Dataset

The dataset contains user interaction information collected from a simulated YouTube recommendation platform.

Main columns include:

- category
- liked
- watch_time
- video_duration
- timestamp

Dataset Source:

https://www.kaggle.com/datasets/iitanshravan/youtube-recommendation-data-for-cleaning-and-ml

---

# 🛠 Technologies

- Python 3.13+
- Pandas
- NumPy
- IceCream
- Tabulate

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/metinntrn/data-science.git
```

Go to the project directory

```bash
cd data_cleaning/project_name
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run

```bash
python main.py
```

Outputs:

```
report.md
clean_data.csv
```

---

# 📚 Skills Demonstrated

- Data Cleaning
- Data Profiling
- Data Validation
- Time Series Processing
- Data Type Standardization
- Outlier Detection
- Markdown Report Generation
- Exception Handling
- Modular Python Programming
- Pandas
- NumPy

---

## 📜 License

This project is intended for educational and portfolio purposes.
