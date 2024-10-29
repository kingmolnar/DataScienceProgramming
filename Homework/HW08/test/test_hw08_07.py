
from solution_8_7 import knn_fraud_detection

import unittest
import pandas as pd

class TestKNNFraudDetection(unittest.TestCase):

    def setUp(self):
        # Load the dataset
        self.df = pd.read_csv('/data/IFI8410/sess10/reduced_fraud_oracle.csv')

    def test_knn_fraud_detection(self):
        # Run the knn_fraud_detection function
        accuracy, report = knn_fraud_detection(self.df)

        # Combined assertions in one function:

        # Check the dataset integrity
        self.assertFalse(self.df.empty, "Dataset should not be empty.")

        # Ensure the dataset contains the required columns
        required_columns = ['VehiclePrice', 'Age', 'DriverRating', 'VehicleCategory', 'PastNumberOfClaims', 'FraudFound_P']
        for column in required_columns:
            self.assertIn(column, self.df.columns, f"Missing required column: {column}")

        # Verify the accuracy range
        self.assertGreaterEqual(accuracy, 0.0, "Accuracy should be at least 0.0.")
        self.assertLessEqual(accuracy, 1.0, "Accuracy should be at most 1.0.")

        # Ensure the classification report contains precision, recall, and f1-score
        self.assertIn('precision', report, "Classification report is missing 'precision'.")
        self.assertIn('recall', report, "Classification report is missing 'recall'.")
        self.assertIn('f1-score', report, "Classification report is missing 'f1-score'.")

        # Test if the report is not empty
        self.assertTrue(len(report) > 0, "Classification report should not be empty.")
