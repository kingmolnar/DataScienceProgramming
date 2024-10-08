
import matplotlib.pyplot as plt
import seaborn as sns
import os
import unittest

class TestPlot0618(unittest.TestCase):
    def test_hw06_18(self):
        # Assert that the file exists
        self.assertTrue(os.path.exists("plot_6_18.png"))
