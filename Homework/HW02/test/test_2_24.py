from solution_2_24 import sort_by_word_length

def test_2_24():
    words = ["sawerblue", "smallfish", "she", "stocks"]
    sol = ['she', 'stocks', 'sawerblue', 'smallfish']
    assert sort_by_word_length(words) == sol, "Invalid result"
