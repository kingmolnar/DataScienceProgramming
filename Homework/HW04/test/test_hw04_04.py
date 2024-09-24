
from solution_4_4 import multiply_elementwise
import unittest
import numpy as np

class TestHW0404(unittest.TestCase):
    def test_multiply_elementwise(self):
        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])
        result = multiply_elementwise(a, b)
        expected = np.array([4, 10, 18])
        np.testing.assert_array_equal(result, expected)
