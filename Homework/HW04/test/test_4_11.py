import os
from solution_4_11 import swap_rows_and_columns
import numpy as np

def test_4_11():

    matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

    expected_result = np.array([[1, 3, 2],
                   [7, 9, 8],
                   [4, 6, 5]])

    result_matrix = swap_rows_and_columns(matrix, 1, 2)

    assert np.allclose(result_matrix, expected_result), "Incorrect Result"

