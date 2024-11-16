
from solution_10_1 import k_fold_cross_val_mse

import unittest
import pandas as pd
from sklearn.metrics import mean_squared_error

class TestKFoldCrossValMSE(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load the dataset for testing
        cls.file_path = '/data/IFI8410/sess11/HousePricePrediction.csv'  # Update this path as necessary
        cls.data = pd.read_csv(cls.file_path)
        cls.data = cls.data.drop(columns=['date'])  # Drop non-numeric column

        # Separate features and target
        cls.X = cls.data.drop(columns=['price'])
        cls.y = cls.data['price']

    def test_k_fold_cross_val_mse(self):
        # Run the function with k=5
        mse = k_fold_cross_val_mse(self.X, self.y, k=5)

        # Check if the function returns a float or int
        self.assertIsInstance(mse, (float, int), "MSE should be a numeric value")

        # Check if the MSE is within a reasonable range (based on prior results)
        self.assertTrue(1e9 <= mse <= 2e10, f"MSE is out of expected range: {mse}")

        print(f"Test passed: Average MSE from 5-fold cross-validation is {mse:.2f}")
