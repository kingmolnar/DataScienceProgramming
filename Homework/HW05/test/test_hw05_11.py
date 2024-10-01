
from solution_5_11 import select_data_with_iloc

import unittest
import pandas as pd

class TestHW0511(unittest.TestCase):
    def test_select_data_with_iloc(self):
        data = {
            'Column1': [1, 2, 3, 4],
            'Column2': [5, 6, 7, 8],
            'Column3': [9, 10, 11, 12]
        }
        df = pd.DataFrame(data)
        row_indices = [0, 2]
        column_indices = [0, 2]
        result = select_data_with_iloc(df, row_indices, column_indices)
        expected_data = {
            'Column1': [1, 3],
            'Column3': [9, 11]
        }
        expected_df = pd.DataFrame(expected_data, index=[0, 2])
        pd.testing.assert_frame_equal(result, expected_df)
