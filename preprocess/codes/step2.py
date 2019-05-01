import warnings
warnings.filterwarnings("ignore")

import pandas as pd

from sklearn.preprocessing import MinMaxScaler
from sklearn.externals import joblib


def tranform_data(df, train_process):
    """Scale df and make the range of each column is 0-1.

    Parameters
    ----------
    df : DataFrame
        After dealing with categorical and numerical dataset
    train_process : boolean
                   True: train process
                   False: test process

    Returns
    -------
    DataFrame
        df: DataFrame
            After transforming data

    """
    # notic: Don't scale target column.
    if train_process:
        df_tranform = MinMaxScaler(feature_range=(0, 1)).fit(df)
        joblib.dump(df_tranform, "../data/tranform_data.save")
    else:
        df_tranform = joblib.load("../data/tranform_data.save")

    df_tranform = df_tranform.transform(df)
    df_tranform = pd.DataFrame(df_tranform)
    df_tranform.columns = df.columns
    return df_tranform

def main():
    df = pd.read_csv("../data/deal_cat_num.csv")
    train_process = True
    df = tranform_data(df, train_process)
    df.to_csv("../data/tranform_data.csv")
if __name__ == "__main__":
    main()
