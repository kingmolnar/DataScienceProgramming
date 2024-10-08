
import matplotlib.pyplot as plt
import seaborn as sns
import os
import unittest

class TestPlot0611(unittest.TestCase):
    def test_hw06_11(self):
        # Assert that the file exists
        self.assertTrue(os.path.exists("plot_6_11.png"))
