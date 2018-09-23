import numpy as np
import pandas as pd
data= pd.read_csv("Folds5x2_pp.csv")
#print(data)
X = data[['AT', 'V', 'AP', 'RH']]
#print(X)
y = data[['PE']]

import sklearn as sk
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test=train_test_split(X,y)

from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(X_train, y_train)
y_pred = linreg.predict(X_test)
from sklearn import metrics
# 用scikit-learn计算MSE
print ("MSE:",metrics.mean_squared_error(y_test, y_pred))
# 用scikit-learn计算RMSE
print ("RMSE:",np.sqrt(metrics.mean_squared_error(y_test, y_pred)))





