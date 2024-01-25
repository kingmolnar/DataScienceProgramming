from solution_2_2 import multiplication_table_csv
from tempfile import NamedTemporaryFile
import os
import pandas as pd

def test_2_2():
    f = NamedTemporaryFile(delete=False)
    fn = f.name
    f.close()
    n = 17
    multiplication_table_csv(fn, n)
    assert os.path.exists(fn), "Failed to create file"
    df = pd.read_csv(fn)
    assert df.shape[0] == n*n, f"Incorrect number of rows: {df.shape[0]} should be {n*n}"
    assert df.shape[1] == 3, f"Incorrect number of colums: {df.shape[1]} should be 3"
    os.unlink(f.name)
    assert not os.path.exists(fn), f"File `{fn}` should have been deleted"
