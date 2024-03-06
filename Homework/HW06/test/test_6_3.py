import numpy as np
from solution_6_3 import concat_feature_matrix

def test_6_3():
    m1 = np.random.rand(100, 16)
    m2 = np.random.rand(100, 4)
    m = concat_feature_matrix(m1, m2)
    assert isinstance(m, np.ndarray)
    assert m.shape[0] == 100, "Invalid number of rows"
    assert m.shape[1] == 20, "Invalid number of columns"
