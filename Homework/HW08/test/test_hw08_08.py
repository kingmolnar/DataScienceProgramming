
from solution_8_8 import knn_plot_confusion_matrix  # Import your function here

import unittest
import pandas as pd

class TestKNNPlot(unittest.TestCase):

    def setUp(self):
        # Load the dataset for testing
        self.df = pd.read_csv('/data/IFI8410/sess10/reduced_fraud_oracle.csv')

    def test_knn_plot_confusion_matrix(self):
        # Check if the dataset loads properly
        self.assertFalse(self.df.empty, "Dataset should not be empty.")

        # Ensure required columns exist in the dataset
        required_columns = ['VehiclePrice', 'Age', 'DriverRating', 'VehicleCategory', 'PastNumberOfClaims', 'FraudFound_P']
        for column in required_columns:
            self.assertIn(column, self.df.columns, f"Missing required column: {column}")

        # Try running the visualization function
        try:
            knn_plot_confusion_matrix(self.df)
        except Exception as e:
            self.fail(f"Visualization function raised an exception: {e}")
