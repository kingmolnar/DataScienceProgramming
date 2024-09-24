
from solution_4_5 import slice_array
import unittest
import numpy as np

class TestHW0405(unittest.TestCase):
    def test_slice_array(self):
        arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        result = slice_array(arr)
        expected = np.array([[1, 2], [4, 5]])
        np.testing.assert_array_equal(result, expected)
