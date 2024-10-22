
import unittest
from solution_7_19 import match_sequence_at_start

class TestMatchSequenceAtStart(unittest.TestCase):

    def test_match_sequence_at_start(self):
        # Test case 1: Matches start with "AB" followed by two digits
        strings = ["AB12", "XY34", "AB56", "A123", "AB78", "XY90"]
        start_sequence = "AB"
        result = match_sequence_at_start(strings, start_sequence)
        expected = ['AB12', 'AB56', 'AB78']
        self.assertEqual(result, expected)

        # Test case 2: Matches start with "XY" followed by two digits
        strings = ["XY12", "XY34", "XY56", "AB78", "XY90"]
        start_sequence = "XY"
        result = match_sequence_at_start(strings, start_sequence)
        expected = ['XY12', 'XY34', 'XY56', 'XY90']
        self.assertEqual(result, expected)

        # Test case 3: No match for strings without two digits after the sequence
        strings = ["AB12", "AB1234", "XYZ78", "XY45"]
        start_sequence = "AB"
        result = match_sequence_at_start(strings, start_sequence)
        expected = ['AB12']
        self.assertEqual(result, expected)

        # Test case 4: Case insensitive check
        strings = ["ab12", "AB34", "Ab56", "A123", "AB78", "XY90"]
        start_sequence = "AB"
        result = match_sequence_at_start(strings, start_sequence)
        expected = ['AB34', 'AB78']
        self.assertEqual(result, expected)
