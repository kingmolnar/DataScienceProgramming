import numpy as np
from solution_5_1 import matrix_manipulation

def test_5_1():
    matrix = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])
    
    result = matrix_manipulation(matrix)
    
    assert np.array_equal(result['transpose'], np.array([[1, 4, 7], [2, 5, 8], [3, 6, 9]])), "Transpose is incorrect"
    assert np.isclose(result['determinant'], 0.0), "Determinant is incorrect"
    assert result['trace'] == 15, "Trace is incorrect"
    assert np.allclose(result['eigenvalues'], np.array([16.116844, -1.116844, 0.0])), "Eigenvalues are incorrect"
