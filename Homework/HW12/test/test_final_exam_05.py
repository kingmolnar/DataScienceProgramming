
from solution_5 import plot_clustering_results

import matplotlib.pyplot as plt
import seaborn as sns
import os
import unittest

class TestClusteringComparison(unittest.TestCase):
    def test_plot_clustering_results(self):
        DIR = os.path.dirname(__file__)
        os.path.join(DIR, '...', 'comparison_of_clustering_techniques.png')
        # Assert that the file exists
        self.assertTrue(os.path.exists('comparison_of_clustering_techniques.png'))
        
