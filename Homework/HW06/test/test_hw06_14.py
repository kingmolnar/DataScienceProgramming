
import matplotlib.pyplot as plt
import seaborn as sns
import os
import unittest

class TestPlot0614(unittest.TestCase):
    def test_hw06_14(self):
        # Assert that the file exists
        self.assertTrue(os.path.exists("plot_6_14.png"))
