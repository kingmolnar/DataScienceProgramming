import os
import solution_4_14
import numpy as np

def test_4_14():
    assert 'A' in dir(solution_4_14), "`A` is not defined"
    A = solution_4_14.A

    assert 'B' in dir(solution_4_14), "`B` is not defined"
    B = solution_4_14.B

    assert 'x' in dir(solution_4_14), "`x` is not defined"
    x = solution_4_14.x


    expected_A = np.array([[2, -1, 3],
              [1, 2, 1],
              [3, 3, 5]])

    expected_B = np.array([5, 4, 12])

    expected_x = np.array([1.        , 0.85714286, 1.28571429])

    assert str(type(A)) == "<class \'numpy.ndarray\'>", "Incorrect type A"
    assert str(type(B)) == "<class \'numpy.ndarray\'>", "Incorrect type B"
    assert str(type(x)) == "<class \'numpy.ndarray\'>", "Incorrect type x"

    assert np.allclose(A, expected_A), "Incorrect A matrix"
    assert np.allclose(B, expected_B), "Incorrect B vector"
    assert np.allclose(x, expected_x), "Incorrect x vector"


