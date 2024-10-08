
from solution_6_8 import regex_match_and_search
import unittest

class TestHW0608(unittest.TestCase):
    def test_regex_match_and_search(self):
        # Test case 1
        example_string = "Hello, welcome to the world of Python."
        pattern = r"world"
        match_result, search_result = regex_match_and_search(example_string, pattern)
        self.assertIsNone(match_result)  # .match() should return None
        self.assertIsNotNone(search_result)  # .search() should return a match object
        self.assertEqual(search_result.span(), (22, 27))  # Corrected span to (22, 27)

        # Test case 2
        example_string = "world of Python is vast."
        pattern = r"world"
        match_result, search_result = regex_match_and_search(example_string, pattern)
        self.assertIsNotNone(match_result)  # .match() should return a match object
        self.assertEqual(match_result.span(), (0, 5))  # span should be (0, 5)
        self.assertEqual(search_result.span(), (0, 5))  # .search() should also match the first occurrence

        # Test case 3
        example_string = "Python programming is fun."
        pattern = r"Python"
        match_result, search_result = regex_match_and_search(example_string, pattern)
        self.assertIsNotNone(match_result)  # .match() should return a match object
        self.assertIsNotNone(search_result)  # .search() should also return a match object
        self.assertEqual(match_result.span(), (0, 6))  # match should be at the beginning
        self.assertEqual(search_result.span(), (0, 6))  # search should find the same match
