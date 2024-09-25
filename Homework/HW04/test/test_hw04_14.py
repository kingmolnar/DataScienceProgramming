
from solution_4_14 import analyze_boolean_array
import unittest
import numpy as np

class TestHW0414(unittest.TestCase):
    def test_analyze_boolean_array(self):
        arr = np.array([True, False, True, False, True])
        true_count, any_true, all_true = analyze_boolean_array(arr)
        self.assertEqual(true_count, 3)
        self.assertTrue(any_true)
        self.assertFalse(all_true)
