import pandas as pd
import hashlib

def test_7_5():
    result = pd.read_csv('student_data_7_5.csv')
    row1 = result.iloc[0,:].to_list()
    row3 = result.iloc[2,:].to_list()
    row5 = result.iloc[4,:].to_list()
    assert hashlib.sha256(str(row1).encode('utf-8')).hexdigest() == 'd91aeaf9017f1565e43db6c6aa4479e71f262906ae0bec6750d490d9d8c3abcd',  'First row values are incorrect'
    assert hashlib.sha256(str(row3).encode('utf-8')).hexdigest() == '9ce18f3071831b4208a2001668fb99141308d5d3416394d1cb7360d3b6e1e8e0',  'Third row values are incorrect'
    assert hashlib.sha256(str(row5).encode('utf-8')).hexdigest() == 'dc4d7f1003c0aa8e4225dff0707190a8ee5123217f980efdb178392b4440cda0',  'Last row values are incorrect'
