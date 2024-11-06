
from solution_9_1 import preprocess_housing_data
from solution_9_2 import select_and_split_data

import unittest
import pandas as pd
from sklearn.model_selection import train_test_split

class TestSelectAndSplitData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load and preprocess sample data
        file_path = '/data/IFI8410/sess10/HousePricePrediction.csv'
        raw_df = pd.read_csv(file_path)
        cls.df_processed = preprocess_housing_data(raw_df)  # Processed DataFrame

    def test_select_and_split_data(self):
        # Run the feature selection and splitting function
        X_train, X_test, y_train, y_test = select_and_split_data(self.df_processed)

        # Verify shapes and column consistency
        self.assertEqual(X_train.shape[1], X_test.shape[1], "Number of features in X_train and X_test should match.")
        self.assertEqual(y_train.shape[0] + y_test.shape[0], self.df_processed.shape[0], "Total number of samples should match the original dataset.")

        # Check the splitting ratio (80:20)
        train_ratio = X_train.shape[0] / self.df_processed.shape[0]
        test_ratio = X_test.shape[0] / self.df_processed.shape[0]

        self.assertAlmostEqual(train_ratio, 0.8, delta=0.05, msg="Training set ratio should be approximately 0.8.")
        self.assertAlmostEqual(test_ratio, 0.2, delta=0.05, msg="Test set ratio should be approximately 0.2.")

        # Ensure 'price' is excluded from features and only appears in the target
        self.assertNotIn('price', X_train.columns, "Target column 'price' should not be included in features (X_train).")
        self.assertNotIn('price', X_test.columns, "Target column 'price' should not be included in features (X_test).")
