
from solution_8_2 import create_one_hot_encoder  # Assuming the function is in 'solution_8_2.py'

import unittest
import pandas as pd

class TestHW0802(unittest.TestCase):
    def setUp(self):
        # Load the dataset
        self.file_path = '/data/IFI8410/sess10/reduced_fraud_oracle.csv'
        self.df = pd.read_csv(self.file_path)

        # Define the list of categorical features to encode
        self.categorical_features = [
            'Make', 'AccidentArea', 'Sex', 'MaritalStatus', 'Fault',
            'PolicyType', 'VehicleCategory', 'PoliceReportFiled',
            'WitnessPresent', 'BasePolicy'
        ]

    def test_create_one_hot_encoder(self):
        # Create and fit the one-hot encoder
        encoder = create_one_hot_encoder(self.df, self.categorical_features)

        # Expected categories in each categorical feature (this is just a sample format; adjust based on actual data)
        expected_categories = [
            ['Honda', 'Toyota', 'Ford'],  # Example values for 'Make' (replace with actual categories if needed)
            ['Urban', 'Rural'],           # 'AccidentArea'
            ['Male', 'Female'],           # 'Sex'
            ['Single', 'Married'],        # 'MaritalStatus'
            # Add expected categories for each feature here
        ]

        # Check that the encoder has the correct number of categories (columns)
        self.assertEqual(len(encoder.categories_), len(self.categorical_features))
        
        # Check if each category in encoder matches expected categories (for demonstration purposes)
        # Adjust the length of expected categories array based on actual column values.
        for idx, category in enumerate(encoder.categories_):

            if idx < len(expected_categories):  # Make sure expected_categories has an entry for the column
                self.assertTrue(set(expected_categories[idx]).issubset(set(category)))
                
