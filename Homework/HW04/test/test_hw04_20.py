
from solution_4_20 import exam_analyze

import numpy as np

def test_exam_analyze():
    exam_scores = np.array([
    [85, 90, 88],
    [78, 92, 87],
    [90, 92, 94],
    [86, 84, 89],
    [88, 75, 78]
    ])

    average_scores_per_exam, average_scores_per_student = exam_analyze(exam_scores)
    assert np.array_equal(average_scores_per_exam, np.mean(exam_scores, axis=0)), "The average scores per exam is incorrect"
    assert np.array_equal(average_scores_per_student, np.mean(exam_scores, axis=1)), "The average scores per student is incorrect"
