import streamlit as st
import pandas as pd

from utils.plots import (
    create_correlation_heatmap,
    create_income_vs_years,
    create_age_income,
)


def show_insights_charts(df: pd.DataFrame) -> None:
    st.subheader("Insights & Trends")

    if df.empty:
        st.warning("No data to display. Adjust your filters.")
        return

    fig = create_correlation_heatmap(df)
    st.plotly_chart(fig, use_container_width=True, key="insights_correlation_chart")

    col1, col2 = st.columns(2)
    with col1:
        fig = create_income_vs_years(df)
        st.plotly_chart(fig, use_container_width=True, key="insights_income_years_chart")
    with col2:
        fig = create_age_income(df)
        st.plotly_chart(fig, use_container_width=True, key="insights_age_income_chart")
