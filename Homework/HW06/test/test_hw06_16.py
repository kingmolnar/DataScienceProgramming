
import matplotlib.pyplot as plt
import seaborn as sns
import os
import unittest

class TestPlot0616(unittest.TestCase):
    def test_hw06_16(self):
        # Assert that the file exists
        self.assertTrue(os.path.exists("plot_6_16.png"))