import pandas as pd

def test_5_19():
    result = pd.read_csv('penguins_5_19.csv')
    assert result.sex.sum() == 168,  'Encoding is incorrect'
