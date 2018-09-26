import pandas as pd
from matplotlib.font_manager import FontProperties
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

boston = datasets.load_boston()
bos=pd.DataFrame(boston.data)

bos.columns= boston.feature_names
bos['PRICE'] = boston.target
#Y=boston.target
X=bos.drop('PRICE',axis=1)

#print(bos['PRICE'])
train,test=train_test_split(bos,test_size=0.3, random_state=0)
train_X=train.drop('PRICE',axis=1)
train_Y=train['PRICE']

test_X=test.drop('PRICE',axis=1)
test_Y=test['PRICE']

lm = LinearRegression()
lm.fit(train_X, train_Y)

predict=lm.predict(test_X)

print(predict)

print(test_Y)

confusion_matrix(predict,test_Y)
# acc= accuracy_score(predict,test_Y)
# print(acc)

#print(train)
#print(test)
#print(bos)