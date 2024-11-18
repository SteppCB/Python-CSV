import pandas as pd

# Part 2: Reading and Writing CSV Files using pandas module

# Task 1: Reading Data from a CSV File using pandas
def read_data(file_path):
  # try-except block to handle exceptions
    # read the file using pandas
    # return the dataframe
  # handle FileNotFoundError
  print("File not found.")
  # handle pd.errors.ParserError
  print(f"Parser error: {e}")
  # if there is an error return None
  return None

# Task 2: Writing Data to a CSV File
def write_data(data, file_path, headers):
  # try-except block to handle exceptions
    # create a dataframe using the data and headers
    # write the dataframe to a csv file
    print(f"Data successfully written to {file_path}")
  # handle pd.errors.EmptyDataError
    print(f"Empty data error: {e}")

# Task 3: Data Cleaning and Transformation
def clean_and_transform_data(file_path):
  # try-except block to handle exceptions
    # read the file using pandas
        # Remove leading and trailing spaces from 'Product' and 'Customer' columns

        # Remove leading and trailing spaces from 'Sales' column and convert to float

        # Transform 'Date' column to datetime object using pandas (without importing datetime module)
        # return the dataframe
  # handle FileNotFoundError
  print("File not found.")
  # handle pd.errors.ParserError
  print(f"Parser error: {e}")
  # if there is an error return None
  return None

# Task 4: Data Aggregation and Analysis using pandas
def data_aggregation_and_analysis(data): # data is a dataframe already
  # Calculate total sales using pandas
  total_sales = None
  # Calculate average sales using pandas
  average_sales = None
  # Find the row with the maximum sales using pandas
  max_sale = None
  # Find the row with the minimum sales using pandas
  min_sale = None
  return total_sales, average_sales, max_sale, min_sale

# Task 5: Data Filtering
def filter_and_select_data(file_path, category, min_quantity):
  # try-except block to handle exceptions
    # read the file using pandas
    # filter the data rows where the 'Category' column matches the category argument and the 'Quantity' column is less than the min_quantity argument
  filtered_data = []
  return filtered_data
  # handle FileNotFoundError
  print("File not found.")
  # handle pd.errors.ParserError
  print(f"Parser error: {e}")
  # if there is an error return None
  return None
