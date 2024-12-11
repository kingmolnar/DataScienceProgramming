
from solution_4 import select_and_split_data, preprocess_train_and_evaluate_model

import unittest
import pandas as pd
import numpy as np

class TestPreprocessData(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # Load the dataset
        import pandas as pd
        file_path = '/data/IFI8410/finalexam/predict_home_value.csv'
        self.df = pd.read_csv(file_path)
        self.numeric_columns = ['LOTAREA', 'OVERALLCOND', 'YEARBUILT', 'FULLBATH', 'HALFBATH',
           'BEDROOMABVGR', 'KITCHENABVGR', 'TOTRMSABVGRD', 'FIREPLACES',
           'GARAGECARS', 'POOLAREA', 'MOSOLD', 'YRSOLD']
        self.target_column = 'SALEPRICE'
        
    def test_preprocess_train_and_evaluate_model(self):

        # Run the feature selection and splitting function
        X_train, X_test, y_train, y_test = select_and_split_data(
            self.df, self.numeric_columns, self.target_column
        )

        # Verify shapes and column consistency
        self.assertEqual(X_train.shape[1], X_test.shape[1], "Number of features in X_train and X_test should match.")
        self.assertEqual(y_train.shape[0] + y_test.shape[0], self.df.shape[0], "Total number of samples should match the original dataset.")

        # Check the splitting ratio (80:20)
        train_ratio = X_train.shape[0] / self.df.shape[0]
        test_ratio = X_test.shape[0] / self.df.shape[0]

        self.assertAlmostEqual(train_ratio, 0.8, delta=0.05, msg="Training set ratio should be approximately 0.8.")
        self.assertAlmostEqual(test_ratio, 0.2, delta=0.05, msg="Test set ratio should be approximately 0.2.")

        # Ensure 'price' is excluded from features and only appears in the target
        self.assertNotIn('price', X_train.columns, "Target column 'price' should not be included in features (X_train).")
        self.assertNotIn('price', X_test.columns, "Target column 'price' should not be included in features (X_test).")

        mae, mse, rmse = preprocess_train_and_evaluate_model(X_train, X_test, y_train, y_test, self.numeric_columns)

        # Check if the metrics are within a reasonable range
        # (for synthetic data, specific bounds are set for demonstration; adjust if using real data)
        self.assertGreaterEqual(mae, 0, "MAE should be non-negative.")
        self.assertGreaterEqual(mse, 0, "MSE should be non-negative.")
        self.assertGreaterEqual(rmse, 0, "RMSE should be non-negative.")
