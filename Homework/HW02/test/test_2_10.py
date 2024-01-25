from solution_2_10 import fibonacci

def test_2_10():
    def _in_order(fib):
        return all([fib[j-1]<=fib[j] for j in range(1, len(fib))])

    fib10 = fibonacci(10)
    assert _in_order(fib10), 'Invalid order of Fibonacci sequence of length 10'
    assert sum(fib10) == 88, 'Invalid sequence. The sum should be 88'
    fib55 = fibonacci(55)
    assert _in_order(fib55), 'Invalid order of Fibonacci sequence of length 55'
    assert sum(fib55) == 225851433716, 'Invalid sequence. The sum should be 225851433716'
    fib79 = fibonacci(79)
    assert _in_order(fib79), 'Invalid order of Fibonacci sequence of length 79'
    assert sum(fib79) == 23416728348467684, 'Invalid sequence. The sum should be 23416728348467684'
