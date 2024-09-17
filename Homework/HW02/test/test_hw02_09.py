
from solution_2_9 import count_students_above_threshold

import unittest

class TestHW0209(unittest.TestCase):
    def setUp(self):
        self.averages = {
        "Alice": 84.33,
        "Bob": 83.33,
        "Charlie": 83.33,
        "David": 97.67
        }
        self.threshold = 84
        
    def test_hw02_08(self):
        result = count_students_above_threshold(self.averages, self.threshold)
        self.assertEqual(result, 2)
        
