
from solution_7_10 import create_sales_pivot_table  # Assuming the function is in 'solution_7_10.py'
import unittest
import pandas as pd

class TestHW0710(unittest.TestCase):
    def test_create_sales_pivot_table(self):
        # Load the CSV file into a DataFrame
        df = pd.read_csv('/data/IFI8410/sess07/sample_sales_data_new.csv')

        # Call the function
        result = create_sales_pivot_table(df)

        # Expected output
        expected_data = {
            'Product': ['A', 'B', 'C'],
            'East': [60, 70, 0],
            'North': [180, 30, 90],
            'South': [0, 50, 230],
            'West': [100, 60, 80]
        }
        expected_df = pd.DataFrame(expected_data).set_index('Product').T

        # Remove the index name from the actual result
        result.index.name = None

        # Ensure the result matches the expected DataFrame
        pd.testing.assert_frame_equal(result, expected_df)
