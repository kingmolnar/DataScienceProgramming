
from solution_8_9 import knn_fraud_probability
import unittest
import pandas as pd

class TestKNNFraudProbability(unittest.TestCase):

    def setUp(self):
        # Load the dataset for testing
        self.df = pd.read_csv('/data/IFI8410/sess10/reduced_fraud_oracle.csv')

    def test_knn_fraud_probability(self):
        # Check if the dataset loads properly
        self.assertFalse(self.df.empty, "Dataset should not be empty.")

        # Ensure required columns exist in the dataset
        required_columns = ['VehiclePrice', 'Age', 'DriverRating', 'VehicleCategory', 'PastNumberOfClaims', 'FraudFound_P']
        for column in required_columns:
            self.assertIn(column, self.df.columns, f"Missing required column: {column}")

        # Run the probability calculation function and capture the output
        try:
            fraud_probabilities = knn_fraud_probability(self.df)
        except Exception as e:
            self.fail(f"Probability function raised an exception: {e}")

        # Check if the result is a DataFrame and contains the expected columns
        self.assertIsInstance(fraud_probabilities, pd.DataFrame, "The result should be a DataFrame.")
        self.assertIn('Fraud_Probability', fraud_probabilities.columns, "Column 'Fraud_Probability' should be in the output.")
        self.assertIn('Actual_Label', fraud_probabilities.columns, "Column 'Actual_Label' should be in the output.")
        
        # Confirm that we have exactly 5 rows in the output
        self.assertEqual(fraud_probabilities.shape[0], 5, "The output should show the top 5 transactions with highest fraud probability.")
        
        # Verify that the Fraud_Probability column values are within the range [0, 1]
        self.assertTrue(fraud_probabilities['Fraud_Probability'].between(0, 1).all(), "Fraud_Probability values should be between 0 and 1.")

        # Check if the Fraud_Probability column is sorted in descending order
        self.assertTrue(fraud_probabilities['Fraud_Probability'].is_monotonic_decreasing, "Fraud_Probability should be sorted in descending order.")
