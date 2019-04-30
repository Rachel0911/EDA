# EDA
This repository will contain the concepts about exploratory data analysis .

# Structure
EDA<br/>
├── preprocess<br/>
│   ├── data<br/>
│   │    └── selected_dataset.csv<br/>
│   ├── scripts<br/>
│   │   ├── step1.py<br/>
│   │   ├── step2.py<br/>
│   │   └── feature_selector<br/>
│   │         ├── __init__.py<br/>      
│   │         └── feature_selector.py<br/>

<br/>
## data folder
selected_dataset.csv is a subset of application_train.csv<br/>
application_train.csv is from <a href="https://www.kaggle.com/c/home-credit-default-risk/data">
Home Credit Default Risk machine learning competition on Kaggle</a>
python code:<br/>
df = pd.read_csv("application_train.csv")<br/>
df = df.iloc[:10000]<br/>
df = df[['NAME_CONTRACT_TYPE','NAME_TYPE_SUITE', 'ORGANIZATION_TYPE','DAYS_EMPLOYED','OWN_CAR_AGE']]<br/>
df.to_csv("selected_dataset.csv")<br/>

## scripts folder
1. Deal with high cardinality categorical variables, i.e. zipcode, city.
2. Deal with missing values(category&number)
3. Transfer data
4. Feature selection<br/>
Part1 and part2 are implemented in step1.py.<br/>
Part3 is implemented in step2.py.<br/>
