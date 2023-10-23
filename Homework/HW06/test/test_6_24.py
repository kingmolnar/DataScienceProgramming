from solution_6_24 import *
import pandas as pd
import hashlib

def test_6_24():
    result = calculate_totalsales()
    assert isinstance(result, pd.Series), "Invalid type"
    assert len(result) == 12, "Invalid length"
    assert hashlib.sha256(str(result).encode('utf-8')).hexdigest() == '7bffafc5d705f9285982de737b6f3d407ae9e1411dc92a838be35300c9348ef8', "Invalid result"
    #     sales=pd.read_csv("/data/IFI8410/sales.csv")
    #     grouped_data = sales.groupby(['Region', 'Category'])['Sales'].sum()
    #     assert result.equals(grouped_data), "Incorrect result"
