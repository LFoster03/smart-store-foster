import pandas as pd
import numpy as np

# Load the data (replace with the correct path if needed)
df = pd.read_csv('/Users/lindsayfoster/Projects/smart-store-foster/data/raw/sales_data.csv')

# Step 1: Verify that the dataset has the correct number and type of columns
expected_columns = ['TransactionID', 'SaleDate', 'CustomerID', 'ProductID', 'StoreID', 'CampaignID', 'SaleAmount', 'DiscountPercent', 'PaymentType']

# Check if the data has the expected columns
if df.columns.tolist() != expected_columns:
    print("Warning: Column mismatch detected. The dataset may need to be corrected.")
else:
    print("Columns are as expected.")

# Step 2: Remove duplicates (rows)
print("\nRemoving duplicates...")
df = df.drop_duplicates()

# Step 3: Handle missing data
print("\nHandling missing data...")

# Drop rows where essential columns have missing values
df = df.dropna(subset=['TransactionID', 'SaleDate', 'CustomerID', 'ProductID', 'StoreID', 'CampaignID', 'SaleAmount', 'DiscountPercent', 'PaymentType'])

# Handle missing or invalid 'SaleAmount' and 'DiscountPercent' by filling them with appropriate values
df['SaleAmount'] = pd.to_numeric(df['SaleAmount'], errors='coerce')
df['DiscountPercent'] = pd.to_numeric(df['DiscountPercent'], errors='coerce')

# Fill missing 'SaleAmount' and 'DiscountPercent' with 0 (or another appropriate strategy based on your context)
df['SaleAmount'] = df['SaleAmount'].fillna(0)
df['DiscountPercent'] = df['DiscountPercent'].fillna(0)

# Step 4: Remove duplicate columns by name
print("\nRemoving duplicate columns by name...")

# Drop columns that have the same name (e.g., 'DiscountPercent.1')
df = df.loc[:, ~df.columns.str.contains('\.1$', regex=True)]

# Step 5: Ensure that numerical columns are of the correct type
df['SaleAmount'] = pd.to_numeric(df['SaleAmount'], errors='coerce')
df['DiscountPercent'] = pd.to_numeric(df['DiscountPercent'], errors='coerce')

# Step 6: Remove outliers from 'SaleAmount' and 'DiscountPercent' using IQR (Interquartile Range)
def remove_outliers(df, column_name):
    Q1 = df[column_name].quantile(0.25)
    Q3 = df[column_name].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    # Remove rows that fall outside the IQR bounds
    return df[(df[column_name] >= lower_bound) & (df[column_name] <= upper_bound)]

# Apply outlier removal on 'SaleAmount' and 'DiscountPercent' columns
print("\nRemoving outliers from 'SaleAmount' and 'DiscountPercent'...")
df = remove_outliers(df, 'SaleAmount')
df = remove_outliers(df, 'DiscountPercent')

# Step 7: Final check for data consistency
print("\nFinal data check...")

# Verify the cleaned dataset structure
print(f"\nFinal columns: {df.columns.tolist()}")
print(f"Final number of records: {df.shape[0]}")

# Save the cleaned data to a new CSV file
df.to_csv('sales_data_prepared.csv', index=False)

print("\nData preparation complete. Cleaned data saved as 'sales_data_prepared.csv'.")
