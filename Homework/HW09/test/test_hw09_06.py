
from solution_9_6 import train_naive_bayes

import unittest
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer

class TestNaiveBayesModel(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        # Define parameters for test
        self.file_path = '/data/IFI8410/sess10/Fraud_data.csv' 
        self.categorical_features = [
            'Make', 'AccidentArea', 'Sex', 'MaritalStatus', 'Fault', 
            'PolicyType', 'VehicleCategory', 'PoliceReportFiled', 
            'WitnessPresent', 'BasePolicy'
        ]
        self.target_feature = 'FraudFound_P'
        
        # Load data
        df = pd.read_csv(self.file_path)
    
        # Split data into features and target
        self.X = df[self.categorical_features]
        self.y = df[self.target_feature]
        
        # Split the data into training and test sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.3, random_state=1
        )
        
    def test_train_naive_bayes(self): 
        y_pred = train_naive_bayes(self.file_path, self.categorical_features, self.target_feature)
        
        # Ensure predictions are made
        self.assertEqual(len(y_pred), len(self.y_test), "Number of predictions should match test set size")
        self.assertTrue(all(pred in [0, 1] for pred in y_pred), "Predictions should be binary (0 or 1)")
    
        # Check that the encoder is correctly configured to handle categorical variables
        encoder = OneHotEncoder(handle_unknown='ignore', drop='first', sparse_output=False)
        encoded = encoder.fit_transform(self.X_train)
        
        # Check that the transformed shape matches expected dimensions
        self.assertEqual(encoded.shape[0], self.X_train.shape[0], "Encoded features should match training set rows")
        self.assertGreater(encoded.shape[1], 0, "Encoded features should have non-zero columns")
