
from solution_6_3 import detect_and_filter_outliers
import unittest
import pandas as pd

class TestHW0603(unittest.TestCase):
    def test_detect_and_filter_outliers(self):
        data = {
            'Company': ['Company A', 'Company B', 'Company C', 'Company D', 'Company E'],
            'Revenue': [100000, 200000, 3000000, 250000, 500000],
            'Profit': [10000, 15000, 200000, 50000, 600000]
        }
        df5 = pd.DataFrame(data)

        df_no_outliers, df_no_outliers_any = detect_and_filter_outliers(df5)

        # Expected result without using .any(axis="columns")
        expected_data_no_any = {
            'Company': ['Company A', 'Company B', 'Company D'],
            'Revenue': [100000, 200000, 250000],
            'Profit': [10000, 15000, 50000]
        }
        expected_df_no_any = pd.DataFrame(expected_data_no_any)

        # Expected result with using .any(axis="columns")
        expected_data_any = expected_data_no_any
        expected_df_any = pd.DataFrame(expected_data_any)

        # Reset index in the result DataFrames for comparison
        pd.testing.assert_frame_equal(df_no_outliers.reset_index(drop=True), expected_df_no_any)
        pd.testing.assert_frame_equal(df_no_outliers_any.reset_index(drop=True), expected_df_any)
