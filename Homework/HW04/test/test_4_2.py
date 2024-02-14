import pandas as pd
import hashlib

def test_4_2():
    result = pd.read_csv('student_data_4_2.csv')
    row3 = result.iloc[2,:].to_list()
    row5 = result.iloc[4,:].to_list()
    assert hashlib.sha256(str(row3).encode('utf-8')).hexdigest() == '763ee1b87c415fd5c0f8d25d346c115205941ae9b5557b0589d7e2ba14c20bc5',  'Third row values are incorrect'
    assert hashlib.sha256(str(row5).encode('utf-8')).hexdigest() == '1acac33fac8ada701b255efd2967979bcab1a240e5adc9c15bba883a7e7ad12c',  'Last row values are incorrect'
