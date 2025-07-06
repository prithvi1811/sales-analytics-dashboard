# Sales Analytics Dashboard 🚀

**End-to-end BI pipeline: ETL, data modeling, and interactive dashboard with real-world e-commerce sales data**

---

## 🎯 Objective

Build an end-to-end BI solution using real sales data to surface business insights via a modern dashboard.

---

## 🔧 Tools & Technologies

- **Data Source:** Kaggle E-Commerce Dataset  
- **ETL:** Python (pandas), SQL  
- **Database:** SQLite or BigQuery  
- **Dashboard:** Tableau Public / Power BI  
- **Jupyter Notebook** for scripting

---

## ✅ Pipeline Overview

### 1. Data Ingestion
- Downloaded the CSV from Kaggle.
- Loaded data into Pandas:
    ```python
    import pandas as pd
    df = pd.read_csv('data.csv', encoding='ISO-8859-1')
    ```

### 2. Data Cleaning & Transformation
- Removed nulls and duplicates.
- Fixed datatypes for `InvoiceDate`, `CustomerID`.
- Created `TotalPrice` column (`Quantity * UnitPrice`).

### 3. Data Modeling
- Designed a **Star Schema**:
    - **Fact Table:** Sales
    - **Dimension Tables:** Customer, Product, Date, Country
- Loaded data into SQLite (via `df.to_sql`) for scalable querying.

### 4. Analysis & Insights
- Performed business analysis with SQL/Pandas:
    - **Monthly revenue trends**
    - **Top 10 customers (Customer LTV)**
    - **Revenue by product and country**

### 5. Dashboard Visualization
- Built an interactive dashboard with:
    - **Revenue trend line**
    - **Customer LTV bar chart**
    - **Product/category sales pie chart**
    - **Geographic map by country**

---

## 📊 Dashboard

[🔗 View Interactive Tableau Dashboard]([PASTE-YOUR-TABLEAU-PUBLIC-LINK-HERE](https://public.tableau.com/app/profile/prithvi.chauhan3487/viz/sales-analytics-dashboard/Dashboard1))

![Dashboard 1](https://github.com/user-attachments/assets/efd7c482-ab36-4482-add9-e39fc107066b)

---

## 💡 Key Insights

- Identified peak revenue months & top regions.
- Pinpointed high-value customers for retention campaigns.
- Highlighted best-selling products and target markets.

---

## 📁 Repository Structure
