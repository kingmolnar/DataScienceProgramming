
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

        expected_accuracy = 0.907
        expected_precision = 0.143
        expected_recall = 0.111
        expected_f1score = 0.125

        cls.assertAlmostEqual(expected_accuracy, accuracy, 2)
        cls.assertAlmostEqual(expected_precision, precision, 2)
        cls.assertAlmostEqual(expected_recall, recall, 2)
        cls.assertAlmostEqual(expected_f1score, f1score, 2)
