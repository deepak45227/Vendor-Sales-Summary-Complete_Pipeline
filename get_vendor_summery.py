import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import logging
from ingestion_db import ingest_db

#  Create folder if missing
os.makedirs("logs", exist_ok=True)  

# Database credentials
username = "root"
password = "root"
host = "localhost"
port = 3306
database_name = "vendor_sales"

# Create database connection URL
engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database_name}")

# Logging configuration
logging.basicConfig(
    filename="logs/get_vendor_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

def create_vendor_summary(engine):
    """
    This function will merge different tables to get the overall vendor summary
    and add new columns in the resultant data.
    """
    vendor_sales_summary = pd.read_sql("""
        WITH FreightSummery AS (
            SELECT 
                VendorNumber,
                SUM(Freight) AS FreightCost
            FROM vendor_invoice
            GROUP BY VendorNumber
        ),
        PurchaseSummery AS (
            SELECT 
                p.VendorNumber,
                p.VendorName,
                p.Brand,
                p.Description,
                p.PurchasePrice,
                pp.Price AS ActualPrice,
                pp.Volume, 
                SUM(p.Quantity) AS TotalPurchaseQuantity,
                SUM(p.Dollars) AS TotalPurchaseDollars
            FROM purchases p
            JOIN purchase_prices pp ON p.Brand = pp.Brand
            WHERE p.PurchasePrice > 0
            GROUP BY p.VendorNumber, p.VendorName, p.Brand, p.Description, p.PurchasePrice, pp.Price, pp.Volume
        ),
        SalesSummery AS (
            SELECT 
                VendorNo,
                Brand,
                SUM(SalesQuantity) AS TotalSalesQuantity,
                SUM(SalesDollars) AS TotalSalesDollar,
                SUM(SalesPrice) AS TotalSalesPrice,
                SUM(ExciseTax) AS TotalExciseTax
            FROM sales
            GROUP BY VendorNo, Brand
        )
        SELECT 
            ps.VendorNumber,
            ps.VendorName,
            ps.Brand,
            ps.Description,
            ps.PurchasePrice,
            ps.ActualPrice,
            ps.Volume, 
            ps.TotalPurchaseQuantity,
            ps.TotalPurchaseDollars,
            ss.TotalSalesQuantity,
            ss.TotalSalesDollar,
            ss.TotalSalesPrice,
            ss.TotalExciseTax,
            fs.FreightCost
        FROM PurchaseSummery ps
        LEFT JOIN SalesSummery ss
            ON ps.VendorNumber = ss.VendorNo AND ps.Brand = ss.Brand
        LEFT JOIN FreightSummery fs
            ON ps.VendorNumber = fs.VendorNumber
        ORDER BY ps.TotalPurchaseDollars DESC;
    """, engine)

    return vendor_sales_summary

def clean_data(df):
    """
    This function will clean the data:
    - Change data types
    - Handle missing and infinite values
    - Add calculated columns
    """
    df["Volume"] = df["Volume"].astype("float64")
    df.fillna(0, inplace=True)
    df["VendorName"] = df["VendorName"].str.strip()
    
    # Calculated columns
    df["GrossProfit"] = df["TotalSalesDollar"] - df["TotalPurchaseDollars"]
    df["StockTurnOver"] = df["TotalSalesQuantity"] / df["TotalPurchaseQuantity"]
    df["ProfitMargin"] = (df["GrossProfit"] / df["TotalSalesDollar"]) * 100
    df["SalesPurchaseRatio"] = df["TotalSalesDollar"] / df["TotalPurchaseDollars"]
    
    # Replace inf and -inf with nan
    df.replace([np.inf, -np.inf],np.nan, inplace=True)
    
    return df

if __name__ == "__main__":
    logging.info("Creating Vendor Summary Table .......")
    summary_df = create_vendor_summary(engine)
    logging.info(summary_df.head())

    logging.info("Cleaning Data ......")
    clean_df = clean_data(summary_df)
    logging.info(clean_df.head())

    logging.info("Ingesting Data.......")
    ingest_db(clean_df, 'vendor_sales_summary', engine)
    logging.info("Completed......")
