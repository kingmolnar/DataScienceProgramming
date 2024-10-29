
from solution_8_9 import knn_fraud_probability

import unittest
import pandas as pd

class TestKNNFraudProbability(unittest.TestCase):

    def setUp(self):
        # Load the dataset for testing
        self.df = pd.read_csv('//data/IFI8410/sess10/reduced_fraud_oracle.csv')

    def test_knn_fraud_probability(self):
        # Check if the dataset loads properly
        self.assertFalse(self.df.empty, "Dataset should not be empty.")

        # Ensure required columns exist in the dataset
        required_columns = ['VehiclePrice', 'Age', 'DriverRating', 'VehicleCategory', 'PastNumberOfClaims', 'FraudFound_P']
        for column in required_columns:
            self.assertIn(column, self.df.columns, f"Missing required column: {column}")

        # Try running the probability calculation function
        try:
            fraud_probabilities = knn_fraud_probability(self.df)
        except Exception as e:
            self.fail(f"Probability function raised an exception: {e}")

        # Check if the result is a DataFrame and contains the expected columns
        self.assertIsInstance(fraud_probabilities, pd.DataFrame, "The result should be a DataFrame.")
        self.assertIn('Fraud_Probability', fraud_probabilities.columns, "Column 'Fraud_Probability' should be in the output.")
        self.assertEqual(fraud_probabilities.shape[0], 5, "The output should show the top 5 transactions with highest fraud probability.")
