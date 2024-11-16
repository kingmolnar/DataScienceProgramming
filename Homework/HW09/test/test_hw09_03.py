
from solution_9_3 import train_and_evaluate_model  # Import the function from your solution file

import unittest
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

class TestTrainAndEvaluateModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Generate synthetic data for testing
        X, y = make_regression(n_samples=100, n_features=10, noise=0.1, random_state=1)
        cls.X_train, cls.X_test, cls.y_train, cls.y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    def test_train_and_evaluate_model(self):
        # Run the training and evaluation function
        mae, mse, rmse = train_and_evaluate_model(self.X_train, self.X_test, self.y_train, self.y_test)

        # Check if the metrics are within a reasonable range
        # (for synthetic data, specific bounds are set for demonstration; adjust if using real data)
        self.assertGreaterEqual(mae, 0, "MAE should be non-negative.")
        self.assertGreaterEqual(mse, 0, "MSE should be non-negative.")
        self.assertGreaterEqual(rmse, 0, "RMSE should be non-negative.")

        # Ensure that RMSE is consistent with MSE
        self.assertAlmostEqual(rmse, mse**0.5, places=5, msg="RMSE should be the square root of MSE.")
