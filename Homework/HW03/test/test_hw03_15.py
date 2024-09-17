
import unittest
from solution_3_15 import get_min_max

class TestGetMinMax(unittest.TestCase):
    def test_get_min_max(self):
        # Specific list of numbers
        numbers_list = [4, 11, 42, 2, 56, 28]
        min_value, max_value = get_min_max(numbers_list)
        self.assertEqual(min_value, 2, "The minimum value should be 2")
        self.assertEqual(max_value, 56, "The maximum value should be 56")
