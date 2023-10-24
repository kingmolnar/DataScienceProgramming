from solution_6_23 import *
import pandas as pd
import hashlib

def test_6_23():
    result = get_monthlysales()
    assert len(result) == 5, "Invalid length"
    assert isinstance(result, pd.Series), "Invalid Type"
    assert hashlib.sha256(str(result).encode('utf-8')).hexdigest() == '2770f52acf503e50b1fa2732019e74bd606f0097b204fb5cafbe3fbb6606b5b9', "Incorrect result"
