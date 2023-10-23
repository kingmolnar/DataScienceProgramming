from solution_6_25 import *
import pandas as pd
import hashlib

def test_6_25():
    result = count_quarterlyCustomer()
    assert isinstance(result, pd.Series), "Invalid type"
    assert len(result) == 5, "Invalid length"
    assert hashlib.sha256(str(result).encode('utf-8')).hexdigest() == '7f81bfca8de1b6a3aff01e90f96110c5405f829a3a1568dbf4dd53d342e69fe1', "Invalid result"
