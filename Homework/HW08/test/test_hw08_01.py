
from solution_8_1 import split_data_set  # Adjust path based on actual file location

import unittest
import pandas as pd

class TestSplitDataSet(unittest.TestCase):
    def setUp(self):
        # Sample dataset with 500 rows for testing
        self.file_path = '/data/IFI8410/sess10/reduced_fraud_oracle.csv'
        self.df = pd.read_csv(self.file_path)

    def test_split_data_set(self):
        # Apply the function with an 80% split
        df_80, df_20 = split_data_set(self.df, 0.8)

        # Assertions to check the number of rows
        self.assertEqual(len(self.df), 500, "Total records should be 500")
        self.assertEqual(len(df_80), 400, "Training set should have 400 records (80%)")
        self.assertEqual(len(df_20), 100, "Test set should have 100 records (20%)")

        # Check that the sum of split sets matches the original DataFrame
        df_80, df_20 = split_data_set(self.df, 0.8)
        self.assertEqual(len(df_80) + len(df_20), len(self.df), "Combined length of splits should match original")
