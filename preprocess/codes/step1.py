import pandas as pd

def deal_cat_num(df, train_process):
    """Deal with categorical variables and numerical variables with null.
    Especial categorical varibales with null or high cardinality!!!

    Parameters
    ----------
    df : DataFrame
        Original dataset
    train_process : boolean
                   True: train process
                   False: test process

    Returns
    -------
    DataFrame
        df: DataFrame
            After dealing with categorical variables

    """
    # print the number of categorical varibales with high cardinality before reduction
    print("ORGANIZATION_TYPE with high leves. The number is: ", df.ORGANIZATION_TYPE.nunique())

    # set up a threshold number
    # This number is the top frequent levels in a categorical variable
    # num_freq = 20 means I just want to remain the first 20 frequent categories.
    # 58 levels in ORGANIZATION_TYPE column after this function, there are 20 levels left.
    # Since I will use one_hot encoding, it doesn't work well when the levels are too many.
    num_freq = 20
    # Preprocess category fields, store unique values when train. Since in practice, the test dataset is real_time.
    # To guarantee train and test have the same column order after one_hot encoding
    cats = ['NAME_CONTRACT_TYPE','NAME_TYPE_SUITE', 'ORGANIZATION_TYPE']
    df.loc[:, cats] = df[cats].fillna('NONE')
    # store unique category values
    if train_process:
        # define a dataframe for unique categirucal values, and then to_csv
        catVal = pd.DataFrame()
        # reduce categories levels(high cardinality)
        for cat in cats:
            cat_levels = df[cat].astype(str) # some categorical valibales with number but we should see them as string
            unique_levels = pd.Series(cat_levels.value_counts()[:num_freq].index)
            unique_levels.rename(cat, inplace=True)
            # remove 'NONE' in unique_cat
            unique_levels = unique_levels[unique_levels != 'NONE'].reset_index().drop(['index'], axis=1)
            catVal = pd.concat([catVal, unique_levels],axis=1)
        catVal.to_csv('../data/unique_cat.csv')

    # read unique category values for train and test
    catVal_dic = {}
    catVal = pd.read_csv("../data/unique_cat.csv")
    # since some categorical variables have less than num_freq levels. Storing in unique_cat.csv will use "na" to make each 
    # columns have 20 rows. Thus need to remove the "na".
    for cat in cats:
        catVal_dic[cat] = list(catVal[cat][~catVal[cat].isnull()])
    # get dummy variables for category columns
    for cat in cats:
        category_values = catVal_dic[cat]
        df[cat] = pd.Categorical(df[cat], category_values, ordered=False)
    df_temp = pd.get_dummies(df[cats])
    df = pd.concat([df, df_temp], axis=1)
    # delete original cat columns
    df.drop(cats, axis=1, inplace=True)

    # deal with numerical variables with null
    nums = ['DAYS_EMPLOYED', 'OWN_CAR_AGE']
    df[nums] = df[nums].fillna(0.0).astype(float)
    return df

def main():
    df = pd.read_csv("../data/selected_dataset.csv")
    train_process = True
    deal_cat_num(df, train_process)

if __name__ == "__main__":
    main()
