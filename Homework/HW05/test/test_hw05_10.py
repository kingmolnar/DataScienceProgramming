
from solution_5_10 import select_specific_data

import unittest
import pandas as pd

class TestHW0510(unittest.TestCase):
    def test_select_specific_data(self):
        data = {
            'Column1': [1, 2, 3, 4],
            'Column2': [5, 6, 7, 8],
            'Column3': [9, 10, 11, 12]
        }
        df = pd.DataFrame(data)
        row_labels = [1, 3]
        column_labels = ['Column1', 'Column3']
        result = select_specific_data(df, row_labels, column_labels)
        expected_data = {
            'Column1': [2, 4],
            'Column3': [10, 12]
        }
        expected_df = pd.DataFrame(expected_data, index=[1, 3])
        pd.testing.assert_frame_equal(result, expected_df)
        
