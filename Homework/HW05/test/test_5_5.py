import numpy as np
from solution_5_5 import scale_recipe_advanced

def test_5_5():
    recipe_matrix = np.array([[200, 2, 300], 
                          [50, 1, 50],
                          [10, 0.5, 5]])   
    number_servings = 4
    desired_servings = 10
    scaled_recipe = scale_recipe_advanced(recipe_matrix, number_servings, desired_servings)
    
    expected_result = np.array([[500.0, 5.0, 750.0],
                                [125.0, 2.5, 125.0],
                                [25.0, 1.25, 12.5]])
    
    assert np.allclose(scaled_recipe, expected_result), "The conversion is incorrect"
