
from solution_4_8 import transpose_and_swap
import unittest
import numpy as np

class TestHW0408(unittest.TestCase):
    def test_transpose_and_swap(self):
        arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
        result = transpose_and_swap(arr)
        expected = np.array([[[1, 3], [2, 4]], [[5, 7], [6, 8]]])
        np.testing.assert_array_equal(result, expected)
