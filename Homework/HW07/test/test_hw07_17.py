
import unittest
from solution_7_17 import check_start_word

class TestCheckStartWord(unittest.TestCase):

    def test_check_start_word(self):
        # Test case 1: Sentence starts with 'Python'
        sentence = "Python is a great language."
        word = "Python"
        result = check_start_word(sentence, word)
        self.assertTrue(result)  # Expected output: True

        # Test case 2: Sentence does not start with 'Python'
        sentence = "Java is widely used."
        word = "Python"
        result = check_start_word(sentence, word)
        self.assertFalse(result)  # Expected output: False

        # Test case 3: Case insensitivity check
        sentence = "JavaScript frameworks are popular."
        word = "javascript"
        result = check_start_word(sentence, word)
        self.assertTrue(result)  # Expected output: True

        # Test case 4: Empty string check
        sentence = ""
        word = "Python"
        result = check_start_word(sentence, word)
        self.assertFalse(result)  # Expected output: False
