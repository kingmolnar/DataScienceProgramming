
from solution_9_9 import train_and_evaluate_svm

import unittest

class TestSVMModel(unittest.TestCase):
    def setUp(self):
        # Define paths and settings
        self.file_path = '/data/IFI8410/sess10/Fraud_data.csv' 
        self.categorical_features = [
            'Make', 'AccidentArea', 'Sex', 'MaritalStatus', 'Fault',
            'PolicyType', 'VehicleCategory', 'PoliceReportFiled',
            'WitnessPresent', 'BasePolicy'
        ]
        self.target_feature = 'FraudFound_P'

    def test_train_and_evaluate_svm(self):
        # Run the function
        metrics = train_and_evaluate_svm(self.file_path, self.categorical_features, self.target_feature)

        # Assertions to check metric values
        self.assertIsInstance(metrics, dict, "Metrics should be returned in a dictionary format.")
        self.assertIn("accuracy", metrics, "Accuracy metric should be present.")
        self.assertIn("precision", metrics, "Precision metric should be present.")
        self.assertIn("recall", metrics, "Recall metric should be present.")
        self.assertIn("f1_score", metrics, "F1-Score metric should be present.")

        # Check that metrics are within a valid range
        for metric_name, metric_value in metrics.items():
            self.assertGreaterEqual(metric_value, 0, f"{metric_name} should be non-negative.")
            self.assertLessEqual(metric_value, 1, f"{metric_name} should not exceed 1.")
