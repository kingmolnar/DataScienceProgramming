from solution_6_22 import *
import pandas as pd
import hashlib

def test_6_22():
    result = percentage_churn()
    
    assert isinstance(result, pd.DataFrame), "Invalid type"
    assert result.shape == (4, 3), "Invalid shape"
    assert hashlib.sha256(str(result).encode('utf-8')).hexdigest() == '5ca432ed77b2a744b29326bdc8e6f1f8789718f2347a9e1bf68b9c5a838accfc', "Result is incorrect"
