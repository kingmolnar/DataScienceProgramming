from solution_5_7 import load_and_analyze_movie_data

def test_5_7():
    result = load_and_analyze_movie_data()
    assert result == (10, 4), "The shape of the dataset is incorrect"
