
import os
import re
import pandas as pd

def test_problem_1_25():
    fn = 'data/positive_negative_table.csv'
    assert os.path.isfile(fn), f"File does not exist: {fn}"
    df = pd.read_csv(fn)
    assert df.shape[1]==3, "Invalid number of columns"
    for col in ['PositiveOnly','NegativeOnly','Both']:
        assert col in df.columns, f"Misssing column: {col}, {df.columns}"
    
