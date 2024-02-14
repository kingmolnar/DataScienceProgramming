from solution_4_6 import *
import pandas as pd
import hashlib

def test_4_6():
    result = pd.read_csv('/data/IFI8410/homework7/student_data.csv')
    df1 = grouping(result, 5, 'age')
    assert hashlib.sha256(str(df1.shape).encode('utf-8')).hexdigest() == 'b1a1e628e1435d001ca3c3a29b1f39e9d7b2f35550a48eaea9def857dfc0c8ed', 'Shape of the first test case is in correct'
    df2 = grouping(result, 7, 'Medu')
    assert hashlib.sha256(str(df2.shape).encode('utf-8')).hexdigest() == 'a4b1877e00a1564fd98d0848a0499b35630252aaee654c2f182630ae1955d38d', 'Shape of the second test case is in correct'
    assert df2.famsize.mean() == 2.0, 'Some values in second test case are incorrect'
