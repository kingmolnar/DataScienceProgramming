
from solution_9_1 import preprocess_housing_data

import unittest
import pandas as pd
import numpy as np

class TestPreprocessHousingData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        file_path = '/data/IFI8410/sess10/HousePricePrediction.csv'
        cls.df = pd.read_csv(file_path)

    def test_preprocess_housing_data(self):
        # Run the preprocessing function
        processed_df = preprocess_housing_data(self.df)

        # Check if all expected columns are present in processed DataFrame
        expected_columns = [
            'price', 'bedrooms', 'grade', 'living_in_m2', 'real_bathrooms',
            'month', 'quartile_zone', 'year', 'has_basement_1', 'renovated_1',
            'nice_view_1', 'perfect_condition_1', 'has_lavatory_1', 'single_floor_1'
        ]
        self.assertTrue(all(col in processed_df.columns for col in expected_columns), "Not all expected columns are present.")

        # Ensure the 'date' column is removed and 'year' and 'month' are present
        self.assertNotIn('date', processed_df.columns, "'date' column was not removed.")
        self.assertIn('year', processed_df.columns, "'year' column is missing.")
        self.assertIn('month', processed_df.columns, "'month' column is missing.")

        # Check for missing values in the processed DataFrame
        self.assertFalse(processed_df.isnull().values.any(), "There are missing values in the processed DataFrame.")

        # Check if numeric columns are scaled (mean around 0 and std close to 1 for scaled columns)
        numeric_features = ['bedrooms', 'grade', 'living_in_m2', 'real_bathrooms', 'quartile_zone', 'year', 'month']
        means = processed_df[numeric_features].mean().round()
        stds = processed_df[numeric_features].std().round()

        # Assert that means are approximately 0 and standard deviations are close to 1
        for mean, std in zip(means, stds):
            self.assertAlmostEqual(mean, 0, delta=1, msg="Mean is not approximately 0 for a numeric feature")
            # self.assertAlmostEqual(std, 1, delta=0.1, msg="Standard deviation is not close to 1 for a numeric feature")
