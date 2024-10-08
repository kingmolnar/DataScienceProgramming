
from solution_6_6 import clean_up_string
import unittest

class TestHW0606(unittest.TestCase):
    def test_clean_up_string(self):
        # Test case 1
        messy_string = "Python---for programming- in  - data---science example!!"
        result = clean_up_string(messy_string)
        expected_result = "Python for programming in data science example!!"
        self.assertEqual(result, expected_result)

        # Test case 2
        messy_string = "   Code---in Python--is great!    "
        result = clean_up_string(messy_string)
        expected_result = "Code in Python is great!"
        self.assertEqual(result, expected_result)

        # Test case 3
        messy_string = "   Learn---Data Science---now    "
        result = clean_up_string(messy_string)
        expected_result = "Learn Data Science now"
        self.assertEqual(result, expected_result)
