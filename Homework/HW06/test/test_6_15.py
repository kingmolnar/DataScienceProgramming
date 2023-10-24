from solution_6_15 import *

def test_6_15():
    result = join_dataframes()
    assert result.shape == (7042, 21), 'Incorrect resulting shape'
