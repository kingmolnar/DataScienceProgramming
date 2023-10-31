from solution_6_19 import *
import pandas as pd
import hashlib

def test_6_19():
    result = melt_data()
    assert isinstance(result, pd.Series), "Invalid type"  
    #     assert result.shape[1] == 3, "Invalid shape"
    result_str = str(result.head(100).to_csv(index=None)).encode('utf-8')
    assert hashlib.sha256(result_str).hexdigest() \
                          == '332ffd7d4eac2e55cc97d7576616bd40581c46e0cdf52c67064691fae4735c17', \
                          "Invalid result" 
