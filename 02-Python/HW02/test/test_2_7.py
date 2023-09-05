import solution_2_7

def test_2_7():
    try:
        numbers = solution_2_7.numbers
    except:
        raise Exception("Missing varaible `numbers`")
    assert isinstance(numbers, list), "Not a list"
