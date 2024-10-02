
from solution_5_4 import add_dataframes_as_arrays

import unittest
import pandas as pd
import numpy as np

class TestHW0504(unittest.TestCase):
    def test_add_dataframes_as_arrays(self):
        # Create sample DataFrames
        data1 = {
            'Column1': [1, 2, 3],
            'Column2': [4, 5, 6]
        }
        data2 = {
            'Column1': [10, 20, 30],
            'Column2': [40, 50, 60]
        }
        df1 = pd.DataFrame(data1)
        df2 = pd.DataFrame(data2)
        result = add_dataframes_as_arrays(df1, df2)
        expected_array = np.array([[11, 44], [22, 55], [33, 66]])
        np.testing.assert_array_equal(result, expected_array)
        
