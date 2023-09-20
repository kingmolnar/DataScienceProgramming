import os
import solution_4_7
import numpy as np

def test_4_7():
    assert 'matrix1' in dir(solution_4_7), "`matrix1` is not defined"
    matrix1 = solution_4_7.matrix1

    assert 'matrix2' in dir(solution_4_7), "`matrix2` is not defined"
    matrix2 = solution_4_7.matrix2

    assert 'matrix_product' in dir(solution_4_7), "`matrix_product` is not defined"
    matrix_product = solution_4_7.matrix_product

    assert str(type(matrix1)) == "<class \'numpy.ndarray\'>", "Incorrect type matrix1"
    assert str(type(matrix2)) == "<class \'numpy.ndarray\'>", "Incorrect type matrix2"
    assert str(type(matrix_product)) == "<class \'numpy.ndarray\'>", "Incorrect type matrix_product"

    assert np.allclose(matrix_product, np.dot(matrix1, matrix2)), "Incorrect dot product"
