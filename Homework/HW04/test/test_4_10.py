import solution_4_10
import numpy as np

def test_4_10():
    assert 'A' in dir(solution_4_10), "`A` is not defined"
    A = solution_4_10.A

    assert 'B' in dir(solution_4_10), "`B` is not defined"
    B = solution_4_10.B

    assert 'X' in dir(solution_4_10), "`X` is not defined"
    X = solution_4_10.X

    assert str(type(A)) == "<class 'numpy.ndarray'>", "Incorrect type A"
    assert str(type(B)) == "<class 'numpy.ndarray'>", "Incorrect type B"
    assert str(type(X)) == "<class 'numpy.ndarray'>", "Incorrect type X"


    assert np.allclose(X, np.linalg.solve(A, B)), "Incorrect X"
