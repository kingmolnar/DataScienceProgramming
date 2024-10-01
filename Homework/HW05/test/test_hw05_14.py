
from solution_5_14 import range_along_rows

import unittest
import pandas as pd

class TestHW0514(unittest.TestCase):
    def test_range_along_rows(self):
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 1, 0],
            'C': [7, 5, 8]
        })
        result = range_along_rows(df)
        expected_series = pd.Series([6, 4, 8], index=[0, 1, 2])
        pd.testing.assert_series_equal(result, expected_series)
