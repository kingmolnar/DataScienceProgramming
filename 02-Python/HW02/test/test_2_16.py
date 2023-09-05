
import os

def test_2_16():
    res = os.popen("python3 solution_2_16.py").read().strip()
    assert res == '[\'Hello\', \'World\']', "String splitting is incorrect."
