
from solution_5_9 import modify_dataframe_columns

import unittest
import pandas as pd

class TestHW0509(unittest.TestCase):
    def test_modify_dataframe_columns(self):
        df = pd.DataFrame({
            'Column1': [1, 2, 10, 20],
            'Column2': [5, 20, 30, 40]
        })
        columns = ['Column1', 'Column2']
        condition_value = 10
        new_value = 100
        result = modify_dataframe_columns(df, columns, condition_value, new_value)
        expected_data = {
            'Column1': [1, 2, 10, 100],
            'Column2': [5, 100, 100, 100]
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(result, expected_df)
        
