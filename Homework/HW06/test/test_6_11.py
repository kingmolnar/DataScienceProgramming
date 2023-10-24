import pandas as pd

def test_6_11():
    df = pd.read_csv('netflix_6_11.csv')
    assert df.shape == (8790, 74), 'The shape of the new dataframe is incorrect.'
    assert df['title'][0] == 'Dick Johnson Is Dead', 'The title column has incorrect first row'
