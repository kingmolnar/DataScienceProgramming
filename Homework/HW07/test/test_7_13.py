import pandas as pd
import hashlib

def test_7_13():
    result = pd.read_csv('penguins_7_13.csv')
    row1 = result.iloc[0,:].to_list()
    row3 = result.iloc[2,:].to_list()
    assert hashlib.sha256(str(row1).encode('utf-8')).hexdigest() == '6beee7ad7f24bd59e5bb93d3f111c7b71c25591e6eb242db95db11ae4b6a48b4',  'First row values are incorrect'
    assert hashlib.sha256(str(row3).encode('utf-8')).hexdigest() == '0586ffd672513034369fc9091e2240dc62db3bd0a87c5f013d36b316e5ceb3ff',  'Third row values are incorrect'
