
from solution_2_13 import caught_speeding

import unittest

class TestHW0213(unittest.TestCase):
    def setUp(self):
        self.is_birthday = True
        self.speed = 80

    def test_hw02_13(self):
        is_birthday = True
        speed = 86
        result = caught_speeding(speed, is_birthday)
        self.assertEqual(result, 'Big Ticket')
        
        speed = 85
        result = caught_speeding(speed, is_birthday)
        self.assertEqual(result, 'Small Ticket')
        
        speed = 65
        result = caught_speeding(speed, is_birthday)
        self.assertEqual(result, 'No Ticket')
       
        is_birthday = False
        speed = 81
        result = caught_speeding(speed, is_birthday)
        self.assertEqual(result, 'Big Ticket')
        
        speed = 80
        result = caught_speeding(speed, is_birthday)
        self.assertEqual(result, 'Small Ticket')
        
        speed = 60
        result = caught_speeding(speed, is_birthday)
        self.assertEqual(result, 'No Ticket') 
