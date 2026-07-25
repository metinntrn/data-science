import streamlit as st
import pandas as pd
from utils.plots import create_department_distribution,create_gender_distribution,create_attrition_distribution


def show_df(df: pd.DataFrame) -> None:
    st.dataframe(df, use_container_width=True)
    
def show_overview_charts(df):
    fig=create_department_distribution(df)
    st.plotly_chart(fig,use_container_width=True)
    chart2,chart3= st.columns(2)
    with chart2:
        fig=create_gender_distribution(df)
        st.plotly_chart(fig,use_container_width=True)
        
    with chart3:
       fig= create_attrition_distribution(df)
       st.plotly_chart(fig,use_container_width=True)
       