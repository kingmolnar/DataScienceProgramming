
from solution_6_4 import detect_and_filter_athlete_outliers
import unittest
import pandas as pd

class TestHW0604(unittest.TestCase):
    def test_detect_and_filter_athlete_outliers(self):
        data = {
            'Athlete': ['Athlete A', 'Athlete B', 'Athlete C', 'Athlete D', 'Athlete E'],
            'Score': [90, 85, 300, 92, 88],
            'Speed': [22.5, 21.8, 18.3, 25.5, 60.0]
        }
        df6 = pd.DataFrame(data)

        df_no_outliers, df_no_outliers_any = detect_and_filter_athlete_outliers(df6)

        # Expected result without using .any(axis=1)
        expected_data_no_any = {
            'Athlete': ['Athlete A', 'Athlete B', 'Athlete D'],
            'Score': [90, 85, 92],
            'Speed': [22.5, 21.8, 25.5]
        }
        expected_df_no_any = pd.DataFrame(expected_data_no_any)

        # Expected result with using .any(axis=1)
        expected_df_any = expected_df_no_any

        pd.testing.assert_frame_equal(df_no_outliers.reset_index(drop=True), expected_df_no_any)
        pd.testing.assert_frame_equal(df_no_outliers_any.reset_index(drop=True), expected_df_any)
