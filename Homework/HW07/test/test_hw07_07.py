
from solution_7_7 import aggregate_region_data  
import unittest
import pandas as pd

class TestHW0707(unittest.TestCase):
    def test_aggregate_region_data(self):
        df = pd.read_csv('/data/IFI8410/sess07/sample_sales_data_new.csv')

        result = aggregate_region_data(df)
        
        expected_data = {
            'Region': ['East', 'North', 'South', 'West'],
            'TotalQuantity': [13, 30, 28, 24],
            'MeanQuantity': [4.33, 7.5, 9.33, 8.0],
            'TotalSales': [130, 300, 280, 240],
            'MaxSales': [70, 100, 120, 100]
        }
        expected_df = pd.DataFrame(expected_data)

        pd.testing.assert_frame_equal(result.round(2), expected_df.round(2))

