import unittest
import os
import sqlite3
import pandas as pd
from pipeline import Pipeline  # Ensure your pipeline class is in a file named pipeline.py

class TestDataPipeline(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize and run the pipeline
        cls.pipeline = Pipeline()
        cls.pipeline.extract_data()
        cls.pipeline.transform_data()

    def test_raw_csv_files_exist(self):
        # Check if the raw CSV files exist
        self.assertTrue(os.path.isfile('./data/raw_csv/Electricity_Sales_by_Sector.csv'),
                        "Electricity Sales CSV file does not exist")
        self.assertTrue(os.path.isfile('./data/raw_csv/Electric_Generation_By_Fuel_Type.csv'),
                        "Electric Generation CSV file does not exist")

    def test_sqlite_file_exists(self):
        # Check if the SQLite database file exists
        self.assertTrue(os.path.isfile('./data/ClimateData_revised.sqlite'),
                        "SQLite database file does not exist")

    def test_sqlite_table_content(self):
        # Connect to the SQLite database and check if the table has data
        conn = sqlite3.connect('./data/ClimateData_revised.sqlite')
        query = "SELECT COUNT(*) FROM ElectricityData"
        cursor = conn.cursor()
        cursor.execute(query)
        count = cursor.fetchone()[0]
        conn.close()
        self.assertTrue(count > 0, "SQLite database table 'ElectricityData' is empty")

    def test_merged_data_integrity(self):
        # Connect to the SQLite database and validate the merged data
        conn = sqlite3.connect('./data/ClimateData_revised.sqlite')
        df = pd.read_sql_query("SELECT * FROM ElectricityData", conn)
        conn.close()
        self.assertFalse(df.empty, "Merged data in the database is empty")
        self.assertTrue('Year' in df.columns, "'Year' column is missing in the merged data")

if __name__ == '__main__':
    unittest.main()
