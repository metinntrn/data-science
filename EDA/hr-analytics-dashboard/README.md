# 📊 HR Analytics Dashboard

An interactive Human Resources analytics dashboard built with **Streamlit**, **Pandas**, and **Plotly** to explore employee demographics, workforce trends, and employee attrition.

The dashboard enables HR professionals and business analysts to monitor workforce metrics, identify turnover patterns, and gain actionable insights through interactive visualizations.

---

# 🚀 Live Demo

👉 https://hr-analytic-dahsboard-metintrn.streamlit.app/

---

# 📂 Repository

https://github.com/metinntrn/data-science/tree/main/EDA

---

# 📸 Dashboard Preview


| Overview | Employees |
|----------|-----------|
| ![](images/overview.png) | ![](images/employees.png) |

| Attrition | Insights |
|-----------|----------|
| ![](images/attrition.png) | ![](images/insights.png) |

---

# ✨ Features

- Interactive dashboard built with Streamlit
- Multi-page application
- Sidebar navigation
- Dynamic filtering by:
  - Department
  - Gender
  - Job Role
  - Attrition
- Real-time KPI metrics
- Interactive Plotly visualizations
- Responsive dark theme
- Correlation analysis
- Workforce insights

---

# 📊 Dashboard Metrics

The dashboard provides key HR metrics including:

- Total Employees
- Attrition Rate
- Average Monthly Income
- Average Job Satisfaction

---

# 📈 Dashboard Pages

## 🏠 Overview

Provides a high-level summary of the workforce.

Includes:

- KPI Cards
- Employee Count by Department
- Gender Distribution
- Attrition Distribution

---

## 👥 Employee Analytics

Analyze employee demographics and compensation.

Visualizations include:

- Employee Count by Job Role
- Monthly Income by Job Role
- Age Distribution by Department

---

## 📉 Attrition Analysis

Identify employee turnover patterns.

Visualizations include:

- Attrition Rate by Department
- Attrition Rate by Job Role
- Attrition Rate by Overtime

---

## 📊 Insights & Trends

Advanced analytical visualizations.

Includes:

- Correlation Heatmap
- Monthly Income vs Years at Company
- Age vs Monthly Income

---

# 📋 Dataset

Dataset:

```
HR_Analytics.csv
```

The dataset contains employee information such as:

- Age
- Gender
- Department
- Job Role
- Monthly Income
- Years at Company
- Overtime
- Job Satisfaction
- Performance Rating
- Attrition
- Education
- Work-Life Balance
- Environment Satisfaction
- Relationship Satisfaction

---

# 🛠 Tech Stack

- Python
- Streamlit
- Pandas
- Plotly Express
- NumPy

---

# 📁 Project Structure

```
EDA/
│
├── main.py
├── requirements.txt
├── README.md
│
├── data/
│   └── HR_Analytics.csv
│
├── screens/
│   ├── overview.py
│   ├── employees.py
│   ├── attrition.py
│   └── insights.py
│
├── utils/
│   ├── paths.py
│   ├── loader.py
│   ├── sidebar.py
│   ├── kpi.py
│   ├── plots.py
│   └── formatter.py
│
└── images/
```

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/metinntrn/data-science.git
```

Navigate to the project

```bash
cd data-science/EDA
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run main.py
```

---

# 💼 Business Questions Answered

The dashboard helps answer questions such as:

- Which department has the highest employee turnover?
- Which job roles experience the highest attrition?
- Does overtime correlate with employee attrition?
- How does salary vary across different job roles?
- What is the gender distribution across departments?
- How are employee age and income related?
- Which workforce metrics have the strongest correlations?

---

# 🎯 Skills Demonstrated

This project demonstrates experience with:

- Exploratory Data Analysis (EDA)
- Interactive Dashboard Development
- Business Intelligence Reporting
- KPI Design
- HR Data Analytics
- Data Aggregation with Pandas
- Interactive Data Visualization
- Multi-page Streamlit Applications
- Deployment with Streamlit Community Cloud

---

# 🔮 Future Improvements

- Employee search functionality
- CSV and Excel export
- Predictive attrition modeling
- Salary forecasting
- Department comparison dashboard
- Time-series workforce analysis
- Authentication system

---

# 👨‍💻 Author

**Metin**

GitHub: https://github.com/metinntrn
