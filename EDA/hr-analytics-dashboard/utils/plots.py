import plotly.express as px 
import pandas as pd 
import streamlit as st 


#overview charts
def create_department_distribution(df):
    dep_dis=(
        df["Department"]
        .value_counts()
        .reset_index())

    fig=px.bar(
    dep_dis,
        x="count",
        y="Department",
        orientation='h')
    return fig

def create_gender_distribution(df):
    gender_dist=(
        df["Gender"]
        .value_counts()
        .reset_index())
    fig=px.pie(
        gender_dist,
        values="count",
        names="Gender",
        hole=0.2)
    return fig

def create_attrition_distribution(df):
    attrition_dis=(
        df["Attrition"]
        .value_counts()
        .reset_index()
        )
    fig=px.pie(
        attrition_dis,
        values="count",
        names="Attrition",
        hole=0.3
    )
    return fig