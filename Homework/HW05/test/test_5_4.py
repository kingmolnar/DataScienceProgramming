import pandas as pd
import hashlib

def test_5_4():
    result = pd.read_csv('titanic_5_4.csv')
    row1 = result.iloc[0,:].to_list()
    row2 = result.iloc[1,:].to_list()
    assert hashlib.sha256(str(row1).encode('utf-8')).hexdigest() == 'e2443f80ad59a1a927d44f4086ce41859150c22d3d98452d3285cca1a33464f0',  'First row values are incorrect'
    assert hashlib.sha256(str(row2).encode('utf-8')).hexdigest() == '2a31d7bfe69198bf64d06cd21068110e1ba2f327ca7aed54d7193f1e26431055',  'Second row values are incorrect'
