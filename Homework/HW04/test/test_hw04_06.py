
from solution_4_6 import select_second_column
import unittest
import numpy as np

class TestHW0406(unittest.TestCase):
    def test_select_second_column(self):
        arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        result = select_second_column(arr)
        expected = np.array([2, 5, 8])
        np.testing.assert_array_equal(result, expected)
