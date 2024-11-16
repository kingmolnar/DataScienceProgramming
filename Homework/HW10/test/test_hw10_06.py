
from solution_10_6 import get_metrics

import unittest
import pandas as pd
from sklearn.model_selection import train_test_split

class TestModelMetrics(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Define file path and categorical features as per the function's requirements
        cls.file_path = '/data/IFI8410/sess11/Fraud_complete.csv'
        cls.categorical_features = [
            'Make', 'AccidentArea', 'Sex', 'MaritalStatus', 'Fault',
            'PolicyType', 'VehicleCategory', 'PoliceReportFiled',
            'WitnessPresent', 'BasePolicy'
        ]
        cls.target_feature = 'FraudFound_P'

        # Load data
        df = pd.read_csv(cls.file_path)

        # Split data into features and target
        X = df[cls.categorical_features]
        y = df[cls.target_feature]

        # Split the data into training and test sets
        cls.X_train, cls.X_test, cls.y_train, cls.y_test = train_test_split(
            X, y, test_size=0.3, random_state=1
        )

    def test_model_metrics(self):
        # Fetch metrics from the function
        metrics = get_metrics(self.X_train, self.X_test, self.y_train, self.y_test)

        # Check if metrics for all models are returned
        self.assertIsInstance(metrics, dict, "Metrics should be returned in a dictionary format.")
        for model_name, model_metrics in metrics.items():
            self.assertIn('Precision', model_metrics, f"Precision metric should be present for {model_name}.")
            self.assertIn('Recall', model_metrics, f"Recall metric should be present for {model_name}.")
            self.assertIn('F1 Score', model_metrics, f"F1 Score metric should be present for {model_name}.")

            # Validate the range of metric values
            self.assertTrue(0 <= model_metrics['Precision'] <= 1, "Precision must be between 0 and 1.")
            self.assertTrue(0 <= model_metrics['Recall'] <= 1, "Recall must be between 0 and 1.")
            self.assertTrue(0 <= model_metrics['F1 Score'] <= 1, "F1 Score must be between 0 and 1.")
