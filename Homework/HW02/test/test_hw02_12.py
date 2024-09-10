
from solution_2_12 import filter_sequence

import unittest

class TestHW0212(unittest.TestCase):
    def setUp(self):
        self.seq = ['soup','dog','salad','cat','great']
            
    def test_hw02_12(self):
        result_list = filter_sequence(self.seq)
        self.assertCountEqual(result_list, ['soup','salad'])
