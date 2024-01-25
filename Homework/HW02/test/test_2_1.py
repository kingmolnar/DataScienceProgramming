from solution_2_1 import circle_measures

def test_2_1():
    rcas = [(783, 4919, 1926075),
     (2973, 18679, 27767686),
     (215, 1350, 145220),
     (7447, 46790, 174225845),
     (9473, 59520, 281919390),
     (3165, 19886, 31470040),
     (2826, 17756, 25089626),
     (2549, 16015, 20412187),
     (9314, 58521, 272535035),
     (8520, 53532, 228049467),
     (7509, 47180, 177138956),
     (8699, 54657, 237732487),
     (6646, 41758, 138761998),
     (6300, 39584, 124689812),
     (4549, 28582, 65010236),
     (7760, 48757, 189179169),
     (2302, 14463, 16647940),
     (6375, 40055, 127676288),
     (2989, 18780, 28067368),
     (6619, 41588, 137636821),
     (3082, 19364, 29841121),
     (5779, 36310, 104919270),
     (8363, 52546, 219722264),
     (4860, 30536, 74203161),
     (4549, 28582, 65010236),
     (933, 5862, 2734721),
     (830, 5215, 2164243)]

    for tup in rcas:
        c, a = circle_measures(tup[0])
        assert int(c) == tup[1] and int(a) == tup[2], f"Calculation error: {tup=}, {c=}, {a=}."
        test_less_zero = False
        try:
            _ = circle_measures(-9)
        except AssertionError as err:
            test_less_zero = True
        assert test_less_zero, "Failed to test for negative values"
        test_not_numeric = False
        try:
            _ = circle_measures("9.3")
        except AssertionError as err:
            test_not_numeric = True
        assert test_not_numeric, "Failed to test for negative values"
