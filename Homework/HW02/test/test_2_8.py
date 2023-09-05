import solution_2_8

def test_2_8():
    try:
        numbers = solution_2_8.numbers
    except:
        raise Exception("Missing varaible `numbers`")
    assert isinstance(numbers, list), "Not a list"
    try:
        avg = solution_2_8.avg
    except:
        raise Exception("Missing varaible `avg`")
    assert isinstance(avg, float), "Not a float"
