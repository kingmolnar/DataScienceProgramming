
from solution_5_13 import subtract_series_from_df

import unittest
import pandas as pd

class TestHW0513(unittest.TestCase):
    def test_subtract_series_from_df(self):
        df = pd.DataFrame({
            'A': [10, 20, 30],
            'B': [1, 2, 3]
        })
        series = pd.Series({'A': 1, 'B': 1})
        result = subtract_series_from_df(df, series)
        expected_df = pd.DataFrame({
            'A': [9, 19, 29],
            'B': [0, 1, 2]
        })
        pd.testing.assert_frame_equal(result, expected_df)
