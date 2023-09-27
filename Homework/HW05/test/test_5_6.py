import os 

def test_5_6():
     assert os.path.isfile('movie_dataset.csv'), "Missing output file."
