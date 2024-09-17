
from solution_3_3 import append_to_list

import unittest

class TestHW0303(unittest.TestCase):
    def setUp(self):
        self.fruits = ["apple", "banana", "orange"]
        self.item = "grape"

    def test_hw03_03(self):
        results = append_to_list(self.fruits, self.item)
        self.assertCountEqual(results, ["apple", "banana", "orange", "grape"])
