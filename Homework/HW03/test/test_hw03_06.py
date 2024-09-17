
from solution_3_6 import remove_key
import unittest

class TestHW0306(unittest.TestCase):
    def setUp(self):
        self.person = {"name": "John", "age": 28, "job": "Engineer"}

    def test_remove_existing_key(self):
        result = remove_key(self.person.copy(), "age")
        expected_result = {"name": "John", "job": "Engineer"}
        self.assertEqual(result, expected_result)

    def test_remove_non_existing_key(self):
        result = remove_key(self.person.copy(), "height")
        expected_result = {"name": "John", "age": 28, "job": "Engineer"}
        self.assertEqual(result, expected_result)

    def test_remove_last_key(self):
        person = {"age": 28}
        result = remove_key(person.copy(), "age")
        expected_result = {}
        self.assertEqual(result, expected_result)

    def test_empty_dictionary(self):
        result = remove_key({}, "age")
        expected_result = {}
        self.assertEqual(result, expected_result)

