import unittest
import pandas as pd
from solution_9_8 import load_and_train_svm_model
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class TestSVMModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Define the file path and features
        cls.file_path = '/data/IFI8410/sess10/Fraud_data.csv' 
        cls.categorical_features = [
            'Make', 'AccidentArea', 'Sex', 'MaritalStatus', 'Fault', 
            'PolicyType', 'VehicleCategory', 'PoliceReportFiled', 
            'WitnessPresent', 'BasePolicy'
        ]
        cls.target_feature = 'FraudFound_P'
        
        # Load the model and predictions
        cls.y_pred_svm, cls.y_test, cls.label_encoder = load_and_train_svm_model(
            cls.file_path, cls.categorical_features, cls.target_feature
        )

    def test_load_and_train_svm_model(self):
        # Check that predictions were made
        self.assertTrue(len(self.y_pred_svm) > 0, "Predictions should not be empty")

        # Ensure that the predictions only contain valid labels (0 or 1)
        unique_labels = set(self.y_pred_svm)
        self.assertTrue(unique_labels.issubset({0, 1}), "Predictions should contain only 0 or 1")

        # Ensure accuracy is above a threshold to confirm model performance
        accuracy = accuracy_score(self.y_test, self.y_pred_svm)
        self.assertGreaterEqual(accuracy, 0.5, "Accuracy should be at least 0.5 for a balanced dataset")

        # Check that metrics meet basic thresholds without printing
        precision = precision_score(self.y_test, self.y_pred_svm, pos_label=1, zero_division=0)
        recall = recall_score(self.y_test, self.y_pred_svm, pos_label=1, zero_division=0)
        f1 = f1_score(self.y_test, self.y_pred_svm, pos_label=1, zero_division=0)
        
        # Assert minimum performance thresholds without printing
        self.assertGreaterEqual(precision, 0.05, "Precision should be at least 0.05")
        self.assertGreaterEqual(recall, 0.05, "Recall should be at least 0.05")
        self.assertGreaterEqual(f1, 0.05, "F1 Score should be at least 0.05")
