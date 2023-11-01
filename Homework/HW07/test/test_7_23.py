import pandas as pd

def test_7_23():
    result = pd.read_csv('penguins_7_23.csv')
    shape=(333, 9)
    assert result.shape == shape,  'Encoding is incorrect'
