
from solution_7_6 import calculate_sales_range  # Assuming the function is in 'solution_7_6.py'
import unittest
import pandas as pd

class TestHW0706(unittest.TestCase):
    def test_calculate_sales_range(self):
        # Load the CSV file into a DataFrame
        df = pd.read_csv('/data/IFI8410/sess07/sample_sales_data_new.csv')

        # Call the function
        result = calculate_sales_range(df)

        # Expected output
        expected_data = {
            'Region': ['East', 'North', 'South', 'West'],
            'SalesRange': [50, 70, 70, 40]  # Updated value for South region to 70
        }
        expected_df = pd.DataFrame(expected_data)

        # Ensure the result matches the expected DataFrame
        pd.testing.assert_frame_equal(result, expected_df)
