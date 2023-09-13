from solution_3_7 import filter_and_square

def test_3_7():
    assert filter_and_square([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}, "filter and square is not correct"
