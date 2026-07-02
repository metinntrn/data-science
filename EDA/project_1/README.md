# Video Game Sales Exploratory Data Analysis (EDA)

This project performs an Exploratory Data Analysis (EDA) on historical video game sales records to uncover industry growth patterns, platform dominance, genre distributions, and regional market behaviors. 

## 📊 Project Overview

Using Python, Pandas, and interactive Plotly visualizations, this data analysis inspects over 16,500 video games. The primary goal is to extract meaningful insights from historical sales data, evaluate the golden eras of gaming, and explore regional cultural preferences (e.g., analyzing titles that were massive hits in North America but underperformed in Japan).

## 📂 Dataset

The notebook utilizes the `vgsales.csv` dataset located under the `./data/` directory. It tracks video games with sales exceeding 100,000 copies.

**Features included:**
- `Rank`: Overall sales ranking.
- `Name`: The game's title.
- `Platform`: Release console (e.g., Wii, PS2, X360, NES).
- `Year`: Year of the game's release.
- `Genre`: Game category (Sports, Action, Shooter, Platform, etc.).
- `Publisher`: Game publisher (Nintendo, Electronic Arts, etc.).
- `NA_Sales` / `EU_Sales` / `JP_Sales` / `Other_Sales`: Regional sales performance (in millions).
- `Global_Sales`: Total worldwide sales (in millions).

## 🔍 Core Analyses Implemented

1. **Historical Global Sales Trends:** Aggregating worldwide sales by year using an interactive line chart to determine industry peaks and growth milestones over decades.
2. **Platform & Genre Distributions:** A comprehensive matrix of sales mapped across platforms and genres to observe which consoles dominated specific categories.
3. **Regional Mismatch & Cultural Dynamics (Hit vs. Flop):** Evaluating cultural preferences by isolating titles that achieved high volume in the West but minimal traction in Japan. This is measured via mathematical sales differences and joint logical filtering, displayed clearly in grouped bar charts.

## 🛠️ Tech Stack & Libraries

- **Programming Language:** Python 3.x
- **Data Manipulation:** `pandas`
- **Interactive Visualizations:** `plotly.express`
