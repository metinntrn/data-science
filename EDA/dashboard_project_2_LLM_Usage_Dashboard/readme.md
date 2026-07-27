# 🤖 LLM Usage Dashboard

An interactive data analytics dashboard built with **Streamlit**, **Plotly**, and **Pandas** to explore and analyze Large Language Model (LLM) usage data.

The dashboard provides interactive visualizations, performance metrics, filtering capabilities, and dataset exploration for understanding LLM behavior across different application domains.

## 🚀 Live Demo

👉 https://9ofhmnmp9szlys4pykdaru.streamlit.app/

---

# 📸 Dashboard Preview

> Add screenshots here

![Dashboard](images/dashboard.png)

---

# ✨ Features

- Interactive dashboard built with Streamlit
- Filter by Model Name
- Filter by Application Domain
- Real-time KPI metrics
- Interactive Plotly charts
- Explore the raw dataset
- Responsive dashboard layout
- Dark theme interface

---

# 📊 Dashboard Metrics

The dashboard calculates:

- Average User Satisfaction
- Average Response Latency
- Total Requests

---

# 📈 Visualizations

### Average Success Rate by Model

Compare successful response rates between different LLMs.

### Average User Satisfaction

Measure user satisfaction for each model.

### Usage by Application Domain

Analyze where models are used most frequently.

### Token Count vs Estimated Cost

Relationship between token usage and cost.

### Average Latency by Model

Compare response speed across models.

### RAG Enabled vs Success Rate

Analyze whether Retrieval-Augmented Generation improves success rate.

---

# 🗂 Dataset

Dataset:

```
genai_llm_usage_dataset_1000.csv
```

Contains information including:

- Model Name
- Application Domain
- Task Type
- Prompt Length
- Total Tokens
- Estimated Cost
- Temperature
- Top-p
- Latency
- User Satisfaction
- Successful Response
- Hallucination Flag
- RAG Enabled

---

# 🛠 Tech Stack

- Python
- Streamlit
- Pandas
- Plotly Express
- NumPy

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/llm-usage-dashboard.git
```

Move into the project

```bash
cd llm-usage-dashboard
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📁 Project Structure

```
llm-usage-dashboard/
│
├── app.py
├── genai_llm_usage_dataset_1000.csv
├── requirements.txt
├── README.md
└── images/
```

---

# 🎯 What I Practiced

During this project I practiced:

- Data filtering with Streamlit
- Building interactive dashboards
- Creating Plotly visualizations
- KPI calculations
- Data aggregation using Pandas
- Dashboard layout design
- Deploying Streamlit applications

---

# 🔮 Future Improvements

- Export filtered data to CSV
- More advanced analytics
- Time-series analysis
- Additional dashboard filters
- Authentication
- Model comparison page
- Mobile responsive improvements

---

# 👨‍💻 Author

Metin

GitHub:https://github.com/metinntrn
