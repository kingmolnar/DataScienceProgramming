from solution_4_17 import color_to_grayscale
import numpy as np

colored_image = np.array([
    [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0], [0, 255, 255]],
    [[128, 128, 128], [255, 128, 0], [0, 255, 128], [128, 0, 255], [64, 64, 0]],
    [[192, 192, 192], [255, 0, 128], [128, 255, 0], [0, 128, 255], [192, 192, 0]],
    [[64, 0, 0], [0, 64, 0], [0, 0, 64], [64, 64, 64], [0, 0, 0]],
    [[255, 255, 255], [128, 128, 0], [0, 128, 128], [128, 0, 128], [0, 0, 128]]
], dtype=np.uint8)

def test_4_17():
    assert color_to_grayscale(colored_image).shape == (5,5), "The shape of the grayscale array is incorrect"
