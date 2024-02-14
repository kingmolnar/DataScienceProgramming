import pandas as pd
import hashlib

def test_4_10():
    result = pd.read_csv('student_data_4_10.csv')
    row1 = result.iloc[0,1]
    row3 = result.iloc[2,1]
    assert hashlib.sha256(row1.encode('utf-8')).hexdigest() == '78eaa1fc9aeccfde92d2dc34b69f6aa715df7812cd189c5aba47f7b00a056b3c',  'First row values are incorrect'
    assert hashlib.sha256(row3.encode('utf-8')).hexdigest() == '8e563c7e0b8200bec3e751ccbce81a0c3e9c99c12daa36fc6adffb0ec1a4f5d1',  'Third row values are incorrect'
