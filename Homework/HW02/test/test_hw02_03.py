
from solution_2_3 import top_students
    
import unittest

class TestHW0204(unittest.TestCase):
    def setUp(self):
        self.averages = {
            "Alice": 84.33,
            "Bob": 83.33,
            "Charlie": 83.33,
            "David": 97.67
        }
        self.overall_average = 87.165
        
    def test_hw02_03(self):
        results = top_students(self.averages, self.overall_average)
        self.assertCountEqual(results, ["David"])
