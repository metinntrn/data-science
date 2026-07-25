import streamlit as st
import pandas as pd


def create_sidebar(df):
    """
    Sidebar navigation and filters.

    Filters:
    - Department
    - Gender
    - Job Role 
    - Attrition 
    """

    # ==========================
    # Navigation
    # ==========================
    st.sidebar.title("📂 Navigation")

    page = st.sidebar.radio(
        "Go to",
        ["Overview", "Employees", "Attrition", "Insights"],
        key="navigation_radio",
        label_visibility="collapsed"
    )

    st.sidebar.divider()

    # ==========================
    # Filters
    # ==========================
    st.sidebar.title("🔍 Filters")

    # Department Filter
    departments = sorted(df["Department"].unique())
    selected_departments = st.sidebar.multiselect(
        "Department",
        options=departments,
        default=departments
    )

    # Gender Filter
    genders = sorted(df["Gender"].unique())
    selected_genders = st.sidebar.multiselect(
        "Gender",
        options=genders,
        default=genders
    )
    #Job Role  Filter
    jobs=sorted(df["JobRole"].unique())
    selected_job=st.sidebar.multiselect(
        "Job Role",
        options=jobs,
        default=jobs
    )
    #Attrition filter
    attrition=sorted(df["Attrition"].unique())
    selected_attrition=st.sidebar.multiselect(
        "Attrition",
        options=attrition,
        default=attrition
    )
    
    

    # ==========================
    # Apply Filters
    # ==========================
    filtered_df = df.copy()

    if selected_departments:
        filtered_df = filtered_df[
            filtered_df["Department"].isin(selected_departments)
        ]

    if selected_genders:
        filtered_df = filtered_df[
            filtered_df["Gender"].isin(selected_genders)
        ]
    if selected_job:
        filtered_df=filtered_df[
            filtered_df["JobRole"].isin(selected_job)
        ]
    if selected_attrition:
         filtered_df=filtered_df[
            filtered_df["Attrition"].isin(selected_attrition)
        ]   
        

    return page, filtered_df