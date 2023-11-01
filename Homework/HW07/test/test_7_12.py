import pandas as pd
import hashlib

def test_7_12():
    result = pd.read_csv('penguins_7_12.csv')
    row1 = result.iloc[0,:].to_list()
    row3 = result.iloc[2,:].to_list()
    assert hashlib.sha256(str(row1).encode('utf-8')).hexdigest() == 'd541183a95f3a94ef35f35a68c0896298a370e065ce929ccaa577409b7c64bfd',  'First row values are incorrect'
    assert hashlib.sha256(str(row3).encode('utf-8')).hexdigest() == '446505b8377a1cb01bbc652fab54fa3ffd74c0545d3a5d1fc48175281be0cd93',  'Third row values are incorrect'
