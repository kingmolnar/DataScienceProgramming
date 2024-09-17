
from solution_3_7 import filter_names_with_a
import unittest

class TestHW0307(unittest.TestCase):
    def setUp(self):
        self.all_data = [["Sara", "Anna"], ["Bob", "Alexandra"], ["David", "Amanda"]]

    # Test 1: Standard case with names containing two or more 'a's
    def test_filter_names_with_a(self):
        
        print(self.all_data)
        
        result = filter_names_with_a(self.all_data)
        expected_result = ["Sara", "Anna", "Alexandra", "Amanda"]
        self.assertEqual(result, expected_result)

    # # Test 2: No names containing two or more 'a's
    # def test_no_names_with_a(self):
    #     all_data = [["Bob", "Chris"], ["Eve", "John"]]
    #     result = filter_names_with_a(all_data)
    #     expected_result = []
    #     self.assertEqual(result, expected_result)
    # 
    # # Test 3: All names containing two or more 'a's
    # def test_all_names_with_a(self):
    #     all_data = [["Sara", "Anna"], ["Amanda"]]
    #     result = filter_names_with_a(all_data)
    #     expected_result = ["Sara", "Anna", "Amanda"]
    #     self.assertEqual(result, expected_result)
    # 
    # # Test 4: Empty input list
    # def test_empty_list(self):
    #     result = filter_names_with_a([])
    #     expected_result = []
    #     self.assertEqual(result, expected_result)
    # 
    # # Test 5: Mixed-case names
    # def test_mixed_case_names(self):
    #     all_data = [["SaRa", "ANNa"], ["bob", "AManDa"]]
    #     result = filter_names_with_a(all_data)
    #     expected_result = ["SaRa", "ANNa", "AManDa"]
    #     self.assertEqual(result, expected_result)
