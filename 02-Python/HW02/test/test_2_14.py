from solution_2_14 import circle_area

def test_2_14():
    for r, a in [(3, 28), (6, 113), (9, 254), (12, 452), (15, 706), (18, 1017)]:
        a2 = int(circle_area(r))
        assert a2==a, "Invalid value"
