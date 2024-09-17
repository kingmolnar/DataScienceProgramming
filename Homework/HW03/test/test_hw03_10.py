
from solution_3_10 import apply_operations, remove_numeric
import unittest

class TestHW0310(unittest.TestCase):

    def setUp(self):
        self.ops = [str.lower, remove_numeric, str.capitalize]

    # Test 1: Standard case with a mix of numbers and letters
    def test_apply_operations(self):
        sample_strings = ["Hello123", "World!456"]
        result = apply_operations(sample_strings, self.ops)
        expected_result = ["Hello", "World!"]
        self.assertEqual(result, expected_result)

    # Test 2: Empty list of strings
    def test_empty_strings_list(self):
        sample_strings = []
        result = apply_operations(sample_strings, self.ops)
        expected_result = []
        self.assertEqual(result, expected_result)

    # Test 3: List with a string that has no numbers
    def test_no_numeric_string(self):
        sample_strings = ["Hello", "World"]
        result = apply_operations(sample_strings, self.ops)
        expected_result = ["Hello", "World"]
        self.assertEqual(result, expected_result)

    # Test 4: String with only numeric characters
    def test_numeric_only_string(self):
        sample_strings = ["123", "456"]
        result = apply_operations(sample_strings, self.ops)
        expected_result = ["", ""]
        self.assertEqual(result, expected_result)

    # Test 5: List with mixed-case strings
    def test_mixed_case_strings(self):
        sample_strings = ["hElLo123", "WoRlD!456"]
        result = apply_operations(sample_strings, self.ops)
        expected_result = ["Hello", "World!"]
        self.assertEqual(result, expected_result)
