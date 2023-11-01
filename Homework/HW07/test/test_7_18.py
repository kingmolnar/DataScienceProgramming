import pandas as pd
import hashlib

def test_7_18():
    result = pd.read_csv('tips_7_18.csv')
    row1 = result.iloc[0,:].to_list()
    row2 = result.iloc[1,:].to_list()
    assert hashlib.sha256(str(row1).encode('utf-8')).hexdigest() == 'a354cf464d659749493430aac43cbd297ba8f24d3eb49682a018e71b6ef963e0',  'First row values are incorrect'
    assert hashlib.sha256(str(row2).encode('utf-8')).hexdigest() == '29d3e0b0a5e3610c479a72bd722c547f3c02aa1508f884768a0d775fcec4a0d5',  'Second row values are incorrect'
