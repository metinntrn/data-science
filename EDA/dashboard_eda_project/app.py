import streamlit as st
import pandas as pd
import plotly.express as px


def load_data(data_path):
    """CSV dosyasını oku."""
    return pd.read_csv(data_path)


def create_sidebar(df):
    """Sidebar filtrelerini oluştur ve filtrelenmiş DataFrame döndür."""

    st.sidebar.header("Filters")

    platforms = sorted(df["Platform"].dropna().unique())
    selected_platforms = st.sidebar.multiselect(
        "Select Platform",
        options=platforms
    )

    categories = sorted(df["Product_Category"].dropna().unique())
    selected_categories = st.sidebar.multiselect(
        "Select Product Category",
        options=categories
    )

    if selected_platforms:
        df = df[df["Platform"].isin(selected_platforms)]

    if selected_categories:
        df = df[df["Product_Category"].isin(selected_categories)]

    return df


def show_metrics(df):
    col1, col2, col3 = st.columns(3)

    out_of_stock = len(df[df["Stock_Status"] == "Out of Stock"])
    in_stock = len(df[df["Stock_Status"] == "In Stock"])
    discounted = len(df[df["Discount_Pct"] > 0])

    col1.metric("Out of Stock Items", out_of_stock)
    col2.metric("In Stock Items", in_stock)
    col3.metric("Discounted Products", discounted)


def show_charts(df):
    col1, col2 = st.columns(2)

    with col1:
        discount_platform = (
            df.groupby("Platform", as_index=False)["Discount_Pct"]
            .mean()
        )

        fig = px.bar(
            discount_platform,
            x="Platform",
            y="Discount_Pct",
            title="Average Discount by Platform",
            color="Platform"
        )

        st.plotly_chart(fig,width="stretch")

    with col2:
        filter_= (
        df[df["Rating"] >= 4.0]
        .groupby("Product_Category")
        .size()
        .reset_index(name="Count"))

        fig=px.bar(filter_,x="Product_Category",y="Count",title="Products Rated 4.0+ by Category")
        st.plotly_chart(fig,width="stretch")
    col1, col2 = st.columns(2)
    with col1:
        stoc_st=pd.DataFrame(df["Stock_Status"].value_counts()).reset_index()
        fig=px.pie(stoc_st,
        names="Stock_Status",
        values="count",
        hole=0.3,
        title="Stock Status")
        st.plotly_chart(fig,width="stretch")
        


def main():
    st.set_page_config(
        page_title="Sales Dashboard",
        page_icon="📊",
        layout="wide"
    )

    st.title("📊 Sales Dashboard")

    data_path = "cleaned_data.csv"

    df = load_data(data_path)

    df = create_sidebar(df)

    show_metrics(df)

    show_charts(df)

    st.subheader("Dataset")
    st.dataframe(df, use_container_width=True)


if __name__ == "__main__":
    main()
