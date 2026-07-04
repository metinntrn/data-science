# 📊 YouTube Recommendation Dataset - Data Cleaning & Profiling Pipeline

A robust, automated data science pipeline designed to profile, clean, and standardize an anomalous YouTube recommendation dataset. This project simulates a professional client-freelancer workflow, transforming raw, messy data into an analysis-ready asset while automatically generating data quality reports.

## 🚀 Key Features
- **Automated Data Profiling:** Generates comprehensive Markdown profile reports (`report.md`) detailing data types, missing numbers, and missing rates prior to cleaning.
- **Robust Outlier & Anomaly Management:** Resolves logical errors like watch times exceeding video durations using capping methods (Winsorization).
- **Type Standardization & Deduplication:** Cleans mixed-type structures, removes whitespace padding, fixes inconsistent categorical entries, and handles deduplication safely.
- **Time-Series Harmonization:** Multi-format parser that gracefully handles both standard datetime strings and raw Unix timestamps simultaneously without breaking.

---

## 🏗️ Architecture & Pipeline Flow

The pipeline executes through a sequence of modular processing functions, ensuring data integrity at each step:

1. **`report_to_md()`**: Profiles the raw dataset and exports a structured markdown table.
2. **`fix_missing_inconsistent_values()`**: Formats text cases, resolves logical bounding issues, and strips exact duplicates.
3. **`fix_mixing_dtypes()`**: Cleans categorical inconsistencies and standardizes Boolean/integer structures.
4. **`fix_time_Series()`**: Harmonizes datetime formats and multi-layered timestamps.

---

## 🧹 Data Cleaning Deep Dive

### 1. Categorical Standardization
The raw dataset contained fragmented categories due to data entry truncation and trailing whitespaces. The pipeline unifies these anomalies:

| Raw Value | Fixed Value | Reason |
| :--- | :--- | :--- |
| `gamingg` | `gaming` | Typo / Duplicate Character |
| `ed` | `education` | Data Truncation |
| `'tech '` / `' tech'` | `tech` | Hidden Trailing/Leading Whitespaces |

### 2. Boolean & Binary Resolution (`liked` Sütunu)
The `liked` column contained mixed data types (integers, strings, and system anomalies). They were mapped into a clean binary classification:
- **Positive Pool (`1`):** Converted from `1` and `yes`.
- **Negative Pool (`0`):** Converted from `0` and `no`.
- **Anomalies (`NaN` -> `0`):** Value `2` (system bugs/rapid clicks) isolated and safely imputed to `0`.

### 3. Logical Bounding (`watch_time` vs `video_duration`)
Identified rows where `watch_time > video_duration` (anomalies caused by background loops or browser tab freezes). The pipeline applies a **Capping (Winsorization)** strategy, forcing the maximum watch time to equal the video duration:

$$\text{watch\_time} = \min(\text{watch\_time}, \text{video\_duration})$$

### 4. Dual-Format Datetime Harmonization
The `timestamp` column contained a mixture of human-readable formats and raw Unix timestamps (e.g., `1744178555`). Standard parsers fail with out-of-range year exceptions. The pipeline resolves this by splitting the parsing logic:
- Numbers are isolated via `pd.to_numeric()` and parsed using `unit='s'`.
- Strings are parsed using `format='mixed'`.
- Both streams are combined using `.fillna()`.

---

## 🛠️ Tech Stack & Dependencies

- **Environment:** Linux-compatible (Optimized for Unix/Linux CLI environments)
- **Language:** Python 3.13+
- **Libraries:**
  - `pandas` (Core Data Manipulation)
  - `numpy` (Mathematical & Conditional Array Operations)
  - `icecream` (Advanced and readable debugging/logging)
  - `tabulate` (Markdown Table Formatting)

---

