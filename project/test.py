import pandas as pd
import sqlite3
import os

# Extracting table name from SQLite file
def fetch_data_from_sqlite(sql_filepath, table_name):
    # Connect to SQLite database
    conn = sqlite3.connect(sql_filepath)
    query = f"SELECT * FROM {table_name};"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Check if table name is available or not
def test_data_existence(sql_filepath, table_name):
    df = fetch_data_from_sqlite(sql_filepath, table_name)
    if len(df) > 1:
        print(f"Data exists in {table_name} table.")
    else:
        print(f"Data does not exist in {table_name} table.")


# Check if dataframe contain values or not
def check_null_values(sql_filepath, table_name):
    df = fetch_data_from_sqlite(sql_filepath, table_name)
    if df.isnull().any().any():
        print(f"DataFrame for {table_name} contains null values.")
    else:
        print(f"DataFrame for {table_name} does not contain null values.")

def get_sql_file_path(directory, filename):
    return os.path.join(os.getcwd(), directory, filename)

def test_datasets():
    # Test 1: arrestdata Data
    arrest_sql_filepath = get_sql_file_path("data", "arrestdata.sqlite")
    arrest_table_name = "arrestdata"
    print(f"Testing data existence in {arrest_table_name}...")
    test_data_existence(arrest_sql_filepath, arrest_table_name)
    print("Testing null values in arrestdata dataset...")
    check_null_values(arrest_sql_filepath, arrest_table_name)

    # Test 2: crimedata Data
    crime_sql_filepath = get_sql_file_path("data", "crimedata.sqlite")
    crime_table_name = "crimedata"
    print(f"Testing data existence in {crime_table_name}...")
    test_data_existence(crime_sql_filepath, crime_table_name)
    print("Testing null values in crimedata dataset...")
    check_null_values(crime_sql_filepath, crime_table_name)
    
    print("All test runs have been finished.")

if __name__ == "__main__":
    test_datasets()
