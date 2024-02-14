import pandas as pd
import hashlib

def test_4_8():
    result = pd.read_csv('student_data_4_8.csv')
    row1 = result.iloc[0,:].to_list()
    row3 = result.iloc[2,:].to_list()
    assert hashlib.sha256(str(row1).encode('utf-8')).hexdigest() == 'e9749803f0fc97cd45dc29b5169ca8dc49c86fa5750dd2f8f86bcc8673b43ab9',  'First row values are incorrect'
    assert hashlib.sha256(str(row3).encode('utf-8')).hexdigest() == '0df95723ea88e9b0accae48c274ef0ee8de6821031149239bd75e99a5eae6b0d',  'Third row values are incorrect'
