
from solution_4_13 import calculate_stats
import unittest
import numpy as np

class TestHW0413(unittest.TestCase):
    def test_calculate_stats(self):
        arr = np.array([1, 2, 3, 4, 5, 6])
        mean_val, std_dev, total_sum = calculate_stats(arr)
        self.assertAlmostEqual(mean_val, 3.5)
        self.assertAlmostEqual(std_dev, 1.707825127659933, places=5)
        self.assertEqual(total_sum, 21)
