from solution_6_18 import *
import pandas as pd
import hashlib

def test_6_18():
    result = create_ChargeRatio()
    assert isinstance(result, pd.DataFrame), "Invalid type"  
    assert result.shape == (7042, 22), "Invalid shape"  
    assert hashlib.sha256(str(result.to_csv()).encode('utf-8')).hexdigest() == '87bdf5d6a1412cf721609bc367d494e58c60d97794976185375113b52bba8c27', "Invalid result" 
  
