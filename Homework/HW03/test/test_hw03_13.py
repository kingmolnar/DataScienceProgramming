
from solution_3_13 import line_count
import unittest

class TestHW0313(unittest.TestCase):
    def setUp(self):
        self.path = 'input_3.13.txt'

    def test_line_count(self):
        result = line_count(self.path)
        self.assertEqual(result, 5, "Test failed: There should be 3 lines")
