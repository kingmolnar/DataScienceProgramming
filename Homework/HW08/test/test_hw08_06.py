
from solution_8_6 import knn_classifier

import unittest
import pandas as pd

class TestHW0806(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Sample dataset for testing
        cls.df = pd.read_csv('/data/IFI8410/sess10/reduced_fraud_oracle.csv')
        cls.feature_columns = ['WeekOfMonth', 'AccidentArea', 'Sex', 'MaritalStatus', 'Age', 'Fault', 'VehicleCategory', 'Deductible', 'DriverRating', 'PoliceReportFiled']
        cls.target_column = 'BasePolicy'

    def test_knn_classifier(self):
        # Run the classifier function
        accuracy, report = knn_classifier(self.df, self.feature_columns, self.target_column)

        # Test 1: Accuracy is a valid float between 0 and 1
        self.assertIsInstance(accuracy, float)
        self.assertGreaterEqual(accuracy, 0.0)
        self.assertLessEqual(accuracy, 1.0)

        # Test 2: Report contains necessary metrics
        self.assertIn("precision", report)
        self.assertIn("recall", report)
        self.assertIn("f1-score", report)

        # Test 3: Accuracy should not be zero
        self.assertGreater(accuracy, 0.0, "The model's accuracy is too low, indicating possible data or implementation issues.")

        # Test 4: Ensure at least one label has a non-zero F1-score
        lines = report.split('\n')
        f1_scores = [float(line.split()[3]) for line in lines if len(line.split()) >= 4 and line.split()[3].replace('.', '', 1).isdigit()]
        self.assertTrue(any(f1 > 0 for f1 in f1_scores), "All F1-scores are zero, indicating model prediction issues.")
