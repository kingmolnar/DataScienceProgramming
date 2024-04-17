from solution_10_3 import build_preprocessor
import pandas as pd
def test_10_3():
    df = pd.read_csv('/data/IFI8410/california_housing/taining60perc.csv')
    pp = build_preprocessor(df, target_feature='MedHouseVal')
    Xy = pp.transform(df)
    Xy_mean = Xy.mean(axis=0)
    assert any([ (-0.0001 < mu < 0.0001) for mu in Xy_mean[:-1] ]), "Distribution of descriptive features not around 0"
    assert Xy_mean[-1] > 2.0, "Invalid mean of target feature"
