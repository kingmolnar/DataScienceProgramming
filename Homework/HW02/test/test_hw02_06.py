
from solution_2_6 import generate_student_ids

import unittest

class TestHW0206(unittest.TestCase):
    def setUp(self):
        self.students = ["Alice", "Bob", "Charlie", "David"]
        
    def test_hw02_06(self):
        generator = generate_student_ids(self.students)
        student_ids = list(generator)
        self.assertCountEqual(student_ids, [1001, 1002, 1003, 1004])
