# data_prep.py

import pandas as pd
import numpy as np

# Load dataset
def load_data(file_path):
    """
    Load data from a CSV file.
    :param file_path: str, path to the data file
    :return: pandas DataFrame
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return df
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Basic data cleaning function
def clean_data(df):
    """
    Clean the data by handling missing values and outliers.
    :param df: pandas DataFrame
    :return: cleaned pandas DataFrame
    """
    # Handle missing values - Option 1: Drop rows with missing values
    df_cleaned = df.dropna()  # Drop rows with any missing values
    # Option 2: Fill missing values with mean for numeric columns
    # df_cleaned = df.fillna(df.mean())
    
    print("Data cleaned: Missing values handled.")
    
    # Remove duplicates
    df_cleaned = df_cleaned.drop_duplicates()
    print("Duplicates removed.")
    
    # Handling outliers - simple method (you can expand this as per your analysis)
    for column in df_cleaned.select_dtypes(include=[np.number]).columns:
        Q1 = df_cleaned[column].quantile(0.25)
        Q3 = df_cleaned[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df_cleaned = df_cleaned[(df_cleaned[column] >= lower_bound) & (df_cleaned[column] <= upper_bound)]
    
    print("Outliers removed using IQR method.")
    return df_cleaned

# Data exploration functions
def explore_data(df):
    """
    Perform basic data exploration.
    :param df: pandas DataFrame
    """
    # Show basic information about the DataFrame
    print("\nBasic info:")
    print(df.info())
    
    # Summary statistics for numerical columns
    print("\nSummary statistics for numerical columns:")
    print(df.describe())
    
    # Check for missing values
    print("\nMissing values in each column:")
    print(df.isnull().sum())

# Main function to execute the preparation steps
def main(file_path):
    # Load the data
    df = load_data(file_path)
    if df is None:
        return
    
    # Explore data
    explore_data(df)
    
    # Clean the data
    df_cleaned = clean_data(df)
    
    # Explore cleaned data
    explore_data(df_cleaned)
    
    # Optionally save cleaned data
    df_cleaned.to_csv('cleaned_data.csv', index=False)
    print("Cleaned data saved as 'cleaned_data.csv'")

# Run the main function with your file path
if __name__ == "__main__":
    # Example file path - replace with your actual file
    file_path = '/Users/lindsayfoster/Projects/smart-store-foster/data/raw/sales_data.csv'
    main(file_path)
