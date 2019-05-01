# EDA
This repository will contain the concepts about exploratory data analysis.
# Structure
```
EDA
├── preprocess
│   ├── data
│   │    └── selected_dataset.csv
│   ├── scripts
│   │   ├── step1.py
│   │   ├── step2.py
│   │   └── feature_selector
│   │         ├── __init__.py   
│   │         └── feature_selector.py
```

## data folder
selected_dataset.csv is a subset of application_train.csv. I just selected the first 10000 rows and 5 columns.<br/>
application_train.csv is from <a href="https://www.kaggle.com/c/home-credit-default-risk/data">
Home Credit Default Risk machine learning competition</a> on Kaggle<br/>
<br/>
python code:<br/>
df = pd.read_csv("application_train.csv")<br/>
df = df.iloc[:10000]<br/>
df = df[['NAME_CONTRACT_TYPE','NAME_TYPE_SUITE', 'ORGANIZATION_TYPE','DAYS_EMPLOYED','OWN_CAR_AGE']]<br/>
df.to_csv("selected_dataset.csv")<br/>
## scripts folder
1. Deal with high cardinality categorical variables, i.e. zipcode, city.
2. Deal with missing values(category&number)
3. Transform data
4. Feature selection<br/>
Part1 and part2 are implemented in step1.py.<br/>
Part3 is implemented in step2.py.<br/>
Part4 is modified from <a href="https://github.com/WillKoehrsen/feature-selector">WillKoehrsen's feature-selector</a>  repository. I forked the whole version.<br/>
Remove one-hot parameter in WillKoehrsen's feature-selector, since I do one-hot encoding in the step1.py<br/>
# Thank you WillKoehrsen for offering a perfect repo about feature selection!
