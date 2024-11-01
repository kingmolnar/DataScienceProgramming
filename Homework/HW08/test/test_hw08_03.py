
from solution_8_3 import process_and_train_decision_tree  # Import the function from your solution file

import unittest
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class TestHW0803(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load data for testing
        cls.file_path = '/data/IFI8410/sess10/Fraud_data.csv'
        cls.df = pd.read_csv(cls.file_path)
        cls.categorical_features = [
            'Make', 'AccidentArea', 'Sex', 'MaritalStatus', 'Fault',
            'PolicyType', 'VehicleCategory', 'PoliceReportFiled',
            'WitnessPresent', 'BasePolicy'
        ]

    def test_process_and_train_decision_tree(self):
        # Ensure the function runs without error and captures metrics
        accuracy, precision, recall, f1score = process_and_train_decision_tree(self.df, self.categorical_features)

        # Check if metrics are within valid bounds
        self.assertTrue(0.87 <= accuracy <= 0.89, "Accuracy out of range")
        self.assertTrue(0.19 <= precision <= 0.21, "Precision out of range")
        self.assertTrue(0.32 <= recall <= 0.34, "Recall out of range")
        self.assertTrue(0.24 <= f1score <= 0.26, "F1-score out of range")
        
