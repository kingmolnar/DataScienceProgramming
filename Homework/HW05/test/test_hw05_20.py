import pandas as pd

def test_5_20():
    result = pd.read_csv('penguins_5_20.csv')
    shape=(333, 9)
    assert result.shape == shape,  'Encoding is incorrect'
