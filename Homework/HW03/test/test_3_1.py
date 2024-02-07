from solution_3_1 import get_books_by_author

books = [
    {"name": "The Lord of the Rings", "author": "J.R.R. Tolkien"},
    {"name": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams"},
    {"name": "Pride and Prejudice", "author": "Jane Austen"},
    {"name": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
]

def test_3_1():
    assert get_books_by_author(books, 'Jane Austen') == ['Pride and Prejudice'], "Mismatch in first test case"
    assert get_books_by_author(books, 'J.R.R. Tolkien') == ['The Lord of the Rings'], "Mismatch in second test case"
    
