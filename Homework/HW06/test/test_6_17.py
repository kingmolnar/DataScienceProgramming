from solution_6_17 import *
import pandas as pd
import hashlib

def test_6_17():
    result = calculate_monthlycharges()
    assert isinstance(result, pd.Series), "Invalid type"  
    assert len(result) == (3), "Invalid type"  
    assert hashlib.sha256(str(result).encode('utf-8')).hexdigest() == '99f2df7186dc0a945bc38269e1b462ed227ab36efbf187d28fa430ba0e5c6a1c', "Invalid result" 
