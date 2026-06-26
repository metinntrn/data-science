# Data Processing Pipeline

This project is a Python-based automation tool designed to analyze raw datasets, generate automated reports, and perform essential data cleaning tasks. It is optimized to streamline data preprocessing workflows and provide quick insights into data quality.

## Features

- **Automated Markdown Reporting:** Automatically generates a report.md file containing row/column counts and a detailed missing data analysis (including data types and percentages).

- **Automated Data Type Conversion:** Detects the OrderDate column and automatically converts it to the datetime format.

 - **Data Cleaning Pipeline:**

      * Drops rows with missing ProductName entries.

      *  Imputes missing Brand and Raw_Weight values with placeholders ("Generic" and "Unknown").

      *  Imputes missing UnitPrice values using the column median to maintain statistical integrity.

## Installation
🛠 Dependencies

This project requires the following libraries:

 *  **pandas:** Data manipulation and analysis.
  
 *   **icecream:** For structured and readable console debugging.
  
 *    **tabulate:** To format data frames into clean Markdown tables.

You can install them via pip:
```bash
pip install pandas icecream tabulate
