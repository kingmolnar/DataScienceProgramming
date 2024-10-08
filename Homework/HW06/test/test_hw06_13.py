
import matplotlib.pyplot as plt
import seaborn as sns
import os
import unittest

class TestPlot0613(unittest.TestCase):
    def test_hw06_13(self):
        # Assert that the file exists
        self.assertTrue(os.path.exists("plot_6_13.png"))
