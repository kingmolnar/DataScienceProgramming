import pandas as pd
import hashlib

def test_7_11():
    result = pd.read_csv('penguins_7_11.csv')
    row1 = result.iloc[0,:].to_list()
    row3 = result.iloc[2,:].to_list()
    assert hashlib.sha256(str(row1).encode('utf-8')).hexdigest() == 'ba34f72f882c43bfbe6012d8105b2affba5b85b01de5b16355e1ba6b098effe0',  'First row values are incorrect'
    assert hashlib.sha256(str(row3).encode('utf-8')).hexdigest() == 'df17bcda3225cb34bfc0996825ceb754e8496ab8a64f249d7fbaf7eb2bb188b8',  'Third row values are incorrect'
