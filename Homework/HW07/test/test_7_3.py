import pandas as pd
import hashlib 

def test_7_3():
    result = pd.read_csv('student_data_7_3.csv')
    assert hashlib.sha256(str(result.iloc[1,3]).encode('utf-8')).hexdigest() == '785f3ec7eb32f30b90cd0fcf3657d388b5ff4297f2f9716ff66e9b69c05ddd09',  'The max value for male in incorrect'
    assert hashlib.sha256(str(result.iloc[0,2]).encode('utf-8')).hexdigest() == 'e629fa6598d732768f7c726b4b621285f9c3b85303900aa912017db7617d8bdb',  'The min value for female in incorrect'
