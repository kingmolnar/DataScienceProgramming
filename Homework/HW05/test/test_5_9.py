import pandas as pd

def test_5_9():
    Y = pd.read_csv('penguins_5_9_Y.csv')
    X =pd.read_csv('penguins_5_9_X.csv')
    y_shape=(333, 1)
    x_shape=(333, 8)
    assert Y.shape == y_shape,  'Splitting Y is incorrect'
    assert X.shape == x_shape,  'Splitting X is incorrect'
