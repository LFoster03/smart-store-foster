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
1. Load Data: Reads the sales_data.csv file into a Pandas DataFrame.
2. Verify Columns: Checks if the dataset has the correct columns, as expected.
3. Remove Duplicates: Removes duplicate rows from the dataset.
4. Handle Missing Data: Fills any missing values in the dataset for key columns like SaleAmount and DiscountPercent.
5. Remove Duplicate Columns: Drops any duplicate columns, particularly those with .1 (e.g., DiscountPercent.1).
6. Ensure Correct Data Types: Ensures columns like SaleAmount and DiscountPercent are of numeric type.
7. Remove Outliers: Identifies and removes outliers in the SaleAmount and DiscountPercent columns based on the interquartile range (IQR).
8. Save Cleaned Data: Saves the cleaned data to a new CSV file, ex.: sales_data_prepared.csv.

# Step-by-Step Breakdown of DataScrubber
1. Review the DataScrubber Class:

Objective: The class DataScrubber is already partially implemented. Your job is to review the class and complete the methods where TODO comments are present. These are the unfinished parts that need your attention.

What to do: Open the scripts/data_scrubber.py file. Look for TODO comments within the code. These comments will indicate where you need to write or fix code logic.

2. Tasks to Complete in DataScrubber:

For each TODO in the DataScrubber class, you need to:

Understand what the method is supposed to do.

Complete the method logic (e.g., fixing the string formatting, handling missing data, etc.).

For example, in the format_column_strings_to_upper_and_trim method, you will need to implement the logic to convert text to uppercase and remove whitespace.

3. Unit Testing with unittest:

Objective: After implementing or fixing the methods in the DataScrubber class, you need to verify that everything works correctly by running tests.

What to do:

There’s a separate test file for this class (tests/test_data_scrubber.py).

This test file should contain unit tests that will automatically check whether the DataScrubber methods are working as expected.

How to test: After completing the DataScrubber methods:

Open tests/test_data_scrubber.py and run the tests to check if all methods in your class pass.

Running tests: You can run the tests using unittest in Python. If you're using VS Code, you can run the tests directly in the terminal, or you can use the testing interface.

4. Ensure All Tests Pass:

After running the tests, verify that all of them pass (100%). This means that each cleaning method you implemented is functioning as expected. If any test fails, it will tell you what part of your DataScrubber class needs to be fixed.

Modify your code as needed: If a test fails, go back and tweak the relevant method in the DataScrubber class and run the tests again.

5. Use the DataScrubber in a Data Preparation Script:

Once your DataScrubber class is working and all tests pass, you will use the DataScrubber class in your data prep script.This means you will import the class and use it to clean your data.

# Use Data Scrubber 

Create Main Data Prep script(s)

scripts/data_prep_cutomers.py
scripts/data_prep_products.py
scripts/data_prep_sales.py

Data Cleaning Steps:

Removed duplicate rows.

Cleaned column names by stripping spaces.

Trimmed whitespace from the 'Name' column and dropped rows with missing CustomerID or Name.

Used the DataScrubber class to handle missing data, check consistency, and parse the JoinDate column as a datetime.

Logging: Added logging messages to track the progress of the data preparation process for the customer data.

Next Steps:
Run the Script:This script will process the customers_data.csv file and save the cleaned data to prepared_customers_data.csv.