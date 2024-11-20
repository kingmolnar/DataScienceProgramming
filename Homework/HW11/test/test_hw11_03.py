
from solution_11_3 import plot_ahc_clustering

import matplotlib.pyplot as plt
import seaborn as sns
import os
import unittest

class TestAHCClustering(unittest.TestCase):
    def test_plot_ahc_clustering(self):
        # Assert that the file exists
        self.assertTrue(os.path.exists("ahc_clustering_average.png"))
                        
