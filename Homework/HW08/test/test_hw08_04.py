
from solution_8_4 import process_and_train_xgboost

import unittest
import pandas as pd

class TestHW0804(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Sample dataset for testing
        cls.file_path = '/data/IFI8410/sess10/Fraud_data.csv'
        cls.df = pd.read_csv(cls.file_path)
        cls.categorical_features = [
            'Make', 'AccidentArea', 'Sex', 'MaritalStatus', 'Fault',
            'PolicyType', 'VehicleCategory', 'PoliceReportFiled',
            'WitnessPresent', 'BasePolicy'
        ]
    
    def test_process_and_train_xgboost(cls):
        accuracy, precision, recall, f1score = process_and_train_xgboost(cls.df, cls.categorical_features)

        # Check if metrics are within valid bounds
        cls.assertTrue(0.8 <= accuracy <= 1.0, "Accuracy out of range")
        cls.assertTrue(0 <= precision <= 0.2, "Precision out of range")
        cls.assertTrue(0 <= recall <= 0.2, "Recall out of range")
        cls.assertTrue(0 <= f1score <= 0.2, "F1-score out of range")
