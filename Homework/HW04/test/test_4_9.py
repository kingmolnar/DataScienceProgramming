import pandas as pd
import hashlib

def test_4_9():
    result = pd.read_csv('student_data_4_9.csv')
    row1 = result.iloc[0,:].to_list()
    row3 = result.iloc[2,:].to_list()
    assert hashlib.sha256(str(row1).encode('utf-8')).hexdigest() == '355e5a387d1b11520d62dc5613b178608b95de98342b89eb951ce205dea37481',  'First row values are incorrect'
    assert hashlib.sha256(str(row3).encode('utf-8')).hexdigest() == 'aa66d7848b4d3ef43a895adf1360e189e25a1dc549b7b19f6b3929a52e7a9824',  'Third row values are incorrect'
