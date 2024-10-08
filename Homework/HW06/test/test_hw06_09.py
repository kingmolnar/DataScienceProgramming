
from solution_6_9 import filter_books_by_title
import unittest
import pandas as pd

class TestHW0609(unittest.TestCase):
    def test_filter_books_by_title(self):
        # Test case 1
        data = {
            'Title': ['The Great Gatsby', 'Moby Dick', 'To Kill a Mockingbird', 'The Catcher in the Rye', 'Gone with the Wind'],
            'Author': ['F. Scott Fitzgerald', 'Herman Melville', 'Harper Lee', 'J.D. Salinger', 'Margaret Mitchell']
        }
        df14 = pd.DataFrame(data)

        # Applying the function to filter books starting with 't' and containing 'the'
        result = filter_books_by_title(df14, 't', 'the')

        expected_data = {
            'Title': ['the great gatsby', 'the catcher in the rye'],
            'Author': ['F. Scott Fitzgerald', 'J.D. Salinger']
        }
        expected_df = pd.DataFrame(expected_data)

        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_df)

        # Test case 2: Filter books starting with 'm' and containing 'dick'
        result = filter_books_by_title(df14, 'm', 'dick')
        expected_data = {
            'Title': ['moby dick'],
            'Author': ['Herman Melville']
        }
        expected_df = pd.DataFrame(expected_data)

        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_df)
