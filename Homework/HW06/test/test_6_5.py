from solution_6_5 import find_statistics

def test_6_5():
    result = find_statistics()
    assert result['mean'] == 25.56, 'Mean is incorrect'
    assert result['median'] == 24.0, 'Median is incorrect'
    assert result['max'] == 97.0, 'Max is incorrect'
    assert result['min'] == 10.0, 'Min is incorrect'
