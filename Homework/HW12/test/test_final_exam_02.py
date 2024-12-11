
from solution_2 import knn_salary_classification
import unittest
import pandas as pd

class TestKNNFraudDetection(unittest.TestCase):

    def setUp(self):
        # # Load the dataset
        # self.df = pd.read_csv('/data/IFI8410/finalexam/reduced_fraud_oracle.csv')

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
        
    def test_knn_salary_classification(self):
        # Run the knn_fraud_detection function
        accuracy, report = knn_salary_classification(self.df)

        # Check the dataset integrity
        self.assertFalse(self.df.empty, "Dataset should not be empty.")

        # Verify the accuracy range
        self.assertIsInstance(accuracy, float, "Accuracy should be a float.")
        self.assertGreaterEqual(accuracy, 0.0, "Accuracy should be at least 0.0.")
        self.assertLessEqual(accuracy, 1.0, "Accuracy should be at most 1.0.")

        # Ensure the classification report contains essential metrics
        self.assertIn('precision', report, "Classification report is missing 'precision'.")
        self.assertIn('recall', report, "Classification report is missing 'recall'.")
        self.assertIn('f1-score', report, "Classification report is missing 'f1-score'.")

        # Check that the classification report is meaningful (not empty)
        lines = report.split('\n')
        f1_scores = [float(line.split()[3]) for line in lines if len(line.split()) >= 4 and line.split()[3].replace('.', '', 1).isdigit()]
        self.assertTrue(any(f1 > 0 for f1 in f1_scores), "All F1-scores are zero, indicating potential issues with predictions.")
