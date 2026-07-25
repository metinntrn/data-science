import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def _empty_figure(message: str = "No data available for the selected filters."):
    fig = go.Figure()
    fig.add_annotation(
        text=message,
        xref="paper",
        yref="paper",
        x=0.5,
        y=0.5,
        showarrow=False,
        font={"size": 16},
    )
    fig.update_layout(
        xaxis={"visible": False},
        yaxis={"visible": False},
        margin={"t": 40, "b": 40, "l": 40, "r": 40},
    )
    return fig


def _is_empty(df: pd.DataFrame) -> bool:
    return df is None or df.empty


# Overview charts
def create_department_distribution(df):
    if _is_empty(df):
        return _empty_figure()

    dep_dis = df["Department"].value_counts().reset_index()
    fig = px.bar(
        dep_dis,
        x="count",
        y="Department",
        orientation="h",
        title="Employee Count by Department",
        labels={"count": "Employees", "Department": "Department"},
    )
    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    return fig


def create_gender_distribution(df):
    if _is_empty(df):
        return _empty_figure()

    gender_dist = df["Gender"].value_counts().reset_index()
    fig = px.pie(
        gender_dist,
        values="count",
        names="Gender",
        hole=0.2,
        title="Gender Distribution",
    )
    return fig


def create_attrition_distribution(df):
    if _is_empty(df):
        return _empty_figure()

    attrition_dis = df["Attrition"].value_counts().reset_index()
    fig = px.pie(
        attrition_dis,
        values="count",
        names="Attrition",
        hole=0.3,
        title="Attrition Distribution",
        color="Attrition",
        color_discrete_map={"Yes": "#ef553b", "No": "#636efa"},
    )
    return fig


# Employees
def create_jobrole_distribution(df):
    if _is_empty(df):
        return _empty_figure()

    role_dist = df["JobRole"].value_counts().reset_index()
    fig = px.bar(
        role_dist,
        x="count",
        y="JobRole",
        orientation="h",
        title="Employee Count by Job Role",
        labels={"count": "Employees", "JobRole": "Job Role"},
    )
    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    return fig


def create_salary_by_jobrole(df):
    if _is_empty(df):
        return _empty_figure()

    fig = px.box(
        df,
        x="JobRole",
        y="MonthlyIncome",
        title="Monthly Income by Job Role",
        labels={"JobRole": "Job Role", "MonthlyIncome": "Monthly Income ($)"},
        color="JobRole",
    )
    fig.update_layout(showlegend=False, xaxis={"tickangle": -45})
    return fig


def create_age_by_department(df):
    if _is_empty(df):
        return _empty_figure()

    fig = px.box(
        df,
        x="Department",
        y="Age",
        title="Age Distribution by Department",
        labels={"Department": "Department", "Age": "Age"},
        color="Department",
    )
    fig.update_layout(showlegend=False, xaxis={"tickangle": -20})
    return fig


# Attrition
def create_attrition_department(df):
    if _is_empty(df):
        return _empty_figure()

    attrition_rate = (
        df.groupby("Department", as_index=False)["Attrition"]
        .apply(lambda s: (s == "Yes").mean() * 100)
        .rename(columns={"Attrition": "Attrition Rate (%)"})
    )
    fig = px.bar(
        attrition_rate,
        x="Department",
        y="Attrition Rate (%)",
        title="Attrition Rate by Department",
        labels={"Department": "Department"},
        color="Attrition Rate (%)",
        color_continuous_scale="Reds",
    )
    fig.update_layout(showlegend=False, xaxis={"tickangle": -20})
    return fig


def create_attrition_jobrole(df):
    if _is_empty(df):
        return _empty_figure()

    attrition_rate = (
        df.groupby("JobRole", as_index=False)["Attrition"]
        .apply(lambda s: (s == "Yes").mean() * 100)
        .rename(columns={"Attrition": "Attrition Rate (%)"})
    )
    fig = px.bar(
        attrition_rate,
        x="JobRole",
        y="Attrition Rate (%)",
        title="Attrition Rate by Job Role",
        labels={"JobRole": "Job Role"},
        color="Attrition Rate (%)",
        color_continuous_scale="Oranges",
    )
    fig.update_layout(showlegend=False, xaxis={"tickangle": -45})
    return fig


def create_attrition_overtime(df):
    if _is_empty(df):
        return _empty_figure()

    attrition_rate = (
        df.groupby("OverTime", as_index=False)["Attrition"]
        .apply(lambda s: (s == "Yes").mean() * 100)
        .rename(columns={"Attrition": "Attrition Rate (%)"})
    )
    fig = px.bar(
        attrition_rate,
        x="OverTime",
        y="Attrition Rate (%)",
        title="Attrition Rate by Overtime",
        labels={"OverTime": "Overtime"},
        color="OverTime",
        color_discrete_map={"Yes": "#ef553b", "No": "#636efa"},
    )
    fig.update_layout(showlegend=False)
    return fig


# Insights
def create_correlation_heatmap(df):
    if _is_empty(df):
        return _empty_figure()

    numeric_cols = df.select_dtypes(include="number").columns
    if len(numeric_cols) < 2:
        return _empty_figure("Not enough numeric columns for correlation.")

    corr = df[numeric_cols].corr(numeric_only=True)
    fig = px.imshow(
        corr,
        text_auto=".2f",
        aspect="auto",
        title="Correlation Heatmap (Numeric Features)",
        color_continuous_scale="RdBu_r",
        zmin=-1,
        zmax=1,
    )
    return fig


def create_income_vs_years(df):
    if _is_empty(df):
        return _empty_figure()

    fig = px.scatter(
        df,
        x="YearsAtCompany",
        y="MonthlyIncome",
        color="Attrition",
        title="Monthly Income vs Years at Company",
        labels={
            "YearsAtCompany": "Years at Company",
            "MonthlyIncome": "Monthly Income ($)",
            "Attrition": "Attrition",
        },
        opacity=0.7,
        color_discrete_map={"Yes": "#ef553b", "No": "#636efa"},
    )
    return fig


def create_age_income(df):
    if _is_empty(df):
        return _empty_figure()

    fig = px.scatter(
        df,
        x="Age",
        y="MonthlyIncome",
        color="Department",
        title="Age vs Monthly Income",
        labels={"Age": "Age", "MonthlyIncome": "Monthly Income ($)"},
        opacity=0.7,
    )
    return fig
