
from solution_10_8 import train_and_evaluate

import unittest
import pandas as pd

class TestModelEvaluation(unittest.TestCase):
    def test_confusion_matrices(self):
        # Define the file path
        file_path = '/data/IFI8410/sess11/Fraud_complete.csv'

        # Define categorical features and target feature
        categorical_features = [
            'Make', 'AccidentArea', 'Sex', 'MaritalStatus', 'Fault',
            'PolicyType', 'VehicleCategory', 'PoliceReportFiled',
            'WitnessPresent', 'BasePolicy'
        ]
        target_feature = 'FraudFound_P'

        # Test the function
        results = train_and_evaluate(file_path, categorical_features, target_feature)

        # Check that all classifiers are in the results and have the expected keys
        self.assertIsInstance(results, dict)
        for key in ['Decision Tree', 'Random Forest', 'XGBoost']:
            self.assertIn(key, results)
            self.assertIn('TP', results[key])
            self.assertIn('FP', results[key])
            self.assertIn('TN', results[key])
            self.assertIn('FN', results[key])

        # Optional: Add more specific checks for expected outcomes
        # For example, check if TP + TN + FP + FN equals the number of test samples
