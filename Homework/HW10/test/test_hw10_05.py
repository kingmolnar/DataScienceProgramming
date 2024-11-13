
from solution_10_5 import model_comparison_r2

import unittest
import pandas as pd

class TestModelComparisonR2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load the dataset for testing
        cls.file_path = '/data/IFI8410/sess11/HousePricePrediction.csv'  # Update this path as necessary
        cls.data = pd.read_csv(cls.file_path)
        cls.data = cls.data.drop(columns=['date'])  # Drop non-numeric column

        # Separate features and target
        cls.X = cls.data.drop(columns=['price'])
        cls.y = cls.data['price']

    def test_model_comparison_r2(self):
        # Run the function
        r2_scores = model_comparison_r2(self.X, self.y)

        # Check if each model has an R² score within a reasonable range
        for model_name, r2 in r2_scores.items():
            self.assertIsInstance(r2, float, f"R² score for {model_name} should be a float")
            self.assertTrue(-1 <= r2 <= 1, f"R² score for {model_name} is out of expected range: {r2}")

        print("Test passed: R² values are within expected range for all models.")
