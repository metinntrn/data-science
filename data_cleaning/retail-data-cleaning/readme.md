# 🛒 E-Commerce Data Cleaning Pipeline

A modular Python pipeline for cleaning and preprocessing raw e-commerce transaction data using **Pandas**.

The project demonstrates practical data engineering concepts such as data validation, missing value handling, duplicate removal, data type conversion, and reusable pipeline design.

---

# 🚀 Overview

Real-world e-commerce datasets often contain missing customer information, duplicate transactions, cancelled orders, and inconsistent data types.

This project automates the preprocessing workflow to transform raw transaction data into a clean, analysis-ready dataset suitable for business intelligence and machine learning tasks.

---

# ✨ Features

- Load large CSV datasets safely
- Handle missing values
- Remove duplicate records
- Standardize data types
- Filter cancelled and invalid transactions
- Modular and reusable pipeline
- Exception handling with `try-except`
- Export cleaned dataset

---

# 📊 Dataset

Dataset:

```
OnlineRetail.csv
```

Source:

https://www.kaggle.com/datasets/vijayuv/onlineretail

The dataset contains more than **540,000** e-commerce transactions from a UK-based online retailer.

### Main Columns

- Invoice Number
- Stock Code
- Product Description
- Quantity
- Invoice Date
- Unit Price
- Customer ID
- Country

> **Note:** The dataset is not included in this repository because of its size. Download it from Kaggle and place it inside the `data/` folder before running the project.

---

# ⚙️ Pipeline Workflow

The pipeline consists of four independent stages.

## 1. Load Data

- Read CSV file
- Handle ISO-8859-1 encoding
- File exception handling

---

## 2. Data Cleaning

- Remove missing `CustomerID`
- Fill missing product descriptions
- Remove duplicate rows

---

## 3. Data Type Conversion

- Convert `InvoiceDate` to `datetime`
- Convert `CustomerID` to integer

---

## 4. Transaction Validation

Remove transactions with:

- Negative Quantity
- Zero Quantity
- Negative Unit Price
- Zero Unit Price

The cleaned dataset is then exported as:

```
OnlineRetail_Cleaned.csv
```

---

# 📁 Project Structure

```text
ecommerce-data-cleaning/
│
├── data/
│   └── OnlineRetail.csv
│
├── output/
│   └── OnlineRetail_Cleaned.csv
│
├── cleaning_pipeline.py
├── requirements.txt
└── README.md
```

---

# 🛠 Tech Stack

- Python
- Pandas
- IceCream
- pathlib

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/metinntrn/data-science.git
```

Navigate to the project

```bash
cd data-science/data_cleaning/ecommerce-data-cleaning
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run

```bash
python cleaning_pipeline.py
```

---

# 📂 Output

After execution, the pipeline generates:

```
OnlineRetail_Cleaned.csv
```

The cleaned dataset is ready for:

- Exploratory Data Analysis (EDA)
- RFM Analysis
- Customer Segmentation
- Cohort Analysis
- Sales Analytics
- Machine Learning

---

# 🎯 Skills Demonstrated

This project demonstrates experience with:

- Data Cleaning
- Data Validation
- Data Preprocessing
- Pandas
- Exception Handling
- Modular Python Programming
- ETL Fundamentals
- File Handling

---

# 🔮 Future Improvements

- Logging with the `logging` module
- Unit tests using `pytest`
- Configuration file support
- Command-line interface (CLI)
- Automatic data quality reports
- Docker support

---

# 👨‍💻 Author

**Metin**

GitHub: https://github.com/metinntrn
