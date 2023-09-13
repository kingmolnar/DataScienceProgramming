import os

def test_3_21():
    res = os.popen("python3 solution_3_21.py").read().strip()
    assert res == '<class \'numpy.ndarray\'>', "Not a numpy array"
