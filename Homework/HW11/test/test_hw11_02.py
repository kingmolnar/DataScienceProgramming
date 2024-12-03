
import unittest
import numpy as np
from sklearn.datasets import make_blobs

from solution_11_2 import kmeans_vs_kmeanspp

class TestKMeansComparison(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.X, _ = make_blobs(n_samples=300, centers=5, cluster_std=1.0, random_state=42)

    def test_kmeans_centroids(self):
        # Ensure the function runs without error and returns expected results
        random_centroids, kmeanspp_centroids = kmeans_vs_kmeanspp(self.X)

        # Test centroid values (example based on expected results for specific dataset)
        expected_random_centroid = [4.5, 2.1]  # Example: Adjust based on dataset and testing
        expected_kmeanspp_centroid = [3.3, 3.1]  # Example: Adjust based on dataset and testing

        np.testing.assert_almost_equal(random_centroids[0], expected_random_centroid, decimal=1, err_msg="Random centroid is incorrect")
        np.testing.assert_almost_equal(kmeanspp_centroids[0], expected_kmeanspp_centroid, decimal=1, err_msg="K-Means++ centroid is incorrect")
