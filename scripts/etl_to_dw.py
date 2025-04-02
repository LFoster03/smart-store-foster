import pandas as pd
import sqlite3
import pathlib

# Constants
DB_PATH = pathlib.Path("data/dw/sales_warehouse.db")
PREPARED_DATA_DIR = pathlib.Path("data/prepared")

def create_schema(cursor: sqlite3.Cursor) -> None:
    """Create the database schema for the warehouse."""
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            CustomerID INTEGER PRIMARY KEY,
            Name VARCHAR NOT NULL,
            Region VARCHAR NOT NULL,
            JoinDate DATE,
            LoyaltyPoints INTEGER,
            CustomerSegment VARCHAR,
            LastPurchaseDate DATE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            ProductID INTEGER PRIMARY KEY,
            ProductName VARCHAR NOT NULL,
            Category VARCHAR NOT NULL,
            UnitPrice DECIMAL NOT NULL,
            StockQuantity INTEGER NOT NULL,
            Supplier VARCHAR,
            AverageRating DECIMAL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            TransactionID INTEGER PRIMARY KEY,
            SaleDate DATE,
            CustomerID INTEGER,
            ProductID INTEGER,
            StoreID INTEGER,
            CampaignID INTEGER,
            SaleAmount DECIMAL NOT NULL,
            DiscountPercent DECIMAL,
            PaymentType VARCHAR,
            FOREIGN KEY (CustomerID) REFERENCES customers (CustomerID),
            FOREIGN KEY (ProductID) REFERENCES products (ProductID)
        )
    """)

def load_data_to_db():
    """Load data into the warehouse database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create schema (tables)
    create_schema(cursor)

    # Load data from CSVs
    customers_df = pd.read_csv(PREPARED_DATA_DIR.joinpath("/Users/lindsayfoster/Projects/smart-store-foster/data/prepared/customers_data_prepared.csv"))
    products_df = pd.read_csv(PREPARED_DATA_DIR.joinpath("/Users/lindsayfoster/Projects/smart-store-foster/data/prepared/products_data_prepared.csv"))
    sales_df = pd.read_csv(PREPARED_DATA_DIR.joinpath("/Users/lindsayfoster/Projects/smart-store-foster/data/prepared/sales_data_prepared.csv"))

    # Insert data into the customers, products, and sales tables
    customers_df.to_sql("customers", conn, if_exists="append", index=False)
    products_df.to_sql("products", conn, if_exists="append", index=False)
    sales_df.to_sql("sales", conn, if_exists="append", index=False)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    load_data_to_db()
