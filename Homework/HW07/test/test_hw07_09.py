
from solution_7_9 import add_total_sales_by_region  
import unittest
import pandas as pd

class TestHW0709(unittest.TestCase):
    def test_add_total_sales_by_region(self):
    
        df = pd.read_csv('/data/IFI8410/sess07/sample_sales_data_new.csv')

        result = add_total_sales_by_region(df)
        
        expected_data = {
            'Region': ['North', 'South', 'North', 'East', 'West', 'South', 'North', 'East', 'West', 'South', 'North', 'East', 'West'],
            'Salesperson': ['John', 'Sara', 'Mike', 'Linda', 'Tom', 'Anna', 'Robert', 'Emma', 'Chris', 'Sophia', 'John', 'Linda', 'Tom'],
            'Product': ['A', 'B', 'A', 'B', 'A', 'C', 'C', 'A', 'B', 'C', 'B', 'A', 'C'],
            'Quantity': [10, 5, 8, 7, 10, 12, 9, 4, 6, 11, 3, 2, 8],
            'SalesAmount': [100, 50, 80, 70, 100, 120, 90, 40, 60, 110, 30, 20, 80],
            'TotalSalesByRegion': [300, 280, 300, 130, 240, 280, 300, 130, 240, 280, 300, 130, 240]
        }
        expected_df = pd.DataFrame(expected_data)

        pd.testing.assert_frame_equal(result, expected_df)
