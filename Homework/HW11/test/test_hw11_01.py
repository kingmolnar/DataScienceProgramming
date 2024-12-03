
from solution_11_1 import kmeans_with_elbow_method

import unittest
import numpy as np
from sklearn.datasets import make_blobs

class TestKMeansClustering(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.X, _ = make_blobs(n_samples=300, centers=5, cluster_std=1.0, random_state=42)
    
    def test_kmeans_with_elbow_method(self):
        # Ensure the function runs without error and returns expected results
        centroid = kmeans_with_elbow_method(self.X)

        # Test centroid values (Cluster 0 centroid rounded to 2 decimals)
        expected_centroid = [ 2.1,  4.1 ]  # Example: Adjust this based on actual centroid from testing
        np.testing.assert_almost_equal(centroid, expected_centroid, decimal=1, err_msg="Centroid coordinates are incorrect")
