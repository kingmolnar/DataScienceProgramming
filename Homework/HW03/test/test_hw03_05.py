
from solution_3_5 import create_dict_from_sequences
import unittest

class TestHW0305(unittest.TestCase):
    def setUp(self):
        self.keys = ("name", "age", "job")
        self.values = ["Alice", 30, "Doctor"]

    def test_hw03_05(self):
        expected_result = {"name": "Alice", "age": 30, "job": "Doctor"}
        result = create_dict_from_sequences(self.keys, self.values)
        self.assertEqual(result, expected_result)

    def test_empty_sequences(self):
        keys = ()
        values = []
        expected_result = {}
        result = create_dict_from_sequences(keys, values)
        self.assertEqual(result, expected_result)

    def test_single_element(self):
        keys = ("key",)
        values = ["value"]
        expected_result = {"key": "value"}
        result = create_dict_from_sequences(keys, values)
        self.assertEqual(result, expected_result)

    def test_mismatched_lengths(self):
        keys = ("name", "age")
        values = ["Alice", 30, "Doctor"]
        expected_result = {"name": "Alice", "age": 30}
        result = create_dict_from_sequences(keys, values)
        self.assertEqual(result, expected_result)


