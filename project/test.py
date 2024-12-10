import pandas as pd
import sqlite3
import os

# Extracting table name from SQLite file
def fetch_data_from_sqlite(sql_filepath, table_name):
    conn = sqlite3.connect(sql_filepath)
    query = f"SELECT * FROM {table_name};"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Save cleaned DataFrame back to the SQLite database
def save_cleaned_data(sql_filepath, table_name, df):
    conn = sqlite3.connect(sql_filepath)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()

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

# Check for duplicate rows in the dataset
def check_duplicates(sql_filepath, table_name):
    df = fetch_data_from_sqlite(sql_filepath, table_name)
    if df.duplicated().any():
        print(f"DataFrame for {table_name} contains duplicate rows.")
    else:
        print(f"DataFrame for {table_name} does not contain duplicate rows.")

# Check unique constraint for specific columns
def validate_unique_constraints(sql_filepath, table_name, unique_columns):
    df = fetch_data_from_sqlite(sql_filepath, table_name)
    for column in unique_columns:
        if df[column].duplicated().any():
            print(f"Column {column} in {table_name} contains duplicate values.")
        else:
            print(f"Column {column} in {table_name} satisfies unique constraint.")

# Validate required columns are present in the table
def validate_required_columns(sql_filepath, table_name, required_columns):
    df = fetch_data_from_sqlite(sql_filepath, table_name)
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        print(f"Table {table_name} is missing columns: {missing_columns}")
    else:
        print(f"Table {table_name} contains all required columns.")

# Check if Sex column contains only 'Male' and 'Female'
def validate_sex_column(sql_filepath, table_name):
    df = fetch_data_from_sqlite(sql_filepath, table_name)
    
    # Rename 'Sex Code' to 'sex' if present for Arrest Data
    if 'Sex Code' in df.columns:
        df.rename(columns={'Sex Code': 'Sex'}, inplace=True)

    # Rename 'Vict Sex' to 'sex' if present for Crime Data
    if 'Vict Sex' in df.columns:
        df.rename(columns={'Vict Sex': 'Sex'}, inplace=True)

    if 'Sex' in df.columns:
        invalid_values = df[~df['Sex'].isin(['M', 'F'])]
        if not invalid_values.empty:
            print(f"Sex column in {table_name} contains invalid values. Removing these rows:")
            print(invalid_values)
            df = df[df['Sex'].isin(['M', 'F'])]
            save_cleaned_data(sql_filepath, table_name, df)
            print(f"Invalid rows removed. Updated table saved.")
        else:
            print(f"Sex column in {table_name} contains only valid values ('Male', 'Female').")
    else:
        print(f"Sex column is missing in {table_name}.")

# Check if Age column has no negative values
def validate_age_column(sql_filepath, table_name):
    df = fetch_data_from_sqlite(sql_filepath, table_name)

    # Rename 'Vict Age' to 'Age' if present for Crime Data
    if 'Vict Age' in df.columns:
        df.rename(columns={'Vict Age': 'Age'}, inplace=True)

    if 'Age' in df.columns:
        negative_ages = df[df['Age'] < 0]
        if not negative_ages.empty:
            print(f"Age column in {table_name} contains negative values:")
            print(negative_ages)
        else:
            print(f"Age column in {table_name} has no negative values.")
    else:
        print(f"Age column is missing in {table_name}.")

def get_sql_file_path(directory, filename):
    # Save the current working directory
    original_directory = os.getcwd()
    # Change to the parent directory (one level up)
    os.chdir('..')
    # Construct the new path after changing the directory
    sql_file_path = os.path.join(os.getcwd(), directory, filename)
    # Change back to the original directory
    os.chdir(original_directory)
    return sql_file_path
 

def test_datasets():
    # Test 1: arrestdata Data
    arrest_sql_filepath = get_sql_file_path("data", "arrestdata.sqlite")
    arrest_table_name = "arrestdata"
    print(f"Testing data existence in {arrest_table_name}...")
    test_data_existence(arrest_sql_filepath, arrest_table_name)
    print("Testing null values in arrestdata dataset...")
    check_null_values(arrest_sql_filepath, arrest_table_name)
    print("Testing duplicates in arrestdata dataset...")
    check_duplicates(arrest_sql_filepath, arrest_table_name)
    print("Validating unique constraints in arrestdata dataset...")
    validate_unique_constraints(arrest_sql_filepath, arrest_table_name, ["Report ID"])
    print("Validating required columns in arrestdata dataset...")
    validate_required_columns(arrest_sql_filepath, arrest_table_name, ["Report ID", "Sex Code","Arrest Date", "Age","Charge Group Description"])
    print("Validating Sex column in arrestdata dataset...")
    validate_sex_column(arrest_sql_filepath, arrest_table_name)
    print("Validating Age column in arrestdata dataset...")
    validate_age_column(arrest_sql_filepath, arrest_table_name)


    # Test 2: crimedata Data
    crime_sql_filepath = get_sql_file_path("data", "crimedata.sqlite")
    crime_table_name = "crimedata"
    print(f"Testing data existence in {crime_table_name}...")
    test_data_existence(crime_sql_filepath, crime_table_name)
    print("Testing null values in crimedata dataset...")
    check_null_values(crime_sql_filepath, crime_table_name)
    print("Testing duplicates in crimedata dataset...")
    check_duplicates(crime_sql_filepath, crime_table_name)
    print("Validating unique constraints in crimedata dataset...")
    validate_unique_constraints(crime_sql_filepath, crime_table_name, ["DR_NO"])
    print("Validating required columns in crimedata dataset...")
    validate_required_columns(crime_sql_filepath, crime_table_name, ["DR_NO", "Date Rptd", "AREA", "AREA NAME", "Vict Age", "Status Desc", "Vict Sex", "LOCATION"])
    print("Validating Sex column in crimedata dataset...")
    validate_sex_column(crime_sql_filepath, crime_table_name)
    print("Validating Age column in crimedata dataset...")
    validate_age_column(crime_sql_filepath, crime_table_name)


    print("All test runs have been finished.")

if __name__ == "__main__":
    test_datasets()  # Run validation tests
