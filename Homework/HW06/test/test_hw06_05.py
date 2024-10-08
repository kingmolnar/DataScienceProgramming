
from solution_6_5 import permute_rows_with_replacement
import unittest
import pandas as pd

class TestHW0605(unittest.TestCase):
    def test_permute_rows_with_replacement(self):
        data = {
            'Movie': ['Inception', 'Titanic', 'The Matrix', 'Avengers', 'Gladiator'],
            'Rating': [8.8, 7.8, 8.7, 8.4, 8.5],
            'Year': [2010, 1997, 1999, 2012, 2000]
        }
        df7 = pd.DataFrame(data)

        result = permute_rows_with_replacement(df7)

        # Check if the result has the same length as the original DataFrame
        self.assertEqual(len(result), len(df7))

        # Check if the output contains only valid movies from the original dataset
        for movie in result['Movie']:
            self.assertIn(movie, df7['Movie'].values)
