
from solution_3_2 import unpack_person

import unittest

class TestHW0302(unittest.TestCase):
    def setUp(self):
        self.person = ("John", 28, "Engineer")

    def test_hw03_02(self):
        results = unpack_person(self.person)
        self.assertEqual(results[0], "John")
        self.assertEqual(results[1], 28)
        self.assertEqual(results[2], "Engineer")
