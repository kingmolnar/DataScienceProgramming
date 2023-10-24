import pandas as pd

def test_6_10():
    df = pd.read_csv('athlete_events_6_10.csv')
    assert df.shape == (271116, 16), 'The shape of the new dataframe is incorrect.'
    assert len(df.Olympics[0].split()) == 3 or len(df.Olympics[0].split()) == 4, 'The new column created has incorrect values'
