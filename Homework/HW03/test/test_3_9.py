from solution_3_9 import list_of_tuples

def test_3_9():
    # Example data:
    names = ['Alice', 'Bob', 'Charlie', 'David']
    ages = [25, 30, 35, 28]
    assert list_of_tuples(names, ages) ==  [('Charlie', 35), ('Bob', 30), ('David', 28), ('Alice', 25)], "List of tuple is not correct"
