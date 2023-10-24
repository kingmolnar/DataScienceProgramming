from solution_6_19 import *
import pandas as pd
import hashlib

def test_6_19():
    result = melt_data()
    assert isinstance(result, pd.DataFrame), "Invalid type"  
    assert result.shape == (3, 2), "Invalid shape"  
    assert hashlib.sha256(str(result).encode('utf-8')).hexdigest() == 'cb66480134ac70d36d1a715badab6913e2f280e7124a0ef29d9c7717dad3f7a5', "Invalid result" 
