
from solution_6_1 import transform_financial_data
import unittest
import pandas as pd

class TestHW0601(unittest.TestCase):
    def test_transform_financial_data(self):
        data = {
            'Company': ['Company A', 'Company B', 'Company C', 'Company D'],
            'Revenue': [600000, 300000, 100000, 800000],
            'Profit': [100000, 50000, 15000, 200000],
            'Expenses': [200000, 150000, 85000, 300000]
        }
        df3 = pd.DataFrame(data)

        result = transform_financial_data(df3)

        expected_data = {
            'Company': ['Company A', 'Company B', 'Company C', 'Company D'],
            'Revenue': ['High', 'Medium', 'Low', 'High'],
            'Profit': ['Medium', 'Medium', 'Low', 'High'],
            'Expenses': ['Medium', 'Medium', 'Low', 'High']
        }
        expected_df = pd.DataFrame(expected_data)

        pd.testing.assert_frame_equal(result[['Revenue', 'Profit', 'Expenses']], expected_df[['Revenue', 'Profit', 'Expenses']])


