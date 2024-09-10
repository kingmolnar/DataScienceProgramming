
from solution_2_10 import split_string

import unittest

class TestHW0210(unittest.TestCase):
    def setUp(self):
        self.s = "Hello there Joseph!"
        
    def test_hw02_10(self):
        result_list = split_string(self.s)
        self.assertCountEqual(result_list, ["Hello", "there", "Joseph!"])
