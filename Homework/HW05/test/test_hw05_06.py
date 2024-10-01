
from solution_5_6 import subset_series

import unittest
import pandas as pd

class TestHW0506(unittest.TestCase):
    def test_subset_series(self):
        data = {'a': 1, 'b': 5, 'c': 10, 'd': 15}
        index_labels = ['b', 'c', 'd']  
        value_condition = 6  

        result = subset_series(data, index_labels, value_condition)
        expected_data = {'c': 10, 'd': 15}
        expected_series = pd.Series(expected_data)

        pd.testing.assert_series_equal(result, expected_series)
