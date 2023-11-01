import pandas as pd
import hashlib

def test_7_14():
    result = pd.read_csv('flights_7_14.csv')
    row1 = result.iloc[0,:].to_list()
    row3 = result.iloc[2,:].to_list()
    assert hashlib.sha256(str(row1).encode('utf-8')).hexdigest() == '6551d358629f3f14ab3549dc9f62c4b07564aee9fdb8d60e572b1aabf99a3695',  'First row values are incorrect'
    assert hashlib.sha256(str(row3).encode('utf-8')).hexdigest() == '4ac96044310135251f494e2fc0b6e3ae7ff81b060276c4f4b0e07c8837f3fff3',  'Third row values are incorrect'
