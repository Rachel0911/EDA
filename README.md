# EDA
This repository will contain the concepts about exploratory data analysis.

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
## codes folder
Feature selection<br/>
Feature selection is modified from <a href="https://github.com/WillKoehrsen/feature-selector">WillKoehrsen's feature-selector</a>  repository. I forked the whole version.<br/>

# Thank you WillKoehrsen for offering a perfect repo about feature selection!
