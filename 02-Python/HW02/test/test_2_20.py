from solution_2_20 import colors_to_integers

def test_2_20():
    words = ['red', 'blue', 'green', 'red', 'red', 'green', 'blue', 'green']
    cols = colors_to_integers(words)
    nums = [1, 2, 3, 1, 1, 3, 2, 3]
    assert all([c==n for c, n in zip(cols, nums)]), "Invalid result"
