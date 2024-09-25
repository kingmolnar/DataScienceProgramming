
from solution_4_7 import positive_elements
import unittest
import numpy as np

class TestHW0407(unittest.TestCase):
    def test_positive_elements(self):
        arr = np.array([1, -1, 2, -2, 3, -3])
        result = positive_elements(arr)
        expected = np.array([1, 2, 3])
        np.testing.assert_array_equal(result, expected)
