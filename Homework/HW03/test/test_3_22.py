import os

def test_3_22():
    res = os.popen("python3 solution_3_22.py ").readlines()
    test = [
      "Type: type(matrix)","Shape: (3, 3)","Dimensions: 2", "Size: 9"
    ]
    for j in range(len(test)):
        assert res[j].strip().startswith(test[j]), f"Mismatch in line {j+1} {test[j]} should be {res[j]}"
