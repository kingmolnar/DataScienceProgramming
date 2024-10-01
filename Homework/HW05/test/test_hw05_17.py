
from solution_5_17 import correlation_with_series

import unittest
import pandas as pd
import numpy as np

class TestHW0520(unittest.TestCase):
    def test_correlation_with_series(self):
        df = pd.DataFrame({
            'A': np.random.randn(100),
            'B': np.random.randn(100) * 100
        })
        series = pd.Series(np.random.randn(100))
        result = correlation_with_series(df, series)
        expected_series = pd.Series({
            'A': df['A'].corr(series),
            'B': df['B'].corr(series)
        })
        pd.testing.assert_series_equal(result, expected_series)
        
