
from solution_3_12 import fibonacci
import unittest

class TestHW0312(unittest.TestCase):
    def test_fibonacci(self):
        fib_gen = fibonacci(10)
        expected_sequence = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        for expected in expected_sequence:
            self.assertEqual(next(fib_gen), expected, f"Test failed at Fibonacci number {expected}")
