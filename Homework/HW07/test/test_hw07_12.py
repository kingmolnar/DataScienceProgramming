
from solution_7_12 import replace_substring
import unittest

class TestReplaceSubstring(unittest.TestCase):
    def test_replace_substring(self):
        # Test case 1
        sentence = "The cat sat on the Cat's mat and scared another cat."
        target = "cat"
        replacement = "dog"
        expected_result = "The dog sat on the dog's mat and scared another dog."
        self.assertEqual(replace_substring(sentence, target, replacement), expected_result)

        # Test case 2
        sentence = "Regex is powerful. Regular expressions (regex) make life easier."
        target = "regex"
        replacement = "pattern"
        expected_result = "pattern is powerful. Regular expressions (pattern) make life easier."
        self.assertEqual(replace_substring(sentence, target, replacement), expected_result)

        # Test case 3
        sentence = "Python is fun. PYTHON is popular."
        target = "python"
        replacement = "coding"
        expected_result = "coding is fun. coding is popular."
        self.assertEqual(replace_substring(sentence, target, replacement), expected_result)

        # Test case 4
        sentence = "The blue bird and BLUE sky."
        target = "blue"
        replacement = "green"
        expected_result = "The green bird and green sky."
        self.assertEqual(replace_substring(sentence, target, replacement), expected_result)

        # Test case 5
        sentence = "Cats and dogs make great pets. CATS love to sleep."
        target = "cats"
        replacement = "birds"
        expected_result = "birds and dogs make great pets. birds love to sleep."
        self.assertEqual(replace_substring(sentence, target, replacement), expected_result)
