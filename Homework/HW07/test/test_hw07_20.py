
import unittest
from solution_7_20 import match_sequence_at_end

class TestMatchSequenceAtEnd(unittest.TestCase):

    def test_match_sequence_at_end(self):
        # Test case 1: Matches end with "AB" preceded by two digits
        strings = ["12AB", "34XY", "56AB", "123A", "78AB", "90XY"]
        end_sequence = "AB"
        result = match_sequence_at_end(strings, end_sequence)
        expected = ['12AB', '56AB', '78AB']
        self.assertEqual(result, expected)

        # Test case 2: Matches end with "XY" preceded by two digits
        strings = ["12XY", "34XY", "56XY", "12AB", "78XY", "90XY"]
        end_sequence = "XY"
        result = match_sequence_at_end(strings, end_sequence)
        expected = ['12XY', '34XY', '56XY', '78XY', '90XY']
        self.assertEqual(result, expected)

        # Test case 3: No match for strings without two digits before the sequence
        strings = ["AB12", "12XY34", "XY56AB", "AB78"]
        end_sequence = "AB"
        result = match_sequence_at_end(strings, end_sequence)
        expected = ['XY56AB']
        self.assertEqual(result, expected)

        # Test case 4: No valid matches
        strings = ["randomString", "anotherTest"]
        end_sequence = "AB"
        result = match_sequence_at_end(strings, end_sequence)
        expected = []
        self.assertEqual(result, expected)
