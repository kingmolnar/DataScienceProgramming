import pandas as pd
import hashlib

def test_4_7():
    result = pd.read_csv('student_data_4_7.csv')
    assert hashlib.sha256(str(round(result.iloc[0,1], 2)).encode('utf-8')).hexdigest() == 'e932a6fc85160851a426eb49c291b69998c2f7c4d05dbce26c59af62941dd613', 'Weighted average value for female is incorrect'
    assert hashlib.sha256(str(round(result.iloc[1,1], 2)).encode('utf-8')).hexdigest() == 'c02a87b566e653db888d05dc45e0291c9a6b5d3697ef63c95035ad226586623d', 'Weighted average values for male is incorrect'
