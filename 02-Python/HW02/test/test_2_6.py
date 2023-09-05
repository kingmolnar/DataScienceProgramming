import os
import solution_2_6

def test_2_6():
    res = os.popen("python3 solution_2_6.py").read().strip()
    assert res == 'John is 35. His favorite color is yellow.'
    assert isinstance(solution_2_6.name, str), "Variable `name` not correctly defined."
    assert isinstance(solution_2_6.age, int), "Variable `age` not correctly defined."
    assert isinstance(solution_2_6.favorite_color, str), "Variable `favorite_color` not correctly defined."
