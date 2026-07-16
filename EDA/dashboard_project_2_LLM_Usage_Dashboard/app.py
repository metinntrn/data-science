import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="LLM Usage Dashboard",
    layout="wide"
)


@st.cache_data
def load_data(data_path):
    return pd.read_csv(data_path)


def create_sidebar(df):
    st.sidebar.title("Filters")

    # Model Name
    model_options = sorted(df["model_name"].dropna().unique())
    selected_models = st.sidebar.multiselect(
        "Select Model Name",
        options=model_options
    )

    st.sidebar.divider()

    # Application Domain
    domain_options = sorted(df["application_domain"].dropna().unique())
    selected_domains = st.sidebar.multiselect(
        "Select Domain",
        options=domain_options
    )

    # Filter dataframe
    filtered_df = df.copy()

    if selected_models:
        filtered_df = filtered_df[
            filtered_df["model_name"].isin(selected_models)
        ]

    if selected_domains:
        filtered_df = filtered_df[
            filtered_df["application_domain"].isin(selected_domains)
        ]

    return filtered_df


def show_metrics(df):
    st.subheader("📊 Dashboard Metrics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Average User Satisfaction",
            f"{df['user_satisfaction'].mean():.2f}"
        )

    with col2:
        st.metric(
            "Average Latency",
            f"{df['latency_sec'].mean():.2f} sec"
        )

    with col3:
        st.metric(
            "Total Requests",
            f"{len(df)}"
        )


def plotly_chart(df):
    # ------------------ First Row ------------------

    col1, col2 = st.columns(2)

    with col1:
        success_df = (
            df.groupby("model_name", as_index=False)["successful_response"]
            .mean()
        )

        fig = px.bar(
            success_df,
            x="model_name",
            y="successful_response",
            color="model_name",
            title="Average Success Rate by Model"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        satisfaction_df = (
            df.groupby("model_name", as_index=False)["user_satisfaction"]
            .mean()
        )

        fig = px.bar(
            satisfaction_df,
            x="model_name",
            y="user_satisfaction",
            color="model_name",
            title="Average User Satisfaction by Model"
        )

        st.plotly_chart(fig, use_container_width=True)

    # ------------------ Second Row ------------------

    col1, col2 = st.columns(2)

    with col1:
        domain_df = (
            df["application_domain"]
            .value_counts()
            .reset_index()
        )

        domain_df.columns = [
            "application_domain",
            "count"
        ]

        fig = px.bar(
            domain_df,
            x="application_domain",
            y="count",
            color="application_domain",
            title="Usage by Application Domain"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.scatter(
            df,
            x="total_tokens",
            y="estimated_cost_usd",
            color="model_name",
            hover_data=["application_domain"],
            title="Token Count vs Estimated Cost"
        )

        st.plotly_chart(fig, use_container_width=True)

    # ------------------ Third Row ------------------

    col1, col2 = st.columns(2)

    with col1:
        latency_df = (
            df.groupby("model_name", as_index=False)["latency_sec"]
            .mean()
        )

        fig = px.bar(
            latency_df,
            x="model_name",
            y="latency_sec",
            color="model_name",
            title="Average Latency by Model"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        rag_df = (
            df.groupby("rag_enabled", as_index=False)["successful_response"]
            .mean()
        )

        fig = px.bar(
            rag_df,
            x="rag_enabled",
            y="successful_response",
            color="rag_enabled",
            title="Does RAG Improve Success?"
        )

        st.plotly_chart(fig, use_container_width=True)


def main():
    st.title("🤖 LLM Usage Dashboard")

    data_path = "../data/genai_llm_usage_dataset_1000.csv"

    df = load_data(data_path)

    filtered_df = create_sidebar(df)

    show_metrics(filtered_df)

    st.divider()

    plotly_chart(filtered_df)

    st.divider()

    st.subheader("Dataset")

    st.dataframe(filtered_df, use_container_width=True)


if __name__ == "__main__":
    main()
