import os

def test_3_23():
    res = os.popen("python3 solution_3_23.py ").readlines()
    test = [
        "addition = [12 24 36 48 60], <class 'numpy.ndarray'>","substraction = [ 8 16 24 32 40], <class 'numpy.ndarray'>",
        "multiplication = [ 20  80 180 320 500], <class 'numpy.ndarray'>", "division = [5. 5. 5. 5. 5.], <class 'numpy.ndarray'>"
    ]
    for j in range(len(test)):
        assert res[j].strip().startswith(test[j]), f"Mismatch in line {j+1} {test[j]} should be {res[j]}"
