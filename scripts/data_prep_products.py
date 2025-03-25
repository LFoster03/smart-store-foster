"""
Module 3: Data Preparation Script
File: scripts/data_prep.py

This script is just one example of a possible data preparation process.
It loads raw CSV files from the 'data/raw/' directory, cleans and prepares each file, 
and saves the prepared data to 'data/prepared/'.
The data preparation steps include removing duplicates, handling missing values, 
trimming whitespace, and more.

This script uses the general DataScrubber class and its methods to perform common, reusable tasks.

To run it, open a terminal in the root project folder.
Activate the local project virtual environment.
Choose the correct command for your OS to run this script.

py scripts\data_prep.py
python3 scripts\data_prep.py
 
"""

import pathlib
import sys
import pandas as pd

# For local imports, temporarily add project root to Python sys.path
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# Now we can import local modules
from utils.logger import logger  # noqa: E402
from scripts.data_scrubber import DataScrubber  # noqa: E402

# Constants
DATA_DIR: pathlib.Path = PROJECT_ROOT.joinpath("data")
RAW_DATA_DIR: pathlib.Path = DATA_DIR.joinpath("raw")
PREPARED_DATA_DIR: pathlib.Path = DATA_DIR.joinpath("prepared")

def read_raw_data(file_name: str) -> pd.DataFrame:
    """Read raw data from CSV."""
    file_path: pathlib.Path = RAW_DATA_DIR.joinpath(file_name)
    return pd.read_csv(file_path)

def save_prepared_data(df: pd.DataFrame, file_name: str) -> None:
    """Save cleaned data to CSV."""
    file_path: pathlib.Path = PREPARED_DATA_DIR.joinpath(file_name)
    df.to_csv(file_path, index=False)
    logger.info(f"Data saved to {file_path}")

def main() -> None:
    """Main function for pre-processing customer, product, and sales data."""
    logger.info("======================")
    logger.info("STARTING data_prep.py")
    logger.info("======================")

    logger.info("========================")
    logger.info("Starting PRODUCTS prep")
    logger.info("========================")

    # Read raw product data
    df_products = read_raw_data("/Users/lindsayfoster/Projects/smart-store-foster/data/raw/products_data.csv")

    # Clean column names (strip spaces)
    df_products.columns = df_products.columns.str.strip()

    # Remove duplicate rows
    df_products = df_products.drop_duplicates()

    # Clean up string columns and handle missing data
    df_products['ProductName'] = df_products['ProductName'].str.strip()  # Trim whitespace from 'ProductName' column
    
    # Initialize DataScrubber for products
    scrubber_products = DataScrubber(df_products)
    scrubber_products.check_data_consistency_before_cleaning()
    scrubber_products.inspect_data()
    
    # Handle missing data
    df_products = scrubber_products.handle_missing_data(fill_value="Unknown")
    
    scrubber_products.check_data_consistency_after_cleaning()

    # Save the cleaned data to prepared_products_data.csv
    save_prepared_data(df_products, "prepared_products_data.csv")

    logger.info("======================")
    logger.info("FINISHED PRODUCTS prep")
    logger.info("======================")

if __name__ == "__main__":
    main()
