import pandas as pd 
from solution_5_15 import find_statistics

def test_5_15():
    result = find_statistics()
    assert round(result['mean'],3) == 5.755, "Mean is incorrect"
    assert result['median'] == 0,  "median is incorrect"
    assert result['max'] == 36542,  "Max is incorrect"
    assert result['min'] == 0,  "Min is incorrect"
