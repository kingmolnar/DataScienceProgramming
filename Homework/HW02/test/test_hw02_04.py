
from solution_2_4 import map_scores_to_grades

import unittest

class TestHW0204(unittest.TestCase):
    def setUp(self):
        self.averages = {
            "Alice": 84.33,
            "Bob": 83.33,
            "Charlie": 83.33,
            "David": 97.67
        }
        
    def test_hw02_04(self):
        results = map_scores_to_grades(self.averages)
        self.assertEqual(results['Alice'], 'B')
        self.assertEqual(results['Charlie'], 'B')
