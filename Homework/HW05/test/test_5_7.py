import pandas as pd

def test_5_7():
    result = pd.read_csv('penguins_5_7.csv')
    assert result.sex.sum() == 168,  'Encoding is incorrect'
