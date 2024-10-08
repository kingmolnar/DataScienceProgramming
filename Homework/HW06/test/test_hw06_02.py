
from solution_6_2 import replace_values_and_rename_axes
import unittest
import pandas as pd

class TestHW0602(unittest.TestCase):
    def test_replace_values_and_rename_axes(self):
        data = {
            'Company': ['Apple', 'Google', 'Pfizer', 'Tesla'],
            'Revenue': [260000, 160000, 52000, 24000],
            'Profit': [55000, 34000, 10000, 1000],
            'Sector': ['Tech', 'Tech', 'Health', 'Auto']
        }
        df4 = pd.DataFrame(data)
        df4.set_index('Company', inplace=True)

        replacements_dict = {'Tech': 'Technology', 'Health': 'Healthcare'}

        result = replace_values_and_rename_axes(df4, replacements_dict)

        expected_data = {
            'Company': ['apple', 'google', 'pfizer', 'tesla'],
            'REVENUE': [260000, 160000, 52000, 24000],
            'PROFIT': [55000, 34000, 10000, 1000],
            'SECTOR': ['Technology', 'Technology', 'Healthcare', 'Auto']
        }
        expected_df = pd.DataFrame(expected_data)
        expected_df.set_index('Company', inplace=True)
        
        pd.testing.assert_frame_equal(result, expected_df)
