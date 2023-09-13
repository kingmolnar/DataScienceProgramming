from solution_3_8 import merge_dicts


def test_3_8():
    # Example data:
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    dict3 = {'c': 5, 'd': 6}
    assert merge_dicts([dict1, dict2, dict3]) == {'a': 1, 'b': 3, 'c': 5, 'd': 6}, "Dict merge is not correct"
