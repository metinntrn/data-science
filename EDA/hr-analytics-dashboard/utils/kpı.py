import streamlit as st
import pandas as pd

from utils.formater import format_currency


def overview_kpi(df: pd.DataFrame) -> None:
    """Overview KPI cards."""

    total_employees = df["EmpID"].nunique()
    attrition_rate = (df["Attrition"] == "Yes").mean() * 100
    avg_income = df["MonthlyIncome"].mean()
    avg_job_satisfaction = df["JobSatisfaction"].mean()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "👥 Total Employees",
            f"{total_employees:,}"
        )

    with col2:
        st.metric(
            "🚪 Attrition Rate",
            f"{attrition_rate:.2f}%"
        )

    with col3:
        st.metric(
            "💰 Average Monthly Income",
            format_currency(avg_income)
        )

    with col4:
        st.metric(
            "😊 Average Job Satisfaction",
            f"{avg_job_satisfaction:.2f}"
        )