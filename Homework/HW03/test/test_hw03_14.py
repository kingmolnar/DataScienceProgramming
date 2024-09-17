
from solution_3_14 import filter_lines

import unittest

class TestHW0314(unittest.TestCase):
    def setUp(self):
        self.input_path = 'input_3.14.txt'
        self.output_path = 'output_3.14.txt'
        
    def test_filter_lines(self):
        filter_lines(self.input_path, self.output_path)
        with open(self.output_path, "r") as f:
            lines = f.readlines()    
            self.assertEqual(len(lines), 6, "Test failed: Incorrect number of lines filtered")
            self.assertEqual(lines[0].strip(), "Hello, welcome to the example file.", "Test failed: Incorrect line content")
            self.assertEqual(lines[1].strip(), "This line is okay.", "Test failed: Incorrect line content")
