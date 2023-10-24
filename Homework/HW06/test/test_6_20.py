from solution_6_20 import *
import pandas as pd
import hashlib

def test_6_20():
    result = calculate_charges()
    assert isinstance(result, pd.DataFrame), "Invalid type"  
    assert result.shape == (6, 2), "Invalid shape"  
    assert hashlib.sha256(str(result).encode('utf-8')).hexdigest() == 'db41e31c79ef4cd6681d0891038f94715d2ed191bc7238888d0b843fdd25d90b', "Invalid result" 
