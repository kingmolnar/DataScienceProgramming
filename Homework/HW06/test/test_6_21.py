from solution_6_21 import *
import pandas as pd
import hashlib

def test_6_21():
    result = payment_percentage()        
    assert isinstance(result, pd.DataFrame), "Invalid type"
    assert result.shape == (4, 2), "Invalid shape"
    assert hashlib.sha256(str(result).encode('utf-8')).hexdigest() == '70f3e6d9f753942ac48218355d2fc8b38d44da77484025814196d2aef08b5c66', "Result is incorrect"
