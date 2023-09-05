from solution_2_21 import create_marks_dict

def test_2_21():
    names = ["John", "Jane", "Doe", "Bill"]
    marks = [100, 90, 80, 85]
    res = create_marks_dict(names, marks)
    assert res == {'John': 100, 'Jane': 90, 'Doe': 80, 'Bill': 85}, "Invalid results"
