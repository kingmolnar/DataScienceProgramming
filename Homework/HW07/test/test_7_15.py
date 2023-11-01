import pandas as pd
import hashlib

def test_7_15():
    result = pd.read_csv('flights_7_15.csv')
    row1 = result.iloc[0,:].to_list()
    row3 = result.iloc[2,:].to_list()
    assert hashlib.sha256(str(row1).encode('utf-8')).hexdigest() == '84953c8be5e4cfcf9e723eb6a35e0c775ca3cad857f54cb7ff9722e333b38b10',  'First row values are incorrect'
    assert hashlib.sha256(str(row3).encode('utf-8')).hexdigest() == '5fcebf5458d7c9a62449b550fedc627479b9f67831a7d00efa5c115c2a0b57dc',  'Third row values are incorrect'
