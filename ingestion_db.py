import pandas as pd
import os
from sqlalchemy import create_engine, text
import time
import logging

os.makedirs("logs", exist_ok=True)  # ✅ Create folder if missing


# Database credentials
username = "root"
password = "root"
host = "localhost"
port = 3306
database_name = "vendor_sales"

# Create database connection URL
engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database_name}")
engine_root = create_engine(f"mysql+mysqlconnector://{username}:{password}@{host}:{port}")

# Create database if not exists
with engine_root.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {database_name}"))
    conn.commit()

# Setup Logging
logging.basicConfig(
    filename="logs/ingestion.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

# Ingestion function
def ingest_db(df, table_name, engine):
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Loaded into table {table_name}")

# Ingest in chunks for large files
def ingest_in_chunks(df, table_name, connection, chunksize=50000):
    df.to_sql(
        table_name,
        connection,
        if_exists='replace',
        index=False,
        chunksize=chunksize,
        method='multi'
    )

# Main function to load and ingest data
def load_raw_data():
    folder_path = "data\\data"  # Folder path

    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            start = time.time()

            path = os.path.join(folder_path, file)
            table_name = os.path.splitext(file)[0]
            df = pd.read_csv(path)

            try:
                with engine.begin() as connection:
                    if table_name in ["purchases", "sales"]:
                        logging.info(f"Ingesting {file} in chunks...")
                        ingest_in_chunks(df, table_name, connection, chunksize=50000)
                    else:
                        logging.info(f"Ingesting {file} normally...")
                        df.to_sql(table_name, connection, if_exists='replace', index=False)

                    print(f"Loaded {file} into table {table_name}")

                end = time.time()
                total_time = (end - start) / 60
                logging.info(f"Completed ingestion of {file} in {total_time:.2f} minutes")

            except Exception as e:
                logging.error(f"Error loading {file}: {e}")
                print(f"Error loading {file}: {e}")

if __name__ == '__main__':
    load_raw_data()
