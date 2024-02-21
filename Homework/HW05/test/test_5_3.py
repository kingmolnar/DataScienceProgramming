import pandas as pd
import hashlib

def test_5_3():
    result = pd.read_csv('titanic_5_3.csv')
    row1 = result.iloc[0,:].to_list()
    row3 = result.iloc[2,:].to_list()
    assert hashlib.sha256(str(row1).encode('utf-8')).hexdigest() == '324488b59b6210bc28e107146c104d76137495196506b064241fab58a1c8b522',  'First row values are incorrect'
    assert hashlib.sha256(str(row3).encode('utf-8')).hexdigest() == '604561951a90441b25b92ec5a325e1dda94ee5327e6ebcf74e1b621358996b5a',  'Third row values are incorrect'
