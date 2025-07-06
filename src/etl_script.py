import pandas as pd
import sqlite3

# 1. Load Data
df = pd.read_csv('data.csv', encoding='ISO-8859-1')

# 2. Data Cleaning
df = df.dropna()
df = df.drop_duplicates()

# 3. Feature Engineering
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['CustomerID'] = df['CustomerID'].astype(int)

# 4. Time Features
df['Month'] = df['InvoiceDate'].dt.to_period('M')

# 5. Analysis

# Revenue by Country
revenue_by_country = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False)

# Monthly Revenue Trend
monthly_revenue = df.groupby('Month')['TotalPrice'].sum()

# Top 10 Customers by Revenue
top_customers = df.groupby('CustomerID')['TotalPrice'].sum().sort_values(ascending=False).head(10)

# Revenue by Product
revenue_by_product = df.groupby('StockCode')['TotalPrice'].sum().sort_values(ascending=False)

# 6. Prepare for Database and Tableau
df['InvoiceDate'] = df['InvoiceDate'].astype(str)
df['Month'] = df['Month'].astype(str)

# 7. Export Cleaned Data for Tableau
df.to_csv('clean_sales_data.csv', index=False)

# 8. (Optional) Load to SQLite for advanced querying
conn = sqlite3.connect('sales.db')
df.to_sql('Sales', conn, if_exists='replace', index=False)
conn.close()
