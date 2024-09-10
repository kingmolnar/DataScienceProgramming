
from solution_2_8 import sort_students_by_score

import unittest

class TestHW0208(unittest.TestCase):
    def setUp(self):
        self.averages = {
        "Alice": 84.33,
        "Bob": 83.33,
        "Charlie": 83.33,
        "David": 97.67
        }
        
    def test_hw02_08(self):
        result = sort_students_by_score(self.averages)
        sorted_list = [
            ("David", 97.67),
            ("Alice", 84.33),
            ("Bob", 83.33),
            ("Charlie", 83.33)
            ]
        self.assertCountEqual(result, sorted_list)
