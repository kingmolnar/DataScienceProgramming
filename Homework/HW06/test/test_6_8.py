import pandas as pd

def test_6_8():
    df = pd.read_csv('athlete_events_6_8.csv')
    assert df.shape == (271116, 35), 'The shape of the new dataframe is incorrect.'
