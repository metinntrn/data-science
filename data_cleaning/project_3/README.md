# 🛒 E-Commerce Data Cleaning Pipeline (Online Retail)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data_Engineering-red.svg)
![Status](https://img.shields.io/badge/Status-Production_Ready-success.svg)

A production-ready, modular Python pipeline designed to clean, transform, and optimize transactional e-commerce data. This project demonstrates industry-standard data engineering practices, including modular function design, exception handling with `try-except` blocks, and automated data logging.

## 💡 Business Value & Impact

Raw e-commerce data is often plagued with missing customer profiles, systemic duplicate logs, and hidden cancellation records that severely distort revenue calculations. This pipeline transforms messy transactional logs into a pristine dataset perfectly optimized for downstream analytics, such as:
* **RFM (Recency, Frequency, Monetary) Segmentation**
* **Accurate Cohort & Revenue Analysis**
* **Market Basket Analysis (Recommendation Engines)**

---

## 📊 Dataset Information

The dataset used in this project is the famous **Online Retail Dataset**, which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail company. 

### Quick Data Dictionary:
* `InvoiceNo`: Unique invoice number. (*Nominal, 6-digit. 'C' indicates cancellation*)
* `StockCode`: Unique product item code.
* `Quantity`: The quantities of each product per transaction.
* `UnitPrice`: Product price per unit in sterling (£).
* `CustomerID`: Unique 5-digit customer identifier.

* **Source:** [Kaggle - Online Retail Dataset](https://www.kaggle.com/datasets/vijayuv/onlineretail)
* **Format:** CSV (Comma-Separated Values)
* **Size:** ~45 MB (Over 540,000 transaction rows)

> ⚠️ **Note on Dataset Availability:** Due to GitHub's file size limitations and standard data repository best practices, the raw dataset file (`OnlineRetail.csv`) is **not uploaded** to this repository. To run this project locally, please download the dataset from the link above and place it into your local `./data` directory.
kaggle data link : https://www.kaggle.com/datasets/vijayuv/onlineretail
---

## 🛠️ Pipeline Architecture

The script handles the raw, messy real-world data through a 4-stage pipeline orchestrated by a central execution unit. Every stage focuses on a specific data integrity problem:

1. **`load_data`**: Dynamically reads the dataset using `ISO-8859-1` encoding to securely process special currency symbols without throwing codec errors.
2. **`data_cleaning_pipeline`**: 
   * Strips out rows with missing `CustomerID` labels to prevent corrupted customer profile analyses.
   * Fills missing product descriptions with standard placeholders (`UNKNOWN ITEM`).
   * Detects and removes completely duplicated rows caused by database double-logging to prevent artificial revenue inflation.
3. **`fix_data_types`**: Parses string-based transactional timestamps into native Pandas `datetime64` formats, making the data ready for time-series and trend modeling.
4. **`filter_erroneous_and_canceled_transactions`**: Isolates actual, successful commercial sales by weeding out negative or zero-value entries in `Quantity` and `UnitPrice` (which represent product returns, order cancellations, or bad debt accounting adjustments).
