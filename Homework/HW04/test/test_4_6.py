import os
import solution_4_6
import numpy as np

def test_4_6():
    assert 'vector1' in dir(solution_4_6), "`vector1` is not defined"
    vector1 = solution_4_6.vector1

    assert 'vector2' in dir(solution_4_6), "`vector2` is not defined"
    vector2 = solution_4_6.vector2

    assert 'dot_product' in dir(solution_4_6), "`dot_product` is not defined"
    dot_product = solution_4_6.dot_product

    assert str(type(vector1)) == "<class \'numpy.ndarray\'>", "Incorrect type vector1"
    assert str(type(vector2)) == "<class \'numpy.ndarray\'>", "Incorrect type vector2"
    assert str(type(dot_product)) == "<class \'numpy.int64\'>", "Incorrect type dot_product"

    assert dot_product == np.dot(vector1, vector2), "Incorrect dot product"
