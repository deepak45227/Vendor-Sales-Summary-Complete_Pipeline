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
├── ingestion_db.py # Python script for fetching and loading raw data from SQL
├── get_vendor_summery.py # Builds summarized vendor sales table and saves back to SQL
│
├── notebooks/
│ ├── Exploratory_data_analysis.ipynb # EDA on cleaned vendor sales data
│ ├── vendor_performance_analysis.ipynb # In-depth vendor performance visualization & metrics
│ └── Untitled.ipynb # Temporary or test notebook
│
├── data/
│ ├── begin_inventory.csv # Opening stock for each product/vendor
│ ├── end_inventory.csv # Closing stock for each product/vendor
│ ├── sales.csv # Sales transactions with vendor and product details
│ ├── vendor_invoice.csv # Vendor invoice and payment details
│ ├── purchase_price.csv # Purchase price per product/vendor
│ └── purchases.csv # Vendor purchase records
│
├── vensor-sales.pbix # Power BI dashboard visualizing vendor summary insights
├── Vendor-Sales-Summeryreport.pdf # Final project report and analysis summary
├── gradient-abstract-wireframe-background.jpg # Dashboard/Report background image
└── README.md # Project documentation (this file)



---

## ⚙️ How It Works
1. **Run `ingestion.py`** to fetch raw data from SQL and perform basic cleaning.  
2. **Execute `get_vendor_summary()`** to build the final summary table and store it back in SQL.  
3. **Open `vendor_eda.ipynb`** to explore and analyze key sales trends.  
4. **Load the processed data in Power BI** to visualize and generate the Vendor Sales Summary Dashboard.

---

## 📊 Results
- Automated the vendor data pipeline and eliminated manual aggregation.
- Improved accuracy and speed of generating sales reports.
- Delivered interactive dashboards for real-time sales monitoring and vendor performance evaluation.

---

## 💡 Future Enhancements
- Integrate scheduling with **Airflow or Cron** for periodic data refresh.  
- Add **real-time dashboard updates** using APIs.  
- Incorporate **forecasting models** for vendor sales prediction.

---

## 👨‍💻 Author
**Dee Y**  
_Data Analyst & Developer passionate about building intelligent, automated data systems._  
📧 deepak045227@gmail.com

---

## 🪪 License
This project is released under the MIT License. Feel free to use and modify with credit.

