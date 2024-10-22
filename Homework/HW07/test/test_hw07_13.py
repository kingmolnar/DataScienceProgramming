
from solution_7_13 import find_words_with_length
import unittest

class TestFindWordsWithLength(unittest.TestCase):
    def test_find_words_with_length(self):
        # Test case 1
        sentence = "Python is amazing and fun! I enjoy coding in Python every day."
        target_length = 5
        expected_result = ['enjoy', 'every']
        self.assertEqual(find_words_with_length(sentence, target_length), expected_result)

        # Test case 2
        sentence = "Find the words that have exactly four characters."
        target_length = 4
        expected_result = ['Find', 'that', 'have', 'four']
        self.assertEqual(find_words_with_length(sentence, target_length), expected_result)

        # Test case 3
        sentence = "The quick brown fox jumps over the lazy dog."
        target_length = 3
        expected_result = ['The', 'fox', 'the', 'dog']
        self.assertEqual(find_words_with_length(sentence, target_length), expected_result)

        # Test case 4
        sentence = "I love programming, it's a passion!"
        target_length = 7
        expected_result = ['passion']
        self.assertEqual(find_words_with_length(sentence, target_length), expected_result)

        # Test case 5
        sentence = "Cats, dogs, and birds are common pets."
        target_length = 4
        expected_result = ['Cats', 'dogs', 'pets']
        self.assertEqual(find_words_with_length(sentence, target_length), expected_result)
