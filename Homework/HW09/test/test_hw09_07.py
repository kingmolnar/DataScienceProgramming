
from solution_9_7 import naive_bayes_metrics

import unittest

class TestNaiveBayesModel(unittest.TestCase):
    def setUp(self):
        # Define parameters for test
        self.file_path = '/data/IFI8410/sess10/Fraud_data.csv' 
        self.categorical_features = [
            'Make', 'AccidentArea', 'Sex', 'MaritalStatus', 'Fault', 
            'PolicyType', 'VehicleCategory', 'PoliceReportFiled', 
            'WitnessPresent', 'BasePolicy'
        ]
        self.target_feature = 'FraudFound_P'

    def test_naive_bayes_metrics(self):
        # Call the function
        metrics = naive_bayes_metrics(self.file_path, self.categorical_features, self.target_feature)

        # Check that metrics are within valid ranges
        self.assertGreaterEqual(metrics['accuracy'], 0.0)
        self.assertLessEqual(metrics['accuracy'], 1.0)
        self.assertGreaterEqual(metrics['precision'], 0.0)
        self.assertLessEqual(metrics['precision'], 1.0)
        self.assertGreaterEqual(metrics['recall'], 0.0)
        self.assertLessEqual(metrics['recall'], 1.0)
        self.assertGreaterEqual(metrics['f1_score'], 0.0)
        self.assertLessEqual(metrics['f1_score'], 1.0)
