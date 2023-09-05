from solution_2_9 import even_or_odd

def test_2_9():
    for n, r in [(17, "odd"), (32, "even")]:
        assert even_or_odd(n) == r, f"Invalid result for {n}"
