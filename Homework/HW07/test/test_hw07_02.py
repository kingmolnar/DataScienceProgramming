
from solution_7_2 import iterate_over_groups  # Assuming the function is in 'solution_7_2.py'
import unittest
import pandas as pd

class TestHW0702(unittest.TestCase):
    def test_iterate_over_groups(self):
        # Load the CSV file into a DataFrame
        df = pd.read_csv('/data/IFI8410/sess07/sample_sales_data_new.csv')

        # Call the function to group by Region
        result = iterate_over_groups(df)

        # Expected group data for each region
        expected_east = pd.DataFrame({
            'Region': ['East', 'East', 'East'],
            'Salesperson': ['Linda', 'Emma', 'Linda'],
            'Product': ['B', 'A', 'A'],
            'Quantity': [7, 4, 2],
            'SalesAmount': [70, 40, 20]
        })

        expected_north = pd.DataFrame({
            'Region': ['North', 'North', 'North', 'North'],
            'Salesperson': ['John', 'Mike', 'Robert', 'John'],
            'Product': ['A', 'A', 'C', 'B'],
            'Quantity': [10, 8, 9, 3],
            'SalesAmount': [100, 80, 90, 30]
        })

        expected_south = pd.DataFrame({
            'Region': ['South', 'South', 'South'],
            'Salesperson': ['Sara', 'Anna', 'Sophia'],
            'Product': ['B', 'C', 'C'],
            'Quantity': [5, 12, 11],
            'SalesAmount': [50, 120, 110]
        })

        expected_west = pd.DataFrame({
            'Region': ['West', 'West', 'West'],
            'Salesperson': ['Tom', 'Chris', 'Tom'],
            'Product': ['A', 'B', 'C'],
            'Quantity': [10, 6, 8],
            'SalesAmount': [100, 60, 80]
        })

        # Assertions to check each region's DataFrame, ignoring index
        pd.testing.assert_frame_equal(result['East'].reset_index(drop=True), expected_east)
        pd.testing.assert_frame_equal(result['North'].reset_index(drop=True), expected_north)
        pd.testing.assert_frame_equal(result['South'].reset_index(drop=True), expected_south)
        pd.testing.assert_frame_equal(result['West'].reset_index(drop=True), expected_west)
