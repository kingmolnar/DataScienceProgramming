
from solution_1 import process_and_train_decision_tree  

import unittest
import pandas as pd

class TestDecisionTree(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # Load data for testing
        self.file_path = '/data/IFI8410/finalexam/HR_Analytics.csv'
        data = pd.read_csv(self.file_path)

        # Create binary target feature for binary classification:
        data.loc[data['salary'] == 'low', 'binary_salary'] = 0
        data.loc[data['salary'] == 'medium', 'binary_salary'] = 0
        data.loc[data['salary'] == 'high', 'binary_salary'] = 1
        data['binary_salary'] = data['binary_salary'].astype(int)
        data.drop(columns=['salary'], inplace = True)

        self.df = data.copy()
        self.categorical_features = [
            'Work_accident',
            'left',
            'promotion_last_5years',
            'Department',
        ]
        self.target_feature = 'binary_salary'

    def test_process_and_train_decision_tree(self):
        # Ensure the function runs without error and captures metrics
        accuracy, precision, recall, f1score = process_and_train_decision_tree(
            self.df, self.categorical_features, self.target_feature
        )

        # Check if metrics are within valid bounds
        self.assertTrue(0.1 <= accuracy <= 1.0, "Accuracy out of range")
        self.assertTrue(0.1 <= precision <= 1.0, "Precision out of range")
        self.assertTrue(0.1 <= recall <= 1.0, "Recall out of range")
        self.assertTrue(0.1 <= f1score <= 1.0, "F1-score out of range")
        
