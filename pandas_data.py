import pandas as pd

# Part 2: Reading and Writing CSV Files using pandas module

# Task 1: Reading Data from a CSV File using pandas
def read_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("File not found.")
        return None
    except pd.errors.ParserError as e:
        print(f"Parser error: {e}")
        return None

# Task 2: Writing Data to a CSV File
def write_data(data, file_path, headers):
    try:
        df = pd.DataFrame(data, columns=headers)
        df.to_csv(file_path, index=False)
        print(f"Data successfully written to {file_path}")
    except pd.errors.EmptyDataError as e:
        print(f"Empty data error: {e}")

# Task 3: Data Cleaning and Transformation
def clean_and_transform_data(file_path):
    try:
        df = pd.read_csv(file_path)

        # Remove leading and trailing spaces from 'Product' and 'Customer' columns
        df['Product'] = df['Product'].str.strip()
        df['Customer'] = df['Customer'].str.strip()

        # Remove leading and trailing spaces from 'Sales' column and convert to float
        df['Sales'] = df['Sales'].str.strip().astype(float)

        # Transform 'Date' column to datetime object using pandas
        df['Date'] = pd.to_datetime(df['Date'].str.strip(), format='%Y-%m-%d')

        return df
    except FileNotFoundError:
        print("File not found.")
        return None
    except pd.errors.ParserError as e:
        print(f"Parser error: {e}")
        return None
    except ValueError as e:
        print(f"Data formatting error: {e}")
        return None

# Task 4: Data Aggregation and Analysis using pandas
def data_aggregation_and_analysis(data):  # data is a dataframe already
    if data is None or data.empty:
        return None, None, None, None

    # Calculate total sales using pandas
    total_sales = data['Sales'].sum()

    # Calculate average sales using pandas
    average_sales = data['Sales'].mean()

    # Find the row with the maximum sales using pandas
    max_sale = data.loc[data['Sales'].idxmax()]

    # Find the row with the minimum sales using pandas
    min_sale = data.loc[data['Sales'].idxmin()]

    return total_sales, average_sales, max_sale, min_sale

# Task 5: Data Filtering
def filter_and_select_data(file_path, category, min_quantity):
    try:
        df = pd.read_csv(file_path)

        # Filter the data rows where the 'Category' column matches the category argument
        # and the 'Quantity' column is less than the min_quantity argument
        filtered_data = df[(df['Category'].str.strip() == category) & (df['Quantity'].astype(int) < min_quantity)]

        return filtered_data
    except FileNotFoundError:
        print("File not found.")
        return None
    except pd.errors.ParserError as e:
        print(f"Parser error: {e}")
        return None
    except ValueError as e:
        print(f"Data formatting error: {e}")
        return None

# Example usage (uncomment and modify paths as needed)
# df = read_data('input.csv')
# write_data(df, 'output.csv', df.columns)
# cleaned_df = clean_and_transform_data('input.csv')
# total, avg, max_row, min_row = data_aggregation_and_analysis(cleaned_df)
# filtered = filter_and_select_data('input.csv', 'Electronics', 5)
