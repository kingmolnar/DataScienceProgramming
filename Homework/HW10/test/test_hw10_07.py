
from solution_10_7 import train_and_evaluate_models

import unittest

class TestModelClassAccuracies(unittest.TestCase):
    def test_class_accuracies(self):
        file_path = '/data/IFI8410/sess11/Fraud_complete.csv'
        categorical_features = ['Make', 'AccidentArea', 'Sex', 'MaritalStatus', 'Fault', 'PolicyType', 'VehicleCategory', 'PoliceReportFiled', 'WitnessPresent', 'BasePolicy']
        target_feature = 'FraudFound_P'
        accuracies = train_and_evaluate_models(file_path, categorical_features, target_feature)

        # Ensure the accuracies dictionary is not empty
        self.assertIsInstance(accuracies, dict)
        self.assertNotEqual(len(accuracies), 0)

        # Check if all expected models are present and their accuracy is a float
        expected_models = ['Decision Tree', 'Random Forest', 'XGBoost']
        for model in expected_models:
            self.assertIn(model, accuracies)
            self.assertIsInstance(accuracies[model], float)

        # Check the range of accuracies
        for accuracy in accuracies.values():
            self.assertGreaterEqual(accuracy, 0.0)
            self.assertLessEqual(accuracy, 1.0)
