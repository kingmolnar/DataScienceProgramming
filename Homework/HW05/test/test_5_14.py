import pandas as pd 

def test_5_14():
    df = pd.read_csv('adp_5_14.csv')
    assert df.date_diff.dtype == 'int64', 'Incorrect data type'
