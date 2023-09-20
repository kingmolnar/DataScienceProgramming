import numpy as np

def test_4_20():
    loaded_data = np.load('numpy_data.npy')
    assert loaded_data.shape == (10, 10), "The shape of the array is incorrected"
    assert abs(10 - np.mean(loaded_data)) < 2, "The mean value used for the array is incorrect"
    assert abs(5 - np.std(loaded_data, ddof=1)) < 2, "The standard deviation value used for the array is incorrect"
