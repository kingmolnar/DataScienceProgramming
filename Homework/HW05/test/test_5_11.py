from solution_5_11 import find_missingvalues

def test_5_11():
    result = find_missingvalues()
    assert len(result) == 23, 'The lenght of list provided is incorrect'
    expected_result = [0, 0, 0, 0, 4, 0, 4, 0, 17061, 14422, 0, 0, 1, 14953, 50, 0, 0, 2160,
                         0, 779, 189, 0, 0]
    assert result == expected_result, 'The output provided is incorrect'
