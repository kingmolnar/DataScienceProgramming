
from solution_5_12 import multiply_dataframes_with_fill

import unittest
import pandas as pd
import numpy as np

class TestHW0512(unittest.TestCase):
    def test_multiply_dataframes_with_fill(self):
        data1 = {
            'Column1': [1, 2, 3],
            'Column2': [3, 2, 4],
        }
        data2 = {
            'Column1': [np.nan, 2, 2],
            'Column3': [np.nan, 4, 2],
        }
        df1 = pd.DataFrame(data1)
        df2 = pd.DataFrame(data2)
        
        result = multiply_dataframes_with_fill(df1, df2)
        
        expected_data = {
            'Column1': [1.0, 4.0, 6.0],
            'Column2': [3.0, 2.0, 4.0],
            'Column3': [1.0, 4.0, 2.0],
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(result, expected_df)
