from solution_4_1 import most_popular_language

new_friends = [
    {'name': 'Alice', 'language': 'Python'},
    {'name': 'Bob', 'language': 'JavaScript'},
    {'name': 'Charlie', 'language': 'Python'},
    {'name': 'David', 'language': 'Java'},
    {'name': 'Eva', 'language': 'Python'},
    {'name': 'Frank', 'language': 'Java'},
    {'name': 'Grace', 'language': 'JavaScript'},
    {'name': 'Helen', 'language': 'C++'},
    {'name': 'Ivy', 'language': 'Python'},
    {'name': 'Jack', 'language': 'JavaScript'}
]

def test_4_1():
    assert most_popular_language(new_friends) == ('Python', 4), "Output is incorrect"
