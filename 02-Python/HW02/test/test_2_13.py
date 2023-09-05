from solution_2_13 import is_prime

def test_2_13():
    for n, p in [(3, True), (7, True), (12, False), (19, True), (25, False), (43, True), (54, False),
                 (59, True), (63, False), (67, True), (71, True), (89, True), (99, False)]:
        assert is_prime(n)==p, f"Invalid result for {n}"
