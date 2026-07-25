import streamlit as st

from utils.loader import load_data
from utils.sidebar import create_sidebar
from utils.kpı import overview_kpi

from screens.overview import show_df,show_overview_charts
from screens.employees import show_employees_charts
from screens.attrition import show_attrition_charts
from screens.insights import show_insights_charts


def main():
    data_path = "./data/HR_Analytics.csv"
    df = load_data(data_path)

    page, filtered_df = create_sidebar(df)

    if page == "Overview":
        st.success("Overview bloğu çalıştı")
        overview_kpi(filtered_df)
        show_overview_charts(filtered_df)
        show_df(filtered_df)

    elif page == "Employees":
        st.success("Employees bloğu çalıştı")
        show_employees_charts(filtered_df)
    elif page == "Attrition":
        st.success("Attrition bloğu çalıştı")
        show_attrition_charts(filtered_df)

    elif page == "Insights":
        st.success("Insights bloğu çalıştı")
        show_insights_charts(filtered_df)




if __name__ == "__main__":
    main()