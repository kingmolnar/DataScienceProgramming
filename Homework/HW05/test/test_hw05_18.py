import pandas as pd

def test_5_18():
    result = pd.read_csv('penguins_5_18.csv')
    assert result.isna().sum().sum() == 0,  'Dataframe has nulls'
