
import unittest
from solution_7_16 import find_word_with_pattern

class TestFindWordWithPattern(unittest.TestCase):

    def test_find_word_with_pattern(self):
        # Test case 1: Word starts with 'r' and ends with 's'
        sentence = "Rabbits are running fast and reach their goals."
        start_letter = "r"
        end_letter = "s"
        result = find_word_with_pattern(sentence, start_letter, end_letter)
        self.assertEqual(result, "Rabbits")  # Expected word is 'Rabbits'

        # Test case 2: Multiple matches, but the longest should be returned
        sentence = "I love programming in Python."
        start_letter = "p"
        end_letter = "g"
        result = find_word_with_pattern(sentence, start_letter, end_letter)
        self.assertEqual(result, "programming")  # Expected word is 'programming'

        # Test case 3: No word starts with 'x' and ends with 'z'
        sentence = "There are no such words here."
        start_letter = "x"
        end_letter = "z"
        result = find_word_with_pattern(sentence, start_letter, end_letter)
        self.assertIsNone(result)  # Expected result is None (no match)

        # Test case 4: Case insensitivity check
        sentence = "Red roses bloom every spring."
        start_letter = "r"
        end_letter = "s"
        result = find_word_with_pattern(sentence, start_letter, end_letter)
        self.assertEqual(result, "roses")  # Expected word is 'roses'
