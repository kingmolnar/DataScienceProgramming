import pandas as pd

def test_6_3():
    df = pd.read_csv('athlete_events_6_3.csv')
    assert df.shape == (271116, 11), 'The shape of the new dataframe is incorrect.'
