import pandas as pd

def test_2_5():
    df = pd.read_csv('newsgroup.csv', engine='python', encoding='utf-8',
                 encoding_errors='ignore')
    assert df.shape[0]> 20_000, "Not enough records"
    assert df.shape[1] == 3, "Invalid number of columns"
    assert all(filter(lambda t:  t[0]==t[1], zip(df.columns, ['Topic', 'Post_ID', 'Sender']))), "Invalid table header"
