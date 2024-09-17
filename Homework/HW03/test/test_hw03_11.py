
from solution_3_11 import is_even
import unittest

class TestIsEven10(unittest.TestCase):
    def test_is_even_10(self):
        # Test specifically for the number 10
        self.assertTrue(is_even(10), "Test failed: 10 should be even")
