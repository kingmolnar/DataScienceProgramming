
from solution_5_2 import create_and_slice_dataframe

import unittest
import pandas as pd

class TestHW0502(unittest.TestCase):
    def test_create_and_slice_dataframe(self):

        expected_data = {
            'Column1': [1, 2, 3],
            'Column2': [6, 7, 8],
            'Column3': [11, 12, 13]
        }
        result = create_and_slice_dataframe(expected_data)
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(result, expected_df)
