# smart-store-foster
# Exploring Business Intelligence
## Author: Lindsay Foster
## Date: March 2025
# Create 
Create a repository in GitHub. Open in VS Code. Add .gitignore and requirements.txt. Create a virtual environment and open it. Create folders, data with prepared and raw subfolders, utils folder with subfolder logger.py. Then download the 3 CSV files and put them in the raw folder. 
# Install requirements
Pip install, then also install requirements.txt. 
# Create utils/logger.py
In VS Code, use File / New Folder to create a new folder named utils to hold utility scripts. In this folder, create a file named logger.py. Copy and paste the content from the starter repo.
# Create scripts/data_prep.py
In VS Code, use File / New Folder to create a new folder named scripts to hold scripts. In this folder, create a file named data_prep.py. Copy and paste the content from the starter repo.
I could not find the data_prep.py file at first so I asked ChatGPT to help create a data prep file to do basic data cleaning and then ran that. 
# Git Add
`git add. 
git commit -m "message"
git push'
# Don't forget the .gitignore
Add the requirements for the gitignore file.
# Clean Data
Clean and prepare each csv file by creating a python file with the code to clean the data. Then save that cleaned data as a new csv file in the prepared folder. 
# Fake Data
Open each csv file in Excel and add:
1. Customers Data
Customer Numeric: LoyaltyPoints (numeric)
Customer Category: CustomerSegment (category)
2. Product Data
Products Numeric: StockQuantity (numeric)
Products Category: Supplier (category)
3. Sales Data
Sales Numeric: DiscountPercent (numeric)
Sales Category: PaymentType (category)
Then save these files under the same name. 
# Cleaning and Preparing Data: sales_data.csv Example
Load Data: Reads the sales_data.csv file into a Pandas DataFrame.
Verify Columns: Checks if the dataset has the correct columns, as expected.
Remove Duplicates: Removes duplicate rows from the dataset.
Handle Missing Data: Fills any missing values in the dataset for key columns like SaleAmount and DiscountPercent.
Remove Duplicate Columns: Drops any duplicate columns, particularly those with .1 (e.g., DiscountPercent.1).
Ensure Correct Data Types: Ensures columns like SaleAmount and DiscountPercent are of numeric type.
Remove Outliers: Identifies and removes outliers in the SaleAmount and DiscountPercent columns based on the interquartile range (IQR).
Save Cleaned Data: Saves the cleaned data to a new CSV file, ex.: sales_data_prepared.csv.