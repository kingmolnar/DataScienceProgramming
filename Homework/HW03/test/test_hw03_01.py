
from solution_3_1 import get_middle_elements

import unittest

class TestHW0301(unittest.TestCase):
    def setUp(self):
        self.numbers = (10, 20, 30, 40, 50)

    def test_hw03_01(self):
        results = get_middle_elements(self.numbers)
        self.assertCountEqual(results, (20, 30, 40))
