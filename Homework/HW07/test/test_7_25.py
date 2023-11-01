import pandas as pd

def test_7_25():
    X_train= pd.read_csv('penguins_7_25_X_train.csv')
    X_test= pd.read_csv('penguins_7_25_X_test.csv')
    Y_train= pd.read_csv('penguins_7_25_Y_train.csv')
    Y_test= pd.read_csv('penguins_7_25_Y_test.csv')

    X_train_shape=(233, 8)
    X_test_shape= (100, 8)
    Y_test_shape=(100, 1)
    Y_train_shape= (233, 1)

    assert X_train.shape == X_train_shape,  'Splitting X_train is incorrect'
    assert X_test.shape == X_test_shape,  'Splitting X_test is incorrect'
    assert Y_train.shape == Y_train_shape, 'Splitting Y_train is incorrect'
    assert Y_test.shape == Y_test_shape,  'Splitting  Y_test_ is incorrect'
