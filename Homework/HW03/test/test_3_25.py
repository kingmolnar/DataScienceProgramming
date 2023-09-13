import os

def test_3_25():
    res = os.popen("python3 solution_3_25.py ").readlines()
    test = [
        "random_array1.shape = (5, 5), np.min(random_array1) >= 0 = True, np.max(random_array1) <= 1 = True",
        "random_array2.shape = (5, 5), np.min(random_array2) >= 1 = True, np.max(random_array2) <= 10 = True"
    ]
    for j in range(len(test)):
        assert res[j].strip().startswith(test[j]), f"Mismatch in line {j+1} {test[j]} should be {res[j]}"
