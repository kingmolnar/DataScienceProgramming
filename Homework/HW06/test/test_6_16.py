from solution_6_16 import *
import pandas as pd
import hashlib

def test_6_16():
    result = calculate_avgcharges()
    assert isinstance(result, pd.DataFrame), "Invalid type"  
    assert result.shape == (2, 3), "Invalid shape"  
    assert hashlib.sha256(str(result).encode('utf-8')).hexdigest() == '5d77766463d68b25d95546d5977796935ec468342b661305d4e67203cbe92472', "Invalid result" 
