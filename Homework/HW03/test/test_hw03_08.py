
from solution_3_8 import map_strings_to_indices
import unittest

class TestHW0308(unittest.TestCase):
    def setUp(self):
        self.strings = ["apple", "banana", "orange"]

    # Test 1: Standard case
    def test_map_strings_to_indices(self):
        result = map_strings_to_indices(self.strings)
        expected_result = {"apple": 0, "banana": 1, "orange": 2}
        self.assertEqual(result, expected_result)

    # Test 2: Empty list
    def test_empty_list(self):
        result = map_strings_to_indices([])
        expected_result = {}
        self.assertEqual(result, expected_result)

    # Test 3: List with one element
    def test_single_element(self):
        result = map_strings_to_indices(["apple"])
        expected_result = {"apple": 0}
        self.assertEqual(result, expected_result)

    # Test 4: List with duplicate elements
    def test_duplicates(self):
        result = map_strings_to_indices(["apple", "banana", "apple"])
        expected_result = {"apple": 2, "banana": 1}  # The second "apple" should overwrite the first
        self.assertEqual(result, expected_result)

    # Test 5: List with mixed case strings
    def test_mixed_case(self):
        result = map_strings_to_indices(["Apple", "banana", "Orange"])
        expected_result = {"Apple": 0, "banana": 1, "Orange": 2}
        self.assertEqual(result, expected_result)


