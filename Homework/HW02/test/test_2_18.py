import os

def test_2_18():
    res = os.popen("python3 solution_2_18.py").read().strip()
    assert res =='Before ([1, 2, 4, 5], <class \'list\'>). After ([\'1\', \'2\', \'4\', \'5\'], <class \'list\'>).', "Integer to string transformation is incorrect."
