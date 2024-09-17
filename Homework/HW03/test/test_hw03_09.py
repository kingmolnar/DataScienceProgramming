
from solution_3_9 import person_details
import unittest

class TestHW0309(unittest.TestCase):

    # Test 1: Standard case with typical name and age
    def test_person_details(self):
        result = person_details("Alice", 30)
        expected_result = ("Alice", 30, 900)  # Age squared is 900
        self.assertEqual(result, expected_result)

    # Test 2: Check if the function works with a negative age
    def test_negative_age(self):
        result = person_details("Bob", -5)
        expected_result = ("Bob", -5, 25)  # (-5)^2 = 25
        self.assertEqual(result, expected_result)

    # Test 3: Check if the function works with age 0
    def test_age_zero(self):
        result = person_details("Charlie", 0)
        expected_result = ("Charlie", 0, 0)  # 0^2 = 0
        self.assertEqual(result, expected_result)

    # Test 4: Check for large age value
    def test_large_age(self):
        result = person_details("David", 1000)
        expected_result = ("David", 1000, 1000000)  # 1000^2 = 1,000,000
        self.assertEqual(result, expected_result)

    # Test 5: Check with an empty name
    def test_empty_name(self):
        result = person_details("", 25)
        expected_result = ("", 25, 625)  # 25^2 = 625
        self.assertEqual(result, expected_result)
