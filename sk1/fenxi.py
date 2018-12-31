from sklearn import preprocessing
import pandas as pda
import matplotlib.pyplot as plt
import numpy as np

def test():
   df=pda.read_csv("../data/HR.csv")
   #print(df)
   #print( df.describe())
   df.dropna(axis=0, how='any')
   #print(df.describe())
   #print(df["last_evaluation"].drop(index=15000))

   df.drop(df.index[[15000,15001]],inplace=True)
   #df["department"]
   #print(df.describe())
   #print(df)
   from sklearn.preprocessing import LabelEncoder,OneHotEncoder
   lb_encoder=LabelEncoder()

   df_1=df.groupby("department").count().reset_index()["department"]

   from sklearn.preprocessing import MinMaxScaler
   from sklearn.preprocessing import StandardScaler
   df["number_project"]
   x=MinMaxScaler().fit_transform(df["number_project"].reshape(-1,1))
   print(x)

'''
数据离散化
'''
def test1():
    list=[1,2,3,4,5,100,32,434,31]
    #等深分箱
    a=pda.qcut(list,q=3,labels=["1","2","3"])
    print(a)
    #等宽分箱
    b=pda.cut(list,bins=3,labels=["1","2","3"])
    print(b)
'''
归一化和标准化
'''
def test2():
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.preprocessing import StandardScaler

    #print(MinMaxScaler().fit_transform(np.array([1,4,10,15,21]).reshape(-1,1)))


    '''归一化'''
    a1=MinMaxScaler().fit_transform(np.array([1,4,10,15,21]).reshape(-1,1))
    print(a1)

    '''标准化'''
    b1=StandardScaler().fit_transform(np.array([1,1,1,1,0,0,0,0]).reshape(-1,1))
    print(b1)

    b2=StandardScaler().fit_transform(np.array([1,0,0,0,0,0,0,0]).reshape(-1,1))
    print(b2)

'''
数值化
'''
def test3():

    '''标签化'''
    from sklearn.preprocessing import LabelEncoder,OneHotEncoder
    '''按照字母的顺序进行数值化 d-0 u-1'''
    a1=LabelEncoder().fit_transform(np.array(["down","up","up","down"]))
    print(a1)


    '''独热'''
    color=np.array(["red","green","blue","yellow","black"])
    lb_encoder=LabelEncoder()
    lb_encoder_f=lb_encoder.fit_transform(color)
    oht_encoder=OneHotEncoder().fit(lb_encoder_f.reshape(-1, 1))

    a2= oht_encoder.fit_transform(lb_encoder.fit_transform(np.array(["red","green","blue","yellow","black"])).reshape(-1, 1)).toarray()
    print(a2)



if __name__ == '__main__':
    test3()