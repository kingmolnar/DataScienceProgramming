
from solution_5_7 import select_rows_with_loc

import unittest
import pandas as pd

class TestHW0507(unittest.TestCase):
    def test_select_rows_with_loc(self):
        data = {'a': 1, 'b': 5, 'c': 10, 'd': 15}
        start_label = 'b'
        end_label = 'd'
        result = select_rows_with_loc(data, start_label, end_label)
        expected_data = {'b': 5, 'c': 10, 'd': 15}
        expected_series = pd.Series(expected_data)
        pd.testing.assert_series_equal(result, expected_series)
        
