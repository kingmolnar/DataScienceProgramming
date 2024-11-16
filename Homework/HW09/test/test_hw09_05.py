
from solution_9_5 import compute_confusion_matrix

import unittest
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix

class TestConfusionMatrixVisualization(unittest.TestCase):

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

    def test_compute_confusion_matrix(self):
        
        cm_calculated = compute_confusion_matrix(self.df, self.target, self.categorical_features, self.numeric_features)
        
        # Assert that the confusion matrix dimensions are correct (2x2 for binary classification)
        self.assertEqual(cm_calculated.shape, (2, 2), "Confusion matrix should be 2x2 for binary classification")

        # Assert that all values in the confusion matrix are integers (count of instances)
        self.assertTrue(np.all(cm_calculated == cm_calculated.astype(int)), "All confusion matrix values should be integers")

        # Assert specific ranges for confusion matrix components if possible
        tn, fp, fn, tp = cm_calculated.ravel()

        # Define reasonable expected ranges based on the data and model performance (customize as needed)
        self.assertTrue(tn >= 0, "True Negatives should be non-negative")
        self.assertTrue(fp >= 0, "False Positives should be non-negative")
        self.assertTrue(fn >= 0, "False Negatives should be non-negative")
        self.assertTrue(tp >= 0, "True Positives should be non-negative")
