
from solution_10_2 import loocv_mse

import unittest
import pandas as pd
from sklearn.metrics import mean_squared_error

class TestLOOCVMSE(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load the dataset for testing
        cls.file_path = '/data/IFI8410/sess11/HousePricePrediction.csv'  # Update this path as necessary
        cls.data = pd.read_csv(cls.file_path)
        cls.data = cls.data.drop(columns=['date'])  # Drop non-numeric column

        # Separate features and target
        cls.X = cls.data.drop(columns=['price'])
        cls.y = cls.data['price']

    def test_loocv_mse(self):
        # Run the function
        mse = loocv_mse(self.X, self.y)

        # Check if the function returns a float or int
        self.assertIsInstance(mse, (float, int), "MSE should be a numeric value")

        # Check if the MSE is within a reasonable range (based on previous MSE from k-fold)
        self.assertTrue(1e10 <= mse <= 5e10, f"MSE is out of expected range: {mse}")

        print(f"Test passed: Average MSE from LOOCV is {mse:.2f}")
