import os
import solution_4_8
import numpy as np

def test_4_8():
    assert 'matrix3' in dir(solution_4_8), "`matrix3` is not defined"
    matrix3 = solution_4_8.matrix3

    assert 'eigenvalues' in dir(solution_4_8), "`eigenvalues` is not defined"
    eigenvalues = solution_4_8.eigenvalues

    assert 'eigenvectors' in dir(solution_4_8), "`eigenvectors` is not defined"
    eigenvectors = solution_4_8.eigenvectors

    assert str(type(matrix3)) == "<class 'numpy.ndarray'>", "Incorrect type matrix3"
    assert str(type(eigenvalues)) == "<class 'numpy.ndarray'>", "Incorrect type eigenvalues"
    assert str(type(eigenvectors)) == "<class 'numpy.ndarray'>", "Incorrect type eigenvectors"

    eigenvalues_computed, eigenvectors_computed = np.linalg.eig(matrix3)

    assert np.allclose(eigenvalues, eigenvalues_computed), "Incorrect eigenvalues"
    assert np.allclose(eigenvectors, eigenvectors_computed), "Incorrect eigenvectors"

    assert 'determinant' in dir(solution_4_8), "`determinant` is not defined"
    determinant = solution_4_8.determinant
    assert str(type(determinant)) == "<class 'numpy.float64'>", "Incorrect type determinant"
    determinant_computed = np.linalg.det(matrix3)
    assert np.allclose(determinant, determinant_computed), "Incorrect determinant"

    assert 'transpose' in dir(solution_4_8), "`transpose` is not defined"
    transpose = solution_4_8.transpose
    assert str(type(transpose)) == "<class 'numpy.ndarray'>", "Incorrect type transpose"

    assert np.allclose(transpose, np.transpose(matrix3)), "Incorrect transpose"
