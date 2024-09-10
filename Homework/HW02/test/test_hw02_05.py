
from solution_2_5 import aggregate_grade_distribution

import unittest

class TestHW0205(unittest.TestCase):
    def setUp(self):
        self.grades = {'Alice': 'B', 'Bob': 'B', 'Charlie': 'B', 'David': 'A'}
        
    def test_hw02_05(self):
        results = aggregate_grade_distribution(self.grades)
        self.assertEqual(results['B'], 3)
        self.assertEqual(results['A'], 1)
