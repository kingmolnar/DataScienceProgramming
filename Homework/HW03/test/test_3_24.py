import os

def test_3_24():
    res = os.popen("python3 solution_3_24.py").read().strip()
    assert res == '[2 3 4 5 6] <class \'numpy.ndarray\'>', "subset or subset type not correct"
