
import unittest
from solution_7_18 import extract_emails

class TestExtractEmails(unittest.TestCase):

    def test_extract_emails(self):
        # Test case 1: Multiple valid email addresses
        strings = [
            "Contact us at support@example.com",
            "This is not an email address",
            "Send your queries to info@mydomain.org or feedback@company.net",
            "random_text_with_no_email"
        ]
        result = extract_emails(strings)
        expected = ['support@example.com', 'info@mydomain.org', 'feedback@company.net']
        self.assertEqual(result, expected)

        # Test case 2: Single valid email address
        strings = ["noemails@here", "randomstring", "valid_email@domain.com"]
        result = extract_emails(strings)
        expected = ['valid_email@domain.com']
        self.assertEqual(result, expected)

        # Test case 3: Handling complex email formats
        strings = ["not_an_email@domain", "test@domain.co.uk"]
        result = extract_emails(strings)
        expected = ['test@domain.co.uk']
        self.assertEqual(result, expected)

        # Test case 4: No valid emails
        strings = ["no valid emails here", "another invalid string"]
        result = extract_emails(strings)
        expected = []
        self.assertEqual(result, expected)
