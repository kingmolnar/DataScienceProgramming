from solution_3_6 import tuple_manipulation

def test_3_6():
    assert tuple_manipulation((3, 2, 2, 1), (5, 6, 4, 4, 4)) == (1, 2, 3, 4, 5, 6), "Tuple concatination is not correct"
