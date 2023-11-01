import pandas as pd

def test_7_21():
    result = pd.read_csv('penguins_7_21.csv')
    assert result.isna().sum().sum() == 0,  'Dataframe has nulls'
