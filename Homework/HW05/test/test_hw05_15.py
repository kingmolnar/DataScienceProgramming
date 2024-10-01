
from solution_5_15 import get_dataframe_statistics

import unittest
import pandas as pd
import numpy as np

class TestHW0515(unittest.TestCase):
    def test_get_dataframe_statistics(self):
        df = pd.DataFrame({
            'A': np.random.randn(100),
            'B': np.random.randint(0, 100, 100)
        })
        result = get_dataframe_statistics(df)
        expected_df = df.describe()
        pd.testing.assert_frame_equal(result, expected_df)
