
from solution_4_9 import generate_random_array
import unittest
import numpy as np

class TestHW0409(unittest.TestCase):
    def test_generate_random_array(self):
        result = generate_random_array()
        self.assertEqual(result.shape, (3, 3))  # Check the shape of the array
        self.assertTrue(np.issubdtype(result.dtype, np.float64))  # Check that the datatype is float64
