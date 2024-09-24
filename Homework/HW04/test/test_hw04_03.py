
from solution_4_3 import add_arrays
import unittest
import numpy as np

class TestHW0403(unittest.TestCase):
    def test_add_arrays(self):
        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])
        result = add_arrays(a, b)
        expected = np.array([5, 7, 9])
        np.testing.assert_array_equal(result, expected)
