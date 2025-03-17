import pandas as pd
import numpy as np

# Load the data (replace with the correct path if needed)
df = pd.read_csv('/Users/lindsayfoster/Projects/smart-store-foster/data/raw/customers_data.csv')

# Step 1: Verify that the dataset has the correct number and type of columns
expected_columns = ['CustomerID', 'Name', 'Region', 'JoinDate', 'LoyaltyPoints', 'CustomerSegment', 'LastPurchaseDate']

# Check if the data has the expected columns
if df.columns.tolist() != expected_columns:
    print("Warning: Column mismatch detected. The dataset may need to be corrected.")
else:
    print("Columns are as expected.")

# Step 2: Remove duplicates
print("\nRemoving duplicates...")
df = df.drop_duplicates()

# Step 3: Handle missing data (for example, dropping rows with missing essential columns)
# We will drop rows with missing values in 'CustomerID', 'Name', 'LoyaltyPoints', and 'CustomerSegment'
print("\nHandling missing data...")
df = df.dropna(subset=['CustomerID', 'Name', 'LoyaltyPoints', 'CustomerSegment'])

# We can also handle other missing columns by filling them in or removing rows if required
# For example, handling missing 'CustomerSegment' could involve filling with a default value (e.g., 'Unknown')
df['CustomerSegment'] = df['CustomerSegment'].fillna('Unknown')

# Step 4: Convert date columns to datetime format (JoinDate and LastPurchaseDate)
df['JoinDate'] = pd.to_datetime(df['JoinDate'], errors='coerce')  # Convert to datetime, invalid dates become NaT
df['LastPurchaseDate'] = pd.to_datetime(df['LastPurchaseDate'], errors='coerce')  # Same for LastPurchaseDate

# Handle any invalid date entries (NaT)
df = df.dropna(subset=['JoinDate', 'LastPurchaseDate'])

# Step 5: Remove outliers from 'LoyaltyPoints' using IQR (Interquartile Range)
def remove_outliers(df, column_name):
    Q1 = df[column_name].quantile(0.25)
    Q3 = df[column_name].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    # Remove rows that fall outside the IQR bounds
    return df[(df[column_name] >= lower_bound) & (df[column_name] <= upper_bound)]

# Apply outlier removal on 'LoyaltyPoints' column
print("\nRemoving outliers from 'LoyaltyPoints'...")
df = remove_outliers(df, 'LoyaltyPoints')

# Step 6: Final check for data consistency
print("\nFinal data check...")

# Verify the cleaned dataset structure
print(f"\nFinal columns: {df.columns.tolist()}")
print(f"Final number of records: {df.shape[0]}")

# Save the cleaned data to a new CSV file
df.to_csv('customers_data_prepared.csv', index=False)

print("\nData preparation complete. Cleaned data saved as 'customers_data_prepared.csv'.")
