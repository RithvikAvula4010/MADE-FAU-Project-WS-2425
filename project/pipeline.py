import os
import sys
import pandas as pd
import sqlite3
from pathlib import Path
import requests

class Pipeline:
    def __init__(self):
        pass

    def extract_data(self):
        # URLs for your datasets
        electric_sales_url = 'https://data.ny.gov/api/views/pv7j-5nz8/rows.csv?accessType=DOWNLOAD'
        electric_generation_url = 'https://data.ny.gov/api/views/h4gs-8qnu/rows.csv?accessType=DOWNLOAD'
        
        # Directory to save raw CSVs
        data_dir = './data/raw_csv/'
        os.makedirs(data_dir, exist_ok=True)
        
        # Paths to save files
        sales_data_path = os.path.join(data_dir, 'Electricity_Sales_by_Sector.csv')
        generation_data_path = os.path.join(data_dir, 'Electric_Generation_By_Fuel_Type.csv')

        # Download datasets
        self.download_csv(electric_sales_url, sales_data_path)
        self.download_csv(electric_generation_url, generation_data_path)
        
    def download_csv(self, url, output_path):
        response = requests.get(url)
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded data from {url} to {output_path}")

    def transform_data(self):
        # Define paths
        sales_data_path = './data/raw_csv/Electricity_Sales_by_Sector.csv'
        generation_data_path = './data/raw_csv/Electric_Generation_By_Fuel_Type.csv'
        # output_path = './data/transformed_data.csv'

        # Load datasets with options to handle formatting issues
        try:
            df_sales = pd.read_csv(sales_data_path, delimiter=',')
            df_generation = pd.read_csv(generation_data_path, delimiter=',')
        except Exception as e:
            print("Error loading CSV files:", e)
            return

        # Merge dataframes and save
        merged_df = pd.merge(df_sales, df_generation, how='outer', on='Year')  # adjust column name if necessary
        # merged_df.to_csv(output_path, index=False)
        print("Data transformation complete and saved to transformed_data.csv")

        columns_to_drop = ['Column1', 'Column2']  # replace with actual column names to drop
        merged_df.drop(columns=columns_to_drop, inplace=True, errors='ignore')
        
        # Save to SQLite
        conn = sqlite3.connect('./data/GenerationToSales.sqlite')
        merged_df.to_sql('ElectricityData', conn, if_exists='replace', index=False)
        connection = sqlite3.connect("./data/GenerationToSales.sqlite")  # Replace with your database file name
        cursor = connection.cursor()
        query = "SELECT * FROM ElectricityData"  # Replace 'your_table_name' with the table you're querying
        cursor.execute(query)
        # Fetch all rows from the result
        rows = cursor.fetchall()

        # Process the rows
        for row in rows:
            print(row)

        # Close the cursor and connection
        cursor.close()
        connection.close()
        
        print("Data inserted successfully into the database.")
        conn.close()

if __name__ == '__main__':
    pipeline = Pipeline()
    pipeline.extract_data()
    pipeline.transform_data()
