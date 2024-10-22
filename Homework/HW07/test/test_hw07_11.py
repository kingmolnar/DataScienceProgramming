
from solution_7_11 import count_word_occurrences_advanced

import unittest

class TestCountWordOccurrencesAdvanced(unittest.TestCase):
    def test_count_word_occurrences_advanced(self):
        # Test case 1
        paragraph = "Python, the best language! python is versatile; many prefer Python, but not everyone loves python."
        target_word = "python"
        self.assertEqual(count_word_occurrences_advanced(paragraph, target_word), 4)

        # Test case 2
        paragraph = "Regex is powerful. Regular expressions (regex) are a must-know!"
        target_word = "regex"
        self.assertEqual(count_word_occurrences_advanced(paragraph, target_word), 2)

        # Test case 3
        paragraph = "The quick brown fox jumps over the lazy dog."
        target_word = "cat"
        self.assertEqual(count_word_occurrences_advanced(paragraph, target_word), 0)

        # Test case 4
        paragraph = "Hello, world! Hello world? Hello-world; Hello... world!"
        target_word = "hello"
        self.assertEqual(count_word_occurrences_advanced(paragraph, target_word), 4)

        # Test case 5
        paragraph = "Python is amazing. PYTHON is powerful. pythonic is something else."
        target_word = "python"
        self.assertEqual(count_word_occurrences_advanced(paragraph, target_word), 2)
