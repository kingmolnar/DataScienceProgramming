
from solution_4_2 import array_with_dtype
import unittest
import numpy as np

class TestHW0402(unittest.TestCase):
    def test_array_with_dtype(self):
        result = array_with_dtype()
        expected = np.array([[1, 2], [3, 4]], dtype=float)
        np.testing.assert_array_equal(result, expected)
