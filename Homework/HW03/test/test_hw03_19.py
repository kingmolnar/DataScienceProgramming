
from solution_3_19 import concatenate_matrices

import os
import numpy as np

def test_3_19():
    matrix1 = np.array([[1, 2],
                      [3, 4]])

    matrix2 = np.array([[5, 6],
                      [7, 8]])

    matrix3 = np.array([[9, 10, 11],
                      [12, 13, 14]])

    result_horizontal = concatenate_matrices(matrix1, matrix2)
    result_vertical = concatenate_matrices(matrix1, matrix3)
    result_invalid = concatenate_matrices(matrix3, np.array([[1, 2], [5, 6], [8, 6]]))

    expected_horizontal = np.array([[1,2, 5, 6],
                                [3, 4, 7, 8]])

    expected_vertical = np.array([[ 1 , 2,  9, 10, 11],
                              [ 3, 4, 12, 13, 14]])

    expected_invalid = "Concatenation not possible: Dimensions do not match."

    assert np.allclose(result_horizontal, expected_horizontal), "Incorrect Horizontal Concatination"
    assert np.allclose(result_vertical, expected_vertical), "Incorrect Veritical Concatination"
    assert result_invalid == expected_invalid, "Incorrect Concatination: Invalid"
