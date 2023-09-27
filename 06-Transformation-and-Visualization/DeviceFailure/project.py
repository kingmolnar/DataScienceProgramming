import sys, os

jp = os.path.join
import datetime
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import findspark

findspark.init()
from pyspark.sql import SparkSession, Window
import pyspark.sql.functions as F
import pyspark.sql.functions as T
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import StandardScaler

S = F.col


def scatter_plot_matrix(df, features=[], label_col=None):
    '''
    The function creates a scatter-plot matrix from the provided dataframe.
    The upper right triangle shows scatter plots, the diagonal contains histograms,
    and the lover left triangle shows the Spearman correlation between two features.
    :param df: Pandas dataframe
    :param features: lsit of columns with features
    :param label_col: column with label
    :return: Matplotlib figure
    '''
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from scipy.stats import spearmanr, pearsonr

    if len(features) == 0:
        features = df.describe().columns
    if label_col:
        features = sorted(list(set(features) - {label_col}))
        pos = df[df[label_col] == 1]
        neg = df[df[label_col] == 0]
    else:
        pos = None
        neg = df

    # pdf = pd.read_csv('./device_failure_fixed.csv', encoding='utf-8')
    # pos = pdf[pdf.failure==1]
    # neg = pdf[pdf.failure==0]
    fig = plt.figure(figsize=(20, 20))
    Nfeat = len(features)
    for k in range(Nfeat):
        for j in range(Nfeat):
            plt.subplot(Nfeat, Nfeat, k * Nfeat + j + 1)
            if j > k:
                x = neg[features[k]]
                y = neg[features[j]]
                plt.plot(x, y, '.', alpha=0.1)
                if not pos is None:
                    x = pos[features[k]]
                    y = pos[features[j]]
                plt.plot(x, y, '.', c='red', alpha=1)
            elif j < k:
                plt.xlim(0, 4)
                plt.ylim(0, 4)
                corr, p = spearmanr(df[features[k]].values, df[features[j]].values)
                # pearsonr(df['attribute%d'%k].values, df['attribute%d'%j].values)
                plt.text(2, 2, "%.2f" % (corr))
            else:
                plt.hist(df[features[k]], bins=20, color='green', log=True)
            if j == 0:
                plt.ylabel(features[k])
            if k == Nfeat - 1:
                plt.xlabel(features[j])
    return fig


#  ____                   _
# / ___| _ __   __ _ _ __| | __
# \___ \| '_ \ / _` | '__| |/ /
#  ___) | |_) | (_| | |  |   <
# |____/| .__/ \__,_|_|  |_|\_\
#       |_|
# Spark functions

def withlagtable(df, nlag, date_col='date', key_col='device', label_col='failure'):
    '''
    Add features for previous time steps to each record
    :param df: Spark dataframe
    :param nlag: number of previous time steps to include
    :param date_col: name of column with date
    :param key_col: name of column to group by
    :param label_col: name of column with label
    :return: Spark dataframe with addtional columns to include features from previous time steps
    '''
    import pyspark.sql.functions as F
    import pyspark.sql.functions as T
    from pyspark.sql import Window
    S = F.col
    head_cols = [date_col, key_col, label_col]
    features = np.array(df.columns)[
        np.array([(str(s.dataType) == 'DoubleType') & (not s.name in head_cols) for s in df.schema])]

    df2 = df  ### .select(*head_cols)
    for k in range(len(features)):
        df2 = df2.withColumnRenamed(features[k], 'a%d_t0' % (k))
    for k in range(len(features)):
        for j in range(1, nlag + 1):
            df2 = df2.withColumn('a%d_t%d' % (k, j),
                                 F.lag('a%d_t0' % (k), count=j).over(
                                     Window.partitionBy('device').orderBy('date')
                                 ))
    return df2


