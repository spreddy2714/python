from sklearn.externals import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.externals import joblib

dataset_url = 'http://mlr.cs.umass.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data = pd.read_csv(dataset_url, sep=";")

# print(data.head())
# print(data.shape)
# print(data.describe())

y = data.quality
X = data.drop('quality', axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.99, random_state=123, stratify=y)

clf2 = joblib.load("scikit_rf_regressor.pkl")
pred = clf2.predict(X_test)
print(r2_score(y_test, pred))
print(mean_squared_error(y_test, pred))

