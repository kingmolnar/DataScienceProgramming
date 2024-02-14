from solution_4_1 import *
import pandas as pd

def test_4_1():
    result = groupby_object()
    assert result == pd.core.groupby.generic.DataFrameGroupBy,  'Incorrect type of the groupby object'
