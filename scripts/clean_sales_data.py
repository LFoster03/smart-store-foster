import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv('/Users/lindsayfoster/Projects/smart-store-foster/data/raw/sales_data.csv')

# Step 2: View the first few rows to understand the structure of the data
print(df.head())

# Step 3: Handle missing values
# Check for missing values in each column
print(df.isnull().sum())

# You can choose one of the following depending on how you'd like to handle missing data
# Option 1: Drop rows with any missing values
df = df.dropna()

# Option 2: Fill missing values with a default value (like 0 or the mean)
# df = df.fillna(0)  # Example of filling with 0
# df = df.fillna(df.mean())  # Example of filling with column mean (for numeric columns)

# Step 4: Remove duplicate rows
df = df.drop_duplicates()

# Step 5: Convert data types if necessary
# For example, converting a 'Date' column to a datetime format
# df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Step 6: Rename columns if needed (you can specify a dictionary for column renaming)
# df = df.rename(columns={'old_column_name': 'new_column_name'})

# Step 7: Handle outliers (optional, depending on the dataset and what you consider outliers)
# Example: remove rows where 'Age' is less than 18
# df = df[df['Age'] >= 18]

# Step 8: Save the cleaned data to a new CSV file
df.to_csv('cleaned_sales_data.csv', index=False)

# Optional: Check the final structure of the cleaned data
print(df.head())

