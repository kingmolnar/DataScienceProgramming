import os
from solution_4_13 import scale_row
import numpy as np

def test_4_13():

    matrix = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

    scaled_matrix = scale_row(matrix, 1, 2)
    scaled_matrix_invalid = scale_row(matrix, 5, 2)

    expected_scaled_matrix = np.array([[ 1 ,2, 3],
                          [ 8 ,10, 12],
                          [ 7, 8 , 9]])

    expected_invalid = "Row not valid."


    assert np.allclose(scaled_matrix, expected_scaled_matrix), "Incorrect scaled matrix"
    assert scaled_matrix_invalid == expected_invalid, "Incorrect Invalid Row handling"
