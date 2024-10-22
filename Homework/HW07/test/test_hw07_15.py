
from solution_7_15 import transform_text

import unittest
import re

class TestTransformText(unittest.TestCase):

    def setUp(self):
        self.file_path = "/data/IFI8410/sess07/RE_Text.txt"

    def test_transform_text(self):
        word_length = 5
        start_letter = "r"
        end_letter = "s"

        # Apply the function
        modified_text, length_words, start_end_words = transform_text(self.file_path, word_length, start_letter, end_letter)

        print(modified_text)
        
        # Expected modified text after extracting from the RTF file and performing transformations
        expected_text = '\"Regular expressions are a powerful tool used for pattern matching in strings. They are commonly used in text processing tasks such as searching, replacing, or splitting text based on specific patterns. With regular expressions, you can extract phone numbers, emails, or URLs from a body of text, or clean up messy data by removing unwanted characters. Mastering regular expressions can significantly improve your ability to manipulate and analyze textual data efficiently.\"'

        print(expected_text)
        
        # Check if the modification is correct
        self.assertEqual(modified_text, expected_text)

        # Expected words of specific length
        expected_length_words = ['tasks', 'based', 'phone', 'clean', 'messy']
        self.assertEqual(length_words, expected_length_words)

        # Expected words that start with 'r' and end with 's'
        expected_start_end_words = []  # Example doesn't contain any such words
        self.assertEqual(start_end_words, expected_start_end_words)
