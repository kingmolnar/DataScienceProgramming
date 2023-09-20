from solution_4_3 import total_amount

def test_4_2():
    assert int(total_amount(1000, 0.05, 5)) == 1276, "Output is incorrect for testcase 1"
    assert int(total_amount(2000, 0.075, 5)) == 2871, "Output is incorrect for testcase 2"
    assert int(total_amount(750, 0.1, 7)) == 1461, "Output is incorrect for testcase 3"
