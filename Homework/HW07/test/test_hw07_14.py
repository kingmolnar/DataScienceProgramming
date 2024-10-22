
from solution_7_14 import find_words_start_end
import unittest

class TestFindWordsStartEnd(unittest.TestCase):
    def test_find_words_start_end(self):
        # Test case 1
        sentence = "Snakes slither silently in the shadows and swiftly strike."
        start_letter = "s"
        end_letter = "y"
        expected_result = ['silently', 'swiftly']
        self.assertEqual(find_words_start_end(sentence, start_letter, end_letter), expected_result)

        # Test case 2
        sentence = "Apples and apricots are amazing fruits that taste great."
        start_letter = "a"
        end_letter = "s"
        expected_result = ['Apples', 'apricots']
        self.assertEqual(find_words_start_end(sentence, start_letter, end_letter), expected_result)

        # Test case 3
        sentence = "The yellow cat sat on the windowsill all day."
        start_letter = "c"
        end_letter = "t"
        expected_result = ['cat']
        self.assertEqual(find_words_start_end(sentence, start_letter, end_letter), expected_result)

        # Test case 4
        sentence = "Dancing daisies dazzle in the daylight."
        start_letter = "d"
        end_letter = "e"
        expected_result = ['dazzle']
        self.assertEqual(find_words_start_end(sentence, start_letter, end_letter), expected_result)

        # Test case 5
        sentence = "He hurried hastily home, holding his hat."
        start_letter = "h"
        end_letter = "y"
        expected_result = ['hastily']
        self.assertEqual(find_words_start_end(sentence, start_letter, end_letter), expected_result)
