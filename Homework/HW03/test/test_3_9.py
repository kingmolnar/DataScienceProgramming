from solution_3_9 import solve_linear_equation
import numpy as np

def test_3_9():

    A = np.array([[2, -1, 3],
              [1, 2, 1],
              [3, 3, 5]])

    B = np.array([5, 4, 12])

    expected_x = np.array([1. , 0.85714286, 1.28571429])
    success, x = solve_linear_equation(A, B)
    assert success, "This example should be solvable"
    assert str(type(x)) == "<class \'numpy.ndarray\'>", "Incorrect type x"
    assert np.allclose(x, expected_x), "Incorrect x vector"

