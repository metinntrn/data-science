import streamlit as st
import pandas as pd

from utils.plots import (
    create_department_distribution,
    create_gender_distribution,
    create_attrition_distribution,
)


def show_df(df: pd.DataFrame) -> None:
    st.subheader("Filtered Data")
    if df.empty:
        st.info("No records match the selected filters.")
        return
    st.dataframe(df, use_container_width=True, key="overview_filtered_data")


def show_overview_charts(df: pd.DataFrame) -> None:
    st.subheader("Overview Charts")

    if df.empty:
        st.warning("No data to display. Adjust your filters.")
        return

    fig = create_department_distribution(df)
    st.plotly_chart(fig, use_container_width=True, key="overview_department_chart")

    chart2, chart3 = st.columns(2)
    with chart2:
        fig = create_gender_distribution(df)
        st.plotly_chart(fig, use_container_width=True, key="overview_gender_chart")
    with chart3:
        fig = create_attrition_distribution(df)
        st.plotly_chart(fig, use_container_width=True, key="overview_attrition_chart")
