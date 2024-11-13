
from solution_10_10 import load_and_preprocess_data, train_logistic_regression

import unittest

class TestLogisticRegressionAUC(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # Define file path and columns for testing
        self.file_path = '/data/IFI8410/sess11/Fraud_complete.csv'
        self.categorical_features = [
            'Make', 'AccidentArea', 'Sex', 'MaritalStatus', 'Fault',
            'PolicyType', 'VehicleCategory', 'PoliceReportFiled',
            'WitnessPresent', 'BasePolicy'
        ]
        self.target_feature = 'FraudFound_P'
    
    def test_train_logistic_regression(self):

        X, y = load_and_preprocess_data(self.file_path, self.categorical_features, self.target_feature)
        
        auc = train_logistic_regression(X, y, self.categorical_features)
        
        # Validate that AUC is a float
        self.assertIsInstance(auc, float, "AUC should be a float value.")

        # Validate that AUC is within a reasonable range
        self.assertGreater(auc, 0.5, "AUC should be greater than 0.5 for a valid model.")
        self.assertLessEqual(auc, 1.0, "AUC should not exceed 1.0.")
