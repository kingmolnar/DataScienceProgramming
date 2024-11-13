
from solution_10_4 import model_comparison_rmse

import unittest
import pandas as pd

class TestModelComparisonRMSE(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load the dataset for testing
        cls.file_path = '/data/IFI8410/sess11/HousePricePrediction.csv'
        cls.data = pd.read_csv(cls.file_path)
        cls.data = cls.data.drop(columns=['date'])  # Drop non-numeric column

        # Separate features and target
        cls.X = cls.data.drop(columns=['price'])
        cls.y = cls.data['price']

    def test_model_comparison_rmse(self):
        # Run the function
        rmse_scores = model_comparison_rmse(self.X, self.y)

        # Check if each model has an RMSE value within a reasonable range
        for model_name, rmse in rmse_scores.items():
            self.assertIsInstance(rmse, (float, int), f"RMSE for {model_name} should be a numeric value")
            self.assertTrue(1e4 <= rmse <= 2e5, f"RMSE for {model_name} is out of expected range: {rmse}")

        print("Test passed: RMSE values are within expected range for all models.")
