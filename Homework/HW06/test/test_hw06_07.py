
from solution_6_7 import count_substring_occurrences
import unittest

class TestHW0607(unittest.TestCase):
    def test_count_substring_occurrences(self):
        # Test case 1
        messy_string = "  This is a simple string---with many SIMPLE and Simple occurrences!  "
        target_substring = "simple"
        result = count_substring_occurrences(messy_string, target_substring)
        expected_result = 3
        self.assertEqual(result, expected_result)

        # Test case 2
        messy_string = "   Python--is the best programming language!  Python--and python!!  "
        target_substring = "python"
        result = count_substring_occurrences(messy_string, target_substring)
        expected_result = 3
        self.assertEqual(result, expected_result)

        # Test case 3
        messy_string = "   Lots --- of   spaces--here    "
        target_substring = "spaces"
        result = count_substring_occurrences(messy_string, target_substring)
        expected_result = 1
        self.assertEqual(result, expected_result)
