
from solution_4_17 import matrix_arithmatic
import numpy as np
import unittest

class TestHW0417(unittest.TestCase):
    def test_matrix_arithmatic(self):
        addition_result, subtraction_result, multiplication_result, division_result = matrix_arithmatic()
        expected_addition_result = np.array([12, 24, 36, 48, 60])
        expected_subtraction_result = np.array([ 8, 16, 24, 32, 40])
        expected_multiplication_result = np.array([ 20, 80, 180, 320, 500])
        expected_division_result = np.array([5., 5., 5., 5., 5.])
        np.testing.assert_array_equal(addition_result, expected_addition_result)
        np.testing.assert_array_equal(subtraction_result, expected_subtraction_result)
        np.testing.assert_array_equal(multiplication_result, expected_multiplication_result)
        np.testing.assert_array_equal(division_result, expected_division_result)
