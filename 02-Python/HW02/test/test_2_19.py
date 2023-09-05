import os

def test_2_19():
    res = os.popen("python3 solution_2_19.py").read().strip()
    assert res == '["red", "red", "green", "blue"] True, ["red", "green", "blue", "yellow"] False', "Color checking is incorrect."
