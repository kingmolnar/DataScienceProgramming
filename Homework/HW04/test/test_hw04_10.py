
from solution_4_10 import sqrt_and_square
import unittest
import numpy as np

class TestHW0410(unittest.TestCase):
    def test_sqrt_and_square(self):
        arr = np.array([1, 4, 9, 16])
        sqrt_result, square_result = sqrt_and_square(arr)
        np.testing.assert_array_almost_equal(sqrt_result, np.array([1., 2., 3., 4.]), decimal=5)
        np.testing.assert_array_almost_equal(square_result, np.array([1, 16, 81, 256]), decimal=5)
