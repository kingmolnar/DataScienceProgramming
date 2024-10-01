
from solution_5_1 import create_series_with_extra_index

import unittest
import pandas as pd
import numpy as np  # Import numpy for using np.nan if necessary

class TestHW0501(unittest.TestCase):
    def test_create_series_with_extra_index(self):
        data_dict = {'a': 1, 'b': 2}
        extra_key = 'c'
        result = create_series_with_extra_index(data_dict, extra_key)
        
        # Expected Series has the extra key with NaN as its value
        expected_index = ['a', 'b', 'c']
        expected_values = [1, 2, np.nan]  # Using np.nan to match typical float handling
        expected_series = pd.Series(expected_values, index=expected_index, dtype='float64')
        
        # Use pd.testing.assert_series_equal to compare the result and expected Series
        pd.testing.assert_series_equal(result, expected_series)
