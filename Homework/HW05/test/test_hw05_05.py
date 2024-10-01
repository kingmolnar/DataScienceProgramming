
from solution_5_5 import reindex_dataframe_columns

import unittest
import pandas as pd

class TestHW0505(unittest.TestCase):
    def test_reindex_dataframe_columns(self):
        df = pd.DataFrame({
            'Column1': [1, 2, 3],
            'Column2': [4, 5, 6]
        })
        new_columns = ['Column2', 'Column3']
        result = reindex_dataframe_columns(df, new_columns, fill_value=-1)
        expected_data = {
            'Column2': [4, 5, 6],
            'Column3': [-1.0, -1.0, -1.0]  # Using floats for filled values
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(result, expected_df)
        
