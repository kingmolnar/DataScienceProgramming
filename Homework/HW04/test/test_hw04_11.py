
from solution_4_11 import add_and_multiply
import unittest
import numpy as np

class TestHW0411(unittest.TestCase):
    def test_add_and_multiply(self):
        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])
        added_result, multiplied_result = add_and_multiply(a, b)
        np.testing.assert_array_equal(added_result, np.array([5, 7, 9]))
        np.testing.assert_array_equal(multiplied_result, np.array([4, 10, 18]))
