
from solution_4_1 import create_ndarray
import unittest
import numpy as np

class TestHW0401(unittest.TestCase):
    def test_create_ndarray(self):
        result = create_ndarray()
        expected = np.zeros((3, 4))
        np.testing.assert_array_equal(result, expected)
