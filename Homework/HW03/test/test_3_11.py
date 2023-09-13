from solution_3_11 import apply_operation




def test_3_11():
    def power(x):
        return x ** 2
    assert apply_operation(power, {1,2,3}) == {1: 1, 2: 4, 3: 9}, "apply_operation is not correct"
