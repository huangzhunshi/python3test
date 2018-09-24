'''

https://blog.csdn.net/qq_33792843/article/details/78477632
'''
import pandas as pd
from matplotlib.font_manager import FontProperties

from sklearn import datasets
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt
"""
mac中文编码
"""
def getChineseFont():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

boston = datasets.load_boston()
# #print(boston.DESCR)
#
# n_samples = len(boston.target)
#
#
# print(boston.target)
#print(boston.keys)
bos=pd.DataFrame(boston.data)
#print(bos)
bos.columns= boston.feature_names
bos['PRICE'] = boston.target


X=bos.drop('PRICE',axis=1)
lm = LinearRegression()

lm.fit(X, bos.PRICE)


print('线性回归算法w值：', lm.coef_)

print('线性回归算法b值: ', lm.intercept_)

plt.scatter(bos.RM, bos.PRICE)

plt.xlabel(u'住宅平均房间数', fontproperties=getChineseFont())

plt.ylabel(u'房屋价格', fontproperties=getChineseFont())

plt.title(u'RM与PRICE的关系', fontproperties=getChineseFont())

plt.show()
