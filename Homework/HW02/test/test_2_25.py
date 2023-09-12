from solution_2_25 import get_values_not_in_both_lists

def test_2_25():
    list1 = ["x", "7", "y", "9"]
    list2 = ["7", "6", "y", "f"]
    sol = get_values_not_in_both_lists(list1, list2)
    assert sol == {'6', '9', 'f', 'x'}, "Invalid result"
