import pandas as pd 

def test_5_12():
    df = pd.read_csv('adp_5_12.csv')
    assert df.loc_type.isnull().sum() == 0, 'There are still missing values in that column'
