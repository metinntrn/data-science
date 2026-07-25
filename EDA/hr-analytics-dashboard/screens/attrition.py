import streamlit as st
import pandas as pd

from utils.plots import (
    create_attrition_department,
    create_attrition_jobrole,
    create_attrition_overtime,
)


def show_attrition_charts(df: pd.DataFrame) -> None:
    st.subheader("Attrition Analysis")

    if df.empty:
        st.warning("No data to display. Adjust your filters.")
        return

    fig = create_attrition_department(df)
    st.plotly_chart(fig, use_container_width=True, key="attrition_department_chart")

    col1, col2 = st.columns(2)
    with col1:
        fig = create_attrition_jobrole(df)
        st.plotly_chart(fig, use_container_width=True, key="attrition_jobrole_chart")
    with col2:
        fig = create_attrition_overtime(df)
        st.plotly_chart(fig, use_container_width=True, key="attrition_overtime_chart")
