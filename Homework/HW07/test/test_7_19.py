import pandas as pd
import hashlib

def test_7_19():
    result = pd.read_csv('tips_7_19.csv')
    row1 = result.iloc[0,:].to_list()
    row2 = result.iloc[1,:].to_list()
    assert hashlib.sha256(str(row1).encode('utf-8')).hexdigest() == 'f85a507bbb4723fca99e53fe8ebd8e98941040466a53f883fadf36f09313ace3',  'First row values are incorrect'
    assert hashlib.sha256(str(row2).encode('utf-8')).hexdigest() == 'cb37e4bba90e249d1e6bf22314651659002ea405f82d605aa94c52e6a3f57a73',  'Second row values are incorrect'
