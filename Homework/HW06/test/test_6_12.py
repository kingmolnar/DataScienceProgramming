from solution_6_12 import *

def test_6_12():
    result = find_movie()
    assert len(result) == 1, 'Incorrect lenght of list'
    assert result[0] == 'Boy and the World' , 'Incorrect answer'
