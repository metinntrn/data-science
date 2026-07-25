import streamlit as st
import pandas as pd

from utils.plots import (
    create_jobrole_distribution,
    create_salary_by_jobrole,
    create_age_by_department,
)


def show_employees_charts(df: pd.DataFrame) -> None:
    st.subheader("Employee Analytics")

    if df.empty:
        st.warning("No data to display. Adjust your filters.")
        return

    fig = create_jobrole_distribution(df)
    st.plotly_chart(fig, use_container_width=True, key="employees_jobrole_chart")

    col1, col2 = st.columns(2)
    with col1:
        fig = create_salary_by_jobrole(df)
        st.plotly_chart(fig, use_container_width=True, key="employees_salary_chart")
    with col2:
        fig = create_age_by_department(df)
        st.plotly_chart(fig, use_container_width=True, key="employees_age_chart")
