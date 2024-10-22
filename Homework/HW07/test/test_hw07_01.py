
from solution_7_1 import group_and_aggregate_sales  # Assuming the function is in 'solution_7_1.py'
import unittest
import pandas as pd

class TestHW0701(unittest.TestCase):
    def test_group_and_aggregate_sales(self):
        # Load the CSV file into a DataFrame
        df = pd.read_csv('/data/IFI8410/sess07/sample_sales_data_new.csv')

        # Call the function
        result = group_and_aggregate_sales(df)
        
        # Expected output
        expected_data = {
            'Region': ['East', 'East', 'North', 'North', 'North', 'South', 'South', 'West', 'West', 'West'],
            'Product': ['A', 'B', 'A', 'B', 'C', 'B', 'C', 'A', 'B', 'C'],
            'Quantity': [6, 7, 18, 3, 9, 5, 23, 10, 6, 8],
            'SalesAmount': [60, 70, 180, 30, 90, 50, 230, 100, 60, 80]
        }
        expected_df = pd.DataFrame(expected_data)

        # Ensure the result matches the expected DataFrame
        pd.testing.assert_frame_equal(result, expected_df)
