
from solution_6_10 import convert_to_category
import unittest
import pandas as pd
import numpy as np

class TestHW0610(unittest.TestCase):
    def test_convert_to_category(self):
        # Test case 1
        animals = ['cat', 'dog', 'elephant', 'dog', 'elephant', 'cat', 'lion', 'tiger', 'lion', 'dog']
        df15 = pd.DataFrame({
            'Animal': animals,
            'Age': np.random.randint(1, 15, size=len(animals)),
            'Weight': np.random.uniform(5, 100, size=len(animals))
        })

        categories_dict, category_counts = convert_to_category(df15)

        # expected_categories_dict = {0: 'cat', 1: 'dog', 2: 'elephant', 3: 'lion', 4: 'tiger'}
        expected_category_counts = {
            'dog': 3,
            'cat': 2,
            'elephant': 2,
            'lion': 2,
            'tiger': 1
        }
                
        # self.assertEqual(categories_dict, expected_categories_dict)
        self.assertDictEqual(category_counts, expected_category_counts)
