
from solution_2_11 import slice_nest

import unittest

class TestHW0211(unittest.TestCase):
    def setUp(self):
        self.nest = [1, 2, 3, [4, 5, ['target']]]
        
    def test_hw02_11(self):
        result = slice_nest(self.nest)
        self.assertEqual(result, 'target')
