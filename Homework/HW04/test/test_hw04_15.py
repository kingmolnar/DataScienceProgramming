
from solution_4_15 import sort_array
import unittest
import numpy as np

class TestHW0415(unittest.TestCase):
    def test_sort_array(self):
        arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        result = sort_array(arr)
        expected = np.array([1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
        np.testing.assert_array_equal(result, expected)

        arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        result = sort_array(arr, ascending=False)
        expected = np.array([9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1])
        np.testing.assert_array_equal(result, expected)