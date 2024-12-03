
from solution_11_4 import apply_dbscan_and_plot

import matplotlib.pyplot as plt
import seaborn as sns
import os
import unittest

class TestDBSCANClustering(unittest.TestCase):
    def test_apply_dbscan_and_plot(self):
        # Assert that the file exists
        self.assertTrue(os.path.exists("dbscan_blobs_and_rings.png"))
