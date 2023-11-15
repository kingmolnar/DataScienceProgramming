import pandas as pd
import hashlib

def test_7_20():
    result = pd.read_csv('tips_7_20.csv')
    assert result.shape == (2, 1), "Invalid shape"
    # row1 = result.iloc[0,:].to_list()
    # row2 = result.iloc[1,:].to_list()
    # assert hashlib.sha256(str(row1).encode('utf-8')).hexdigest() == '6aa4cac00d7f817e536f4c81ed042abd382ff650672548bc61018ae8e54051ff',  'First row values are incorrect'
    # assert hashlib.sha256(str(row2).encode('utf-8')).hexdigest() == '090da858c78829659c5de6ed2afac3c017649c2865bf49f80a497b389ad2c75d',  'Second row values are incorrect'
