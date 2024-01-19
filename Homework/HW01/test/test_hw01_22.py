
import os
import re
import pandas as pd

def test_problem_1_22():
    fn = 'data/word_frequency_positive_negative.csv'
    assert os.path.isfile(fn), f"File does not exist: {fn}"
    df = pd.read_csv(fn)
    assert df.shape[1]==3, "Invalid number of columns"
    for col in ['Word','Positive_Freq','Negative_Freq']:
        assert col in df.columns, f"Misssing column: {col}, {df.columns}"
