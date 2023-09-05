from solution_2_21 import create_marks_dict
from solution_2_22 import get_students_with_above_average_marks

def test_2_22():
    names = ["John", "Jane", "Doe", "Bill"]
    marks = [100, 90, 80, 85]
    students = create_marks_dict(names, marks)
    top_students = get_students_with_above_average_marks(students)
    assert top_students == {'John': 100, 'Jane': 90}, "Invalid results"
