
from solution_8_7 import knn_fraud_detection
import unittest
import pandas as pd

class TestKNNFraudDetection(unittest.TestCase):

    def setUp(self):
        # Load the dataset
        self.df = pd.read_csv('/data/IFI8410/sess10/reduced_fraud_oracle.csv')

    def test_knn_fraud_detection_combined(self):
        # Run the knn_fraud_detection function
        accuracy, report = knn_fraud_detection(self.df)

        # Check the dataset integrity
        self.assertFalse(self.df.empty, "Dataset should not be empty.")

        # Ensure the dataset contains the required columns
        required_columns = ['VehiclePrice', 'Age', 'DriverRating', 'VehicleCategory', 'PastNumberOfClaims', 'FraudFound_P']
        for column in required_columns:
            self.assertIn(column, self.df.columns, f"Missing required column: {column}")

        # Verify the accuracy range
        self.assertIsInstance(accuracy, float, "Accuracy should be a float.")
        self.assertGreaterEqual(accuracy, 0.0, "Accuracy should be at least 0.0.")
        self.assertLessEqual(accuracy, 1.0, "Accuracy should be at most 1.0.")

        # Ensure the classification report contains essential metrics
        self.assertIn('precision', report, "Classification report is missing 'precision'.")
        self.assertIn('recall', report, "Classification report is missing 'recall'.")
        self.assertIn('f1-score', report, "Classification report is missing 'f1-score'.")

        # Check that the classification report is meaningful (not empty)
        lines = report.split('\n')
        f1_scores = [float(line.split()[3]) for line in lines if len(line.split()) >= 4 and line.split()[3].replace('.', '', 1).isdigit()]
        self.assertTrue(any(f1 > 0 for f1 in f1_scores), "All F1-scores are zero, indicating potential issues with predictions.")
