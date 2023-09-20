import os
import solution_4_9
import numpy as np


def test_4_9():
    assert 'matrix4' in dir(solution_4_9), "`matrix4` is not defined"
    matrix4 = solution_4_9.matrix4
    assert str(type(matrix4)) == "<class 'numpy.ndarray'>", "Incorrect type matrix4"

    try:
        assert 'inverse_matrix' in dir(solution_4_9), "`inverse_matrix` is not defined"
        inverse_matrix = solution_4_9.inverse_matrix
        assert str(type(inverse_matrix)) == "<class 'numpy.ndarray'>", "Incorrect type inverse_matrix"
        assert np.allclose(inverse_matrix, np.linalg.inv(matrix4)), "Matrix inversion is incorrect"

    except:
        res = os.popen("python3 solution_4_9.py").read().strip()
        assert res == 'Matrix is not invertible.', "Matrix inversion handling is incorrect"