def extendtimeline(df, key_col='device', date_col='date',
                   start_time=datetime.date(2015, 1, 1), Nday=305):
    '''
    Add additional records for missing days, except for key_col and date_col all columns have NULL values
    :param df: Spark DataFrame
    :param key_col:
    :param date_col:
    :param start_time: start date
    :param Nday: Number of days covered
    :return: Spark Dataframe with addtional rows
    '''
    import datetime
    import pyspark.sql.functions as F
    import pyspark.sql.functions as T
    S = F.col

    dd = df.sql_ctx.createDataFrame(
        zip([start_time + datetime.timedelta(days=k) for k in range(Nday + 1)])
    ) \
        .withColumnRenamed('_1', date_col)
    return df.select(key_col).distinct().crossJoin(dd) \
        .join(df, on=[key_col, date_col], how='left')


def train_valid_test_split(df, label_col='failure', feature_col='features', sampler=None,
                           test_split=0.4, validation_split=0.2, down_sample_factor=1.0,
                           random_seed=42):
    '''

    :param df: Spark DataFrame with fetature vector
    :param label_col: column name of label
    :param feature_col: column name of feature vector
    :param sampler: type of sampler: None, 'down', 'smote'
    :param test_split: ratio of samples witheld for final testing
    :param validation_split: ratio of training samples for training validation
    :param down_sample_factor: factor of negative sample size over positive sample size, only for down-sampling
    :param random_seed:
    :return: X_res_train, X_res_valid, X_test, y_res_train, y_res_valid, y_test Numpy matrices and vectors
    '''
    from sklearn.model_selection import train_test_split
    from imblearn.over_sampling import SMOTE

    df_pos = df.where("failure=1")
    df_neg = df.where("failure=0")

    train_pos_df, test_pos_df = df_pos.randomSplit([1.0 - test_split, test_split], seed=random_seed)
    train_neg_df, test_neg_df = df_neg.randomSplit([1.0 - test_split, test_split], seed=random_seed)

    X_test, y_test = feature_vect_to_Xy(test_pos_df.union(test_neg_df), label_col=label_col, feature_col=feature_col)

    if sampler and (sampler.lower()=='smote'):
        # use SMOTE up-sampling
        X_train, y_train = feature_vect_to_Xy(train_pos_df.union(train_neg_df), label_col=label_col, feature_col=feature_col)
        assert X_train.shape[0] == len(y_train), 'Mismatch in number or training records and labels'
        #print("Number of training samples: %d, proportion of positive labels: %.4f" % (len(y_train), np.mean(y_train)))
        sm = SMOTE(random_state=random_seed)
        X_res, y_res = sm.fit_resample(X_train, y_train)
        assert X_res.shape[0] == len(y_res), 'Mismatch in number or resampled records and labels'
        X_res_train, X_res_valid, y_res_train, y_res_valid = \
            train_test_split(X_res, y_res, test_size=validation_split, random_state=random_seed)

    elif sampler and (sampler.lower()=='down'):
        # use down-sampling
        N_pos = train_pos_df.count()
        N_neg = train_neg_df.count()
        fract = down_sample_factor*float(N_pos)/float(N_neg)
        if fract<1.0:
            train_neg_subdf = train_neg_df.sample(fraction=fract, seed=random_seed)
        else:
            train_neg_subdf = train_neg_df
        X_res, y_res = feature_vect_to_Xy(train_pos_df.union(train_neg_subdf), label_col=label_col, feature_col=feature_col)
        X_res_train, X_res_valid, y_res_train, y_res_valid = \
            train_test_split(X_res, y_res, test_size=validation_split, random_state=random_seed)

    else:
        # no sampling train and validation will be the same
        X_res_train, y_res_train = feature_vect_to_Xy(train_pos_df.union(train_neg_df), label_col=label_col, feature_col=feature_col)
        X_res_valid = X_res_train.copy()
        y_res_valid = y_res_train.copy()

    return X_res_train, X_res_valid, X_test, y_res_train, y_res_valid, y_test



def feature_vect_to_Xy(df, feature_col='features', label_col='failure'):
    '''
    Convert Spark features column to Numpy arrays X and y
    :param df: Spark DataFrame
    :param feature_col: single column with Vector (dense or sparse)
    :param label_col:  single column with scalar value
    :return: X, y numpy arrays
    '''
    # http://blog.madhukaraphatak.com/spark-vector-to-numpy/
    X = np.apply_along_axis(lambda x : x[0], 1, df.select(feature_col).toPandas())
    y = np.apply_along_axis(lambda x : x[0], 1, df.select(label_col).collect())
    return X, y

