import pandas as pd

def test_7_24():
    Y = pd.read_csv('penguins_7_24_Y.csv')
    X =pd.read_csv('penguins_7_24_X.csv')
    y_shape=(333, 1)
    x_shape=(333, 8)
    assert Y.shape == y_shape,  'Splitting Y is incorrect'
    assert X.shape == x_shape,  'Splitting X is incorrect'
