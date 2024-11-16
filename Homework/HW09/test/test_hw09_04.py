
from solution_9_4 import process_and_train_logistic_regression

import unittest
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class TestLogisticRegressionModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load data for testing
        cls.file_path = '/data/IFI8410/sess10/HR_Analytics.csv'
        cls.df = pd.read_csv(cls.file_path)

        # Define target, categorical, and numeric columns
        cls.target = 'left'
        cls.categorical_features = ['Department', 'salary']
        cls.numeric_features = [
            'satisfaction_level', 'last_evaluation', 'number_project',
            'average_montly_hours', 'time_spend_company', 'Work_accident',
            'promotion_last_5years'
        ]

    def test_process_and_train_logistic_regression(self):
        # Run the function and get outputs
        accuracy, precision, recall, f1score = process_and_train_logistic_regression(
            self.df, self.target, self.categorical_features, self.numeric_features
        )

        # Check output types
        self.assertIsInstance(accuracy, float, "Accuracy should be a float")
        self.assertIsInstance(precision, float, "Precision should be a float")
        self.assertIsInstance(recall, float, "Recall should be a float")
        self.assertIsInstance(f1score, float, "F1-Score should be a float")

        # Check if metrics are within valid range [0, 1]
        self.assertTrue(0.0 <= accuracy <= 1.0, "Accuracy out of valid range")
        self.assertTrue(0.0 <= precision <= 1.0, "Precision out of valid range")
        self.assertTrue(0.0 <= recall <= 1.0, "Recall out of valid range")
        self.assertTrue(0.0 <= f1score <= 1.0, "F1-Score out of valid range")
