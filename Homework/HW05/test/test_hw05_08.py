
from solution_5_8 import select_rows_with_iloc

import unittest
import pandas as pd

class TestHW0508(unittest.TestCase):
    def test_select_rows_with_iloc(self):
        data = [1, 5, 10, 15]
        start_pos = 1
        end_pos = 3
        result = select_rows_with_iloc(data, start_pos, end_pos)
        expected_series = pd.Series([5, 10], index=[1, 2])
        pd.testing.assert_series_equal(result, expected_series)
