import pandas as pd

def test_7_22():
    result = pd.read_csv('penguins_7_22.csv')
    assert result.sex.sum() == 168,  'Encoding is incorrect'
