
import matplotlib.pyplot as plt
import seaborn as sns
import os
import unittest

class TestPlot0615(unittest.TestCase):
    def test_hw06_15(self):
        # Assert that the file exists
        self.assertTrue(os.path.exists("plot_6_15.png"))
