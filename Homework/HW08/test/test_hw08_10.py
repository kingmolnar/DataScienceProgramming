
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

        # Try running the hybrid model function
        try:
            accuracy, report = hybrid_fraud_detection(self.df)
        except Exception as e:
            self.fail(f"Hybrid model function raised an exception: {e}")

        # Check if the accuracy is a float and the report is a string
        self.assertIsInstance(accuracy, float, "Accuracy should be a float.")
        self.assertIsInstance(report, str, "Classification report should be a string.")

        # Check if accuracy is within a reasonable range
        self.assertGreaterEqual(accuracy, 0.5, "Expected accuracy to be at least 0.5.")
        self.assertLessEqual(accuracy, 1.0, "Accuracy cannot exceed 1.0.")
