
from solution_5_16 import column_statistics

import unittest
import pandas as pd

class TestHW0516(unittest.TestCase):
    def test_column_statistics(self):
        df = pd.DataFrame({
            'A': [10, 20, 30, 40, 50],
            'B': [15, 25, 35, 45, 55]
        })
        result = column_statistics(df, 'B')
        expected_stats = [
            5, 15, 55, 0, 4, 
            175, 35, 35, 250, 15.811388300841896
        ]
        # self.assertEqual(result, expected_stats)
        self.assertAlmostEqual(result, expected_stats, 5)
        
