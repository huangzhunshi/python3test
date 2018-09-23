import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

#这个属性设置是让matplot画图时显示中文的标签
#font = FontProperties(fname=r"C:\Windows\Fonts\msyh.ttc",size=15)

#定义画图函数
# def runplt():
#     plt.figure()
#     plt.title('披萨价格与直径数据')
#     plt.xlabel('直径(英寸)')
#     plt.ylabel('价格(美元)')
#     plt.axis([0,25,0,25])
#     plt.grid(True)
#     return plt

X = [[6], [8], [10], [14], [18]]
y = [[7], [9], [13], [17.5], [18]]

#导入一元线性回归函数:y = α + βx  
from sklearn.linear_model import  LinearRegression
model = LinearRegression()
model.fit(X,y)
print ('预测一张12英寸披萨价格：$%.2f' % model.predict(12))



X2 = [[0],[10],[14],[25]]
y2 = model.predict(X2)  #预测数据
plt.plot(X,y,'k.')
plt.plot(X2,y2,'g-')

#残差预测值
# yr = model.predict(X)
# for idx,x in enumerate(X):
#     plt.plot([x,x], [y[idx], yr[idx]],'r-')

plt.show()