
from solution_8_6 import knn_classifier
import unittest
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder

class TestHW0806(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Sample dataset for testing
        cls.df = pd.read_csv('/data/IFI8410/sess10/reduced_fraud_oracle.csv')
        cls.feature_columns = ['WeekOfMonth', 'AccidentArea', 'Sex', 'MaritalStatus', 'Age', 'Fault', 'VehicleCategory', 'Deductible', 'DriverRating', 'PoliceReportFiled']
        cls.target_column = 'BasePolicy'

    def test_knn_classifier_combined(self):
        # Run the classifier function
        accuracy, report = knn_classifier(self.df, self.feature_columns, self.target_column)

        # Check if the accuracy is a valid float between 0 and 1
        self.assertIsInstance(accuracy, float, "Accuracy should be a float.")
        self.assertGreaterEqual(accuracy, 0.0, "Accuracy should be at least 0.0.")
        self.assertLessEqual(accuracy, 1.0, "Accuracy should not exceed 1.0.")
        
        # Verify that the classification report contains necessary metrics
        self.assertIn("precision", report, "Report should include precision metric.")
        self.assertIn("recall", report, "Report should include recall metric.")
        self.assertIn("f1-score", report, "Report should include F1-score metric.")
        
        # Ensure accuracy is non-zero to indicate model is learning something
        self.assertGreater(accuracy, 0.0, "The model's accuracy is too low, possibly indicating issues.")
        
        # Check that at least one label has a non-zero F1-score
        lines = report.split('\n')
        f1_scores = [float(line.split()[3]) for line in lines if len(line.split()) >= 4 and line.split()[3].replace('.', '', 1).isdigit()]
        self.assertTrue(any(f1 > 0 for f1 in f1_scores), "All F1-scores are zero, indicating prediction issues.")
        
        # Confirm LabelEncoder was applied if target is categorical
        y = self.df[self.target_column]
        if y.dtype == 'object':
            self.assertTrue(hasattr(LabelEncoder(), 'fit_transform'), "Target should be label-encoded if categorical.")
