from solution_6_1 import *
import hashlib

def test_6_1():
    result = find_missingvalues()
    assert isinstance(result, list), "Invalid type"  
    assert hashlib.sha256(str(result).encode('utf-8')).hexdigest() == '48dea75185ad4b1b50ceed67ce64103623548c1c44d93897952506af9b462c67', "Invalid result" 
