
from solution_2_7 import find_highest_lowest_student

import unittest

class TestHW0207(unittest.TestCase):
    def setUp(self):
        self.averages = {
        "Alice": 84.33,
        "Bob": 83.33,
        "Charlie": 83.33,
        "David": 97.67
        }
        
    def test_hw02_07(self):
        student1, score1, student2, score2 = find_highest_lowest_student(self.averages)
        self.assertEqual(student1, 'David')
        self.assertEqual(score1, 97.67)
        self.assertEqual(student2, 'Bob')
        self.assertEqual(score2, 83.33)