def eval_prediction(y_act, y_hat):
    '''
    Calculates evaluation metrics
    :param y_act: actual label (Numpy array)
    :param y_hat: predicted label (Numpy array)
    :return: precision, recall, fscore, TP, FN, FP, TN
    '''
    import numpy as np
    TP = np.sum((y_act == y_hat) & (y_act == 1))
    TN = np.sum((y_act == y_hat) & (y_act == 0))
    FN = np.sum((y_act != y_hat) & (y_act == 1))
    FP = np.sum((y_act != y_hat) & (y_act == 0))
    precision =  1.0*TP/(TP+FP) if (TP+FP)>0 else np.nan
    recall = 1.0*TP/(TP+FN) if (TP+FN)>0 else np.nan
    fscore =  2.0*TP/(2.0*TP+FP+FN) if (TP+FP+FN)>0 else np.nan
    return precision, recall, fscore, TP, FN, FP, TN


def print_model_evaluaton(model, X_valid, X_test, y_valid, y_test):
    y_hat = model.predict(X_valid)
    precision, recall, fscore, TP, FN, FP, TN = eval_prediction(y_valid, y_hat)
    print("\tresampled: precision=%.2f, recall=%.2f, F-score=%.2f" % (precision, recall, fscore))
    print("\tresampled: TP={:,}, FN={:,}, FP={:,}, TN={:,}".format(TP, FN, FP, TN))
    y_hat = model.predict(X_test)
    precision, recall, fscore, TP, FN, FP, TN = eval_prediction(y_test, y_hat)
    print("\ttest:      precision=%.2f, recall=%.2f, F-score=%.2f" % (precision, recall, fscore))
    print("\ttest:      TP={:,}, FN={:,}, FP={:,}, TN={:,}".format(TP, FN, FP, TN))


def load_data(spark, fname='device_failure_fixed.csv'):
    import datetime
    df_pd = pd.read_csv(fname)
    df_pd['date'] = df_pd['date'].map(lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'))
    for k in range(1, 10):
        df_pd['attribute%d' % k] = df_pd['attribute%d' % k].map(float)
    assert isinstance(df_pd, pd.DataFrame)
    df = spark.createDataFrame(df_pd)
    return df


def build_feature_table(df, attribute_cols=[], lag=0,
                        date_col='date', key_col='device', label_col='failure', feature_col='features',
                        with_scaler=True
                        ):
    '''
    Build feature table with feature vector form select attributes.
    IF lag>0
    :param df: Spark dataframe
    :param attribute_cols: list of columns that should be included as features
    :param lag: number of previous timesteps to include in the table
    :param date_col: name of column holding the date
    :param key_col: name of column to group by
    :param label_col: name of column with label
    :return: Spark dataframe with feature column
    '''
    if len(attribute_cols)==0:
        attcols = ['attribute%d' % k for k in [1, 2, 3, 4, 5, 6, 7, 9]]
    else:
        attcols = attribute_cols

    df_sel = df.select(date_col, key_col, label_col, *attcols)
    if lag==0:

        assembler = VectorAssembler(
            inputCols=attcols,
            outputCol='_features_raw'
        )
        df2 = assembler.transform(df_sel)
    else:
        df_wl = withlagtable(df_sel, lag, date_col=date_col,
                             key_col=key_col, label_col=label_col) \
            .dropna().cache()

        assembler = VectorAssembler(
            inputCols=list(filter(lambda c: c[0]=='a', df_wl.columns)),
            outputCol='_features_raw',
            handleInvalid = "keep",
        )
        df2 = assembler.transform(df_wl)

    if with_scaler:
        scaler = StandardScaler(inputCol="_features_raw",
                                outputCol=feature_col,
                                withStd=True, withMean=False, # "keep" or "skip"
                                )
        scalerModel = scaler.fit(df2)
        df3 = scalerModel.transform(df2)
        return df3.drop("_features_raw")
    else:
        return df2.withColumnRenamed('_features_raw', feature_col)

