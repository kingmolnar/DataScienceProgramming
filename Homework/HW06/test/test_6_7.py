import pandas as pd

def test_6_7():
    df = pd.read_csv('athlete_events_6_7.csv')
    assert df.shape == (13, 15), 'The shape of the new dataframe is incorrect.'
    assert round(df.Age.mean(), 2) == 84.38, 'The data inside the dataframe is incorrect'
