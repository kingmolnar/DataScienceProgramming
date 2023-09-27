import pandas as pd 

def test_5_13():
    df = pd.read_csv('adp_5_13.csv')
    assert df.shape[0] == 4467, 'Incorrect number of rows have been dropped'
