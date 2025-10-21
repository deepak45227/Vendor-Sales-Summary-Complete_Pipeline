# 🧾 Vendor Sales Summary Project

## 📌 Overview
The **Vendor Sales Summary Project** automates the entire process of creating database, extracting, transforming, analyzing, and visualizing vendor sales data.  
It creates a seamless **ETL (Extract–Transform–Load)** pipeline using **Python** and **SQL**, performs **data cleaning and summarization**, and finally delivers insights through **EDA and Power BI dashboards**.

---

## 🚀 Key Features

- **Automated Data Ingestion:**  
  - `ingestion.py`connects to the SQL Server using sqlalchemy and automated tables creating and export all the  data in respected tables .
  -  write a python script  that iterate over the files create table with respectes names and export all the data send data in chunks for large files  .
  - (sales table is approx 1.3 gb in size so used sql inline method for fast process)
  - Handles large datasets and ensures data consistency during import.

- **Data Transformation & Integration:**  
  - Cleans and merges multiple tables into a single, standardized dataset.
  - Implements the `get_vendor_summary()` function to create a consolidated vendor performance table.
  - Saves the cleaned and summarized data back into SQL for future use.

- **Exploratory Data Analysis (EDA):**  
  - Conducted in Jupyter Notebook using Pandas, Matplotlib, and Seaborn.
  - Includes insights such as top-performing vendors, sales trends, and seasonal sales behavior.

- **Business Intelligence Dashboard:**  
  - Power BI dashboard visualizes vendor sales KPIs:
    - Total Sales by Vendor  
    - Quantity Sold  
    - Average Order Value  
    - Revenue Trends  
  - Enables stakeholders to make data-driven business decisions quickly.

---

## 🧰 Tech Stack
| Category | Tools & Technologies |
|-----------|---------------------|
| Programming | Python (Pandas, SQLAlchemy) |
| Database | SQL |
| Analysis | Jupyter Notebook |
| Visualization | Power BI |
| Other | Data Cleaning, ETL Automation, Data Aggregation |

---

## 📂 Project Structure
Vendor-Sales-Summary/
│
├── ingestion.py # Script for data extraction and ingestion from SQL
├── get_vendor_summary.py # Function to aggregate and summarize vendor data
├── notebooks/
│ └── vendor_eda.ipynb # Jupyter notebook for exploratory data analysis
├── powerbi_dashboard/ # Power BI report files (.pbix)
├── data/
│ └── 
├── requirements.txt # List of Python dependencies
└── README.md # Project documentation
|__vrndor-sales-summary-report.pdf
