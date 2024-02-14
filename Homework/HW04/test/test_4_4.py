import pandas as pd
import hashlib

def test_4_4():
    result = pd.read_csv('student_data_4_4.csv')
    val1 = round(result[(result.school == 'GP') & (result.sex=='F')]['age'].values[0],2)
    val2 = round(result[(result.school == 'MS') & (result.sex=='M')]['age'].values[0],2) 
    assert hashlib.sha256(str(val1).encode('utf-8')).hexdigest() == 'ee66b6ed063a824e27aafdaac3daccb8b2ec7cc7581c202a2680e412fa3657b7',  'The mean age for Female students in GP school is incorrect'
    assert hashlib.sha256(str(val2).encode('utf-8')).hexdigest() == '2fe0249fda7a6473f86f4533d2dfcc3adfe122ad6aaf742bb89b6847a368f7c4',  'The mean age for Male students in MS school is incorrect'
