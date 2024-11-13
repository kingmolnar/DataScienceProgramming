
from solution_10_3 import bootstrap_mse  # Import the function from your solution file

import unittest
import pandas as pd

class TestBootstrapMSE(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load the dataset for testing
        cls.file_path = '/data/IFI8410/sess11/HousePricePrediction.csv'
        cls.data = pd.read_csv(cls.file_path)
        cls.data = cls.data.drop(columns=['date'])  # Drop non-numeric column

        # Separate features and target
        cls.X = cls.data.drop(columns=['price'])
        cls.y = cls.data['price']

    def test_bootstrap_mse(self):
        # Run the function with n_bootstrap=100
        mse = bootstrap_mse(self.X, self.y, n_bootstrap=100)

        # Check if the function returns a float or int
        self.assertIsInstance(mse, (float, int), "MSE should be a numeric value")

        # Check if the MSE is within a reasonable range
        self.assertTrue(1e10 <= mse <= 5e10, f"MSE is out of expected range: {mse}")

        print(f"Test passed: Average MSE from Bootstrapping is {mse:.2f}")
