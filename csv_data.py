import csv
from datetime import datetime

# Part 1: Reading and Writing CSV Files using csv module

# Task 1: Reading Data from a CSV File
def read_data(file_path):
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
        return data
    except FileNotFoundError:
        print("File not found.")
        return None
    except csv.Error as e:
        print(f"CSV error: {e}")
        return None

# Task 2: Writing Data to a CSV File
def write_data(data, file_path, headers):
    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)
        print(f"Data successfully written to {file_path}")
    except csv.Error as e:
        print(f"CSV error: {e}")

# Task 3: Data Cleaning and Transformation
def clean_and_transform_data(file_path):
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            cleaned_data = []

            for row in reader:
                # Clean 'Product' and 'Customer' columns
                row['Product'] = row['Product'].strip()
                row['Customer'] = row['Customer'].strip()

                # Clean 'Sales' column and convert to float
                row['Sales'] = float(row['Sales'].strip())

                # Convert 'Date' column to datetime object
                row['Date'] = datetime.strptime(row['Date'].strip(), '%Y-%m-%d')

                cleaned_data.append(row)
        return cleaned_data
    except FileNotFoundError:
        print("File not found.")
        return None
    except csv.Error as e:
        print(f"CSV error: {e}")
        return None
    except ValueError as e:
        print(f"Data formatting error: {e}")
        return None

# Task 4: Data Aggregation and Analysis
def data_aggregation_and_analysis(data):
    if not data:
        return None, None, None, None

    total_sales = sum(row['Sales'] for row in data)
    average_sales = total_sales / len(data) if len(data) > 0 else 0

    max_sale = max(data, key=lambda x: x['Sales'])
    min_sale = min(data, key=lambda x: x['Sales'])

    return total_sales, average_sales, max_sale, min_sale

# Task 5: Data Filtering
def filter_and_select_data(file_path, category, min_quantity):
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            filtered_data = [
                row for row in reader
                if row['Category'].strip() == category and int(row['Quantity'].strip()) < min_quantity
            ]
        return filtered_data
    except FileNotFoundError:
        print("File not found.")
        return None
    except csv.Error as e:
        print(f"CSV error: {e}")
        return None
    except ValueError as e:
        print(f"Data formatting error: {e}")
        return None

# Example usage (uncomment and modify paths as needed)
# data = read_data('input.csv')
# write_data(data, 'output.csv', ['Header1', 'Header2'])
# cleaned_data = clean_and_transform_data('input.csv')
# total, avg, max_row, min_row = data_aggregation_and_analysis(cleaned_data)
# filtered = filter_and_select_data('input.csv', 'Electronics', 5)
