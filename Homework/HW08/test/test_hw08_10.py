
import unittest
import pandas as pd
from solution_8_10 import hybrid_fraud_detection

class TestHybridFraudDetection(unittest.TestCase):

    def setUp(self):
        # Load the dataset for testing
        self.df = pd.read_csv('/data/IFI8410/sess10/reduced_fraud_oracle.csv')

    def test_hybrid_fraud_detection(self):
        # Check if the dataset loads properly
        self.assertFalse(self.df.empty, "Dataset should not be empty.")

        # Ensure required columns exist in the dataset
        required_columns = ['VehiclePrice', 'Age', 'DriverRating', 'VehicleCategory', 'PastNumberOfClaims', 'FraudFound_P']
        for column in required_columns:
            self.assertIn(column, self.df.columns, f"Missing required column: {column}")

        # Run the hybrid model function and capture outputs
        try:
            accuracy, report = hybrid_fraud_detection(self.df)
        except Exception as e:
            self.fail(f"Hybrid model function raised an exception: {e}")

        # Check if accuracy is a float and report is a string
        self.assertIsInstance(accuracy, float, "Accuracy should be a float.")
        self.assertIsInstance(report, str, "Classification report should be a string.")

        # Verify the accuracy is within an expected range
        self.assertGreaterEqual(accuracy, 0.5, "Expected accuracy to be at least 0.5.")
        self.assertLessEqual(accuracy, 1.0, "Accuracy cannot exceed 1.0.")

        # Check for essential metrics in the classification report
        self.assertIn("precision", report, "Classification report is missing 'precision'.")
        self.assertIn("recall", report, "Classification report is missing 'recall'.")
        self.assertIn("f1-score", report, "Classification report is missing 'f1-score'.")
