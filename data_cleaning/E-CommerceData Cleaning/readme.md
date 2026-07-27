# 🛒 E-Commerce Data Cleaning Pipeline

A modular Python data cleaning pipeline built with **Pandas** for preparing raw e-commerce transaction data for analytics and machine learning workflows.

The project demonstrates practical data preprocessing techniques including missing value handling, duplicate removal, data type conversion, transaction validation, and reusable pipeline design.

---

# 🚀 Overview

Real-world transactional datasets often contain:

- Missing customer information
- Duplicate records
- Invalid transactions
- Product returns
- Cancelled orders
- Incorrect data types

This project transforms raw transaction logs into a clean and analysis-ready dataset suitable for business intelligence and data science applications.

---

# 📊 Dataset

Dataset:

```
OnlineRetail.csv
```

Source:

https://www.kaggle.com/datasets/vijayuv/onlineretail

Dataset contains over **540,000** e-commerce transactions from a UK-based online retailer.

Main columns include:

- Invoice Number
- Product Description
- Quantity
- Unit Price
- Customer ID
- Invoice Date
- Country

---

# ⚙️ Pipeline Workflow

The pipeline consists of four modular stages.

### 1. Load Data

- Reads CSV safely
- Handles ISO-8859-1 encoding
- Exception handling

### 2. Data Cleaning

- Remove missing Customer IDs
- Fill missing product descriptions
- Remove duplicate rows

### 3. Data Type Conversion

- Convert InvoiceDate to datetime
- Convert CustomerID to integer

### 4. Transaction Validation

Remove:

- Negative quantities
- Zero quantities
- Negative prices
- Cancelled transactions

---

# 📈 Output

The pipeline generates a cleaned dataset ready for:

- Exploratory Data Analysis (EDA)
- Customer Segmentation (RFM)
- Sales Analytics
- Cohort Analysis
- Recommendation Systems
- Machine Learning

---

# 🛠 Technologies

- Python
- Pandas
- IceCream
- pathlib

---

# 📁 Project Structure

```
ecommerce-cleaning/
│
├── main.py
├── requirements.txt
├── README.md
│
├── data/
│   └── OnlineRetail.csv
│
└── output/
    └── OnlineRetail_Cleaned.csv
```

---

# ▶️ Installation

```bash
git clone https://github.com/yourusername/ecommerce-cleaning.git

cd ecommerce-cleaning

pip install -r requirements.txt

python main.py
```

---

# 🎯 Skills Demonstrated

This project demonstrates experience with:

- Data Cleaning
- Data Validation
- Exception Handling
- Modular Python Design
- Pandas
- Data Preprocessing
- ETL Fundamentals

---

# 🔮 Future Improvements

- Logging module
- Unit tests
- Configuration file
- CLI interface
- Docker support
- Automatic report generation
- Data quality report

---

# 👨‍💻 Author

Metin
