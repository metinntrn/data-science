# 📱 Apple Products Pricing Dashboard

Interactive Streamlit dashboard analyzing Apple product pricing strategies from 2020-2026.

## 🎯 Overview

This project provides a comprehensive analysis of Apple's pricing strategy across different product categories (iPhone, Mac, iPad, AirPods, etc.) over a 6-year period. Includes stock status tracking, discount analysis, and customer ratings.

## ✨ Features

- 📊 **Real-time Filters** - Filter by platform, category, and stock status
- 💰 **Discount Analysis** - Track pricing reductions across products
- 📈 **Stock Monitoring** - Visualize in-stock vs out-of-stock items
- ⭐ **Rating Insights** - Customer satisfaction analysis
- 🎨 **Interactive Charts** - Hover, zoom, and explore data
- 📱 **Responsive Design** - Works on desktop and mobile

## 📊 Dashboard Components

### Metrics Section
- **Out of Stock Items** - Count of unavailable products
- **In Stock Items** - Count of available products
- **Discounted Products** - Number of products with price reductions

### Charts
1. **Average Discount by Platform** - Bar chart showing discount percentages by platform
2. **Category Comparison** - Bar chart of average prices by product category
3. **Stock Status** - Pie chart showing stock distribution

## 📋 Dataset

**Source:** Apple Products Pricing Dataset (2020-2026)

**Columns:**
- `Date` - Date of record
- `Platform` - Sales platform (e.g., Apple Store, Amazon, etc.)
- `Product_Category` - Category (iPhone, Mac, iPad, AirPods, etc.)
- `Condition` - Product condition (New, Refurbished, Open Box)
- `Launch_Price_USD` - Original launch price
- `Current_Price_USD` - Current selling price
- `Discount_Pct` - Discount percentage
- `Sale_Event` - Promotional event (if any)
- `Stock_Status` - In Stock / Out of Stock
- `Rating` - Customer rating (1-5 stars)
- `Reviews_Count` - Number of customer reviews

**Size:** 1,000+ products

## 🛠️ Technologies

- **Python 3.9+**
- **Streamlit** - Web framework
- **Plotly** - Interactive visualizations
- **Pandas** - Data manipulation
- **pathlib** - File path handling

