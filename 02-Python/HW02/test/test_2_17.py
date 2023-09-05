import os

def test_2_17():
    res = os.popen("python3 solution_2_17.py").read().strip()
    assert res == '2023', "Integer extraction is incorrect."
