
from solution_5_3 import create_dataframe_from_nested_dict

import unittest
import pandas as pd

class TestHW0503(unittest.TestCase):
    def test_create_dataframe_from_nested_dict(self):
        nested_dict = {
            'item1': {'a': 1, 'b': 2},
            'item2': {'a': 3, 'c': 4}
        }
        result = create_dataframe_from_nested_dict(nested_dict)
        expected_data = {
            'a': [1, 3],
            'b': [2, 0.0],  
            'c': [0.0, 4]
        }
        expected_df = pd.DataFrame(expected_data, index=['item1', 'item2'])
        pd.testing.assert_frame_equal(result, expected_df)
        
