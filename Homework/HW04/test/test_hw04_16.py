
from solution_4_16 import matrix_multiplication
import unittest
import numpy as np

class TestHW0416(unittest.TestCase):
    def test_matrix_multiplication(self):
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[2, 0], [1, 2]])
        result = matrix_multiplication(A, B)
        expected = np.array([[4, 4], [10, 8]])
        np.testing.assert_array_equal(result, expected)
