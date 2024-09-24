
from solution_4_12 import apply_conditions
import unittest
import numpy as np

class TestHW0412(unittest.TestCase):
    def test_apply_conditions(self):
        a = np.array([1, 2, 3, 4, 5])
        cond = np.array([True, False, True, False, True])
        b = np.array([5, 4, 3, 2, 1])
        result = apply_conditions(a, cond, b)
        expected = np.array([1, 4, 3, 2, 5])
        np.testing.assert_array_equal(result, expected)
