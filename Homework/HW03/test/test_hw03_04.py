
from solution_3_4 import sort_by_length
import unittest

class TestHW0304(unittest.TestCase):
    def setUp(self):
        self.words = ["apple", "banana", "kiwi", "blueberry", "fig"]

    def test_hw03_04(self):
        results = sort_by_length(self.words)
        self.assertEqual(results, ['fig', 'kiwi', 'apple', 'banana', 'blueberry'])

