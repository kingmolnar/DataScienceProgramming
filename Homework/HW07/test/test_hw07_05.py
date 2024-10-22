
from solution_7_5 import calculate_revenue_per_item  # Assuming the function is in 'solution_7_5.py'
import unittest
import pandas as pd

class TestHW0705(unittest.TestCase):
    def test_calculate_revenue_per_item(self):
        # Load the CSV file into a DataFrame
        df = pd.read_csv('/data/IFI8410/sess07/sample_sales_data_new.csv')

        # Call the function
        result = calculate_revenue_per_item(df)

        # Expected output
        expected_data = {
            'Region': ['East', 'North', 'South', 'West'],
            'TotalQuantity': [13, 30, 28, 24],
            'TotalRevenue': [130, 300, 280, 240],
            'RevenuePerItem': [10.0, 10.0, 10.0, 10.0]
        }
        expected_df = pd.DataFrame(expected_data)

        # Convert the TotalQuantity and TotalRevenue columns to float for comparison
        result['TotalQuantity'] = result['TotalQuantity'].astype(float)
        result['TotalRevenue'] = result['TotalRevenue'].astype(float)
        expected_df['TotalQuantity'] = expected_df['TotalQuantity'].astype(float)
        expected_df['TotalRevenue'] = expected_df['TotalRevenue'].astype(float)

        # Ensure the result matches the expected DataFrame
        pd.testing.assert_frame_equal(result, expected_df)
