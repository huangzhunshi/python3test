import pandas as pd
import numpy as np


df = pd.DataFrame({"id":[1001,1002,1003,1004,1005,1006],
                   "date":pd.date_range('20130102', periods=6),
                   "city":['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
                   "age":[23,44,54,32,34,32],
                   "category":['100-A','100-B','110-A','110-C','210-A','130-F'],
                   "price":[1200,np.nan,2133,5433,np.nan,4432]},
                  columns =['id','date','city','category','age','price'])

df1=pd.DataFrame({"id":[1001,1002,1003,1004,1005,1006,1007,1008],
                  "gender":['male','female','male','female','male','female','male','female'],
                  "pay":['Y','N','Y','Y','N','Y','N','Y',],
                  "m-point":[10,12,20,40,40,40,30,20]})

df_inner=pd.merge(df,df1,how='inner')  # 匹配合并，交集


print(df_inner)

print(df_inner.groupby('city')['price'].agg([len,np.sum, np.mean]))

print(df_inner.sample(n=6, replace=True))

print(df_inner.corr())
#
# print(df_inner.loc[0:1])

#print(df_inner.iloc[[0,2,5],[4,5]])

df_inner


#print(df.sort_values(by="price"))


# print(df['city'].str.lower())
# print(df.fillna(value=-1))
#print(df.isnull())
# print(df.shape)
# print(df.info())
# print(df.dtypes)
#print(df.columns)
#print(df.dtypes)

#a=t.sum001(10,10)

