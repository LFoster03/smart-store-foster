import pandas as pd
import numpy as np

# Load the data (replace with the correct path if needed)
df = pd.read_csv('/Users/lindsayfoster/Projects/smart-store-foster/data/raw/products_data.csv')

# Step 1: Verify that the dataset has the correct number and type of columns
expected_columns = ['ProductID', 'ProductName', 'Category', 'UnitPrice', 'StockQuantity', 'Supplier', 'AverageRating']

# Check if the data has the expected columns
if df.columns.tolist() != expected_columns:
    print("Warning: Column mismatch detected. The dataset may need to be corrected.")
else:
    print("Columns are as expected.")

# Step 2: Remove duplicates
print("\nRemoving duplicates...")
df = df.drop_duplicates()

# Step 3: Handle missing data
print("\nHandling missing data...")

# Drop rows where essential columns have missing values
df = df.dropna(subset=['ProductID', 'ProductName', 'Category', 'UnitPrice', 'StockQuantity', 'Supplier'])

# Fill missing values in 'AverageRating' with the median rating (since 'Unknown' isn't a valid number)
df['AverageRating'] = pd.to_numeric(df['AverageRating'], errors='coerce')
df['AverageRating'] = df['AverageRating'].fillna(df['AverageRating'].median())

# Step 4: Ensure that numerical columns are of the correct type
df['UnitPrice'] = pd.to_numeric(df['UnitPrice'], errors='coerce')
df['StockQuantity'] = pd.to_numeric(df['StockQuantity'], errors='coerce')

# Step 5: Remove outliers from 'UnitPrice' and 'StockQuantity' using IQR (Interquartile Range)
def remove_outliers(df, column_name):
    Q1 = df[column_name].quantile(0.25)
    Q3 = df[column_name].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    # Remove rows that fall outside the IQR bounds
    return df[(df[column_name] >= lower_bound) & (df[column_name] <= upper_bound)]

# Apply outlier removal on 'UnitPrice' and 'StockQuantity' columns
print("\nRemoving outliers from 'UnitPrice' and 'StockQuantity'...")
df = remove_outliers(df, 'UnitPrice')
df = remove_outliers(df, 'StockQuantity')

# Step 6: Final check for data consistency
print("\nFinal data check...")

# Verify the cleaned dataset structure
print(f"\nFinal columns: {df.columns.tolist()}")
print(f"Final number of records: {df.shape[0]}")

# Save the cleaned data to a new CSV file
df.to_csv('products_data_prepared.csv', index=False)

print("\nData preparation complete. Cleaned data saved as 'products_data_prepared.csv'.")
