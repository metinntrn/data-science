# HR Analytics Dashboard

Interactive HR analytics dashboard built with Streamlit and Plotly.

Repository: [data-science/EDA](https://github.com/metinntrn/data-science/tree/main/EDA)


**App Link**:https://hr-analytic-dahsboard-metintrn.streamlit.app/

## Project Structure

```
EDA/
├── main.py                 # App entry point
├── requirements.txt
├── data/
│   └── HR_Analytics.csv    # Dataset
├── screens/
│   ├── overview.py
│   ├── employees.py
│   ├── attrition.py
│   └── insights.py
└── utils/
    ├── paths.py            # Project paths (GitHub-safe)
    ├── loader.py
    ├── sidebar.py
    ├── kpi.py
    ├── plots.py
    └── formater.py
```

## Setup

```bash
git clone https://github.com/data-science/EDA.git
cd EDA

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

## Run

```bash
streamlit run main.py
```

Open `http://localhost:8501` in your browser.

## Pages

| Page | Content |
|------|---------|
| Overview | KPI cards, department/gender/attrition charts, filtered data table |
| Employees | Job role distribution, salary and age analysis |
| Attrition | Attrition rates by department, role, and overtime |
| Insights | Correlation heatmap, income vs tenure, age vs income |

## Notes

- Data paths are resolved from the project root via `utils/paths.py`.
- Use `streamlit run main.py` — do not run with `python main.py`.
