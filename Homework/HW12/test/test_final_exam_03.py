
from solution_3 import naive_bayes_metrics

import pandas as pd
import unittest

class TestNaiveBayesModel(unittest.TestCase):
    def setUp(self):

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
    
    def test_naive_bayes_metrics(self):
        # Call the function
        metrics = naive_bayes_metrics(
            self.df, self.categorical_features, self.target_feature
        )

        # Check that metrics are within valid ranges
        self.assertGreaterEqual(metrics['accuracy'], 0.0)
        self.assertLessEqual(metrics['accuracy'], 1.0)
        self.assertGreaterEqual(metrics['precision'], 0.0)
        self.assertLessEqual(metrics['precision'], 1.0)
        self.assertGreaterEqual(metrics['recall'], 0.0)
        self.assertLessEqual(metrics['recall'], 1.0)
        self.assertGreaterEqual(metrics['f1_score'], 0.0)
        self.assertLessEqual(metrics['f1_score'], 1.0)
        
