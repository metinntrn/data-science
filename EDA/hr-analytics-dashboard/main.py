import streamlit as st

from utils.loader import load_data
from utils.sidebar import create_sidebar
from utils.kpi import overview_kpi

from screens.overview import show_df, show_overview_charts
from screens.employees import show_employees_charts
from screens.attrition import show_attrition_charts
from screens.insights import show_insights_charts


st.set_page_config(
    page_title="HR Analytics Dashboard",
    page_icon="📊",
    layout="wide",
)

PAGE_RENDERERS = {
    "Overview": lambda df: (
        overview_kpi(df),
        show_overview_charts(df),
        show_df(df),
    ),
    "Employees": show_employees_charts,
    "Attrition": show_attrition_charts,
    "Insights": show_insights_charts,
}


def main():
    st.title("📊 HR Analytics Dashboard")

    df = load_data()

    page, filtered_df = create_sidebar(df)
    content = st.empty()

    with content.container():
        if filtered_df.empty:
            st.warning("No records match the selected filters. Please adjust sidebar filters.")
            return

        render_page = PAGE_RENDERERS.get(page)
        if render_page is None:
            st.error(f"Unknown page: {page}")
            return

        render_page(filtered_df)


main()
