import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dates=pd.date_range('20180611',periods=10)
print(dates)


if not True:
    print('ok')
else:
    print('no')

"""wo yes """
str1="""this is world bbb""" +\
     " dsfdsf"

#print(str);print("one rows ")

#print(str[2:7])

list_1=['huangzhun001','huangzhun002','huangzhun003']
list_2=['ok1','ok2','ok3']

# print(list_1[0:1])
# print(list_1+list_2)
list_1.append("huangzhun004")
list_1.append("huangzhun005")
# print(list_1)
tuple_1=('a01','a02','a03')
tuple_2=('b01','b02')
# print(tuple_1[0:2])
# print(tuple_2+tuple_1)

mydict={"huang":"zhun","li":"hao"};
# print(mydict.get("li"))
# print(mydict.keys())
#
# print("huangzhun001" in list_1 or "huangzhun0021" in list_1)

# a=20
# b=20
#
# print(a is not b)

class Emp:
    empCount=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Emp.empCount=Emp.empCount+1

    def showEmp(self):
        print(self)
        print(self.name)
        print(self.age)


emp=Emp("yihui",12)
emp.showEmp()
emp2=Emp("huangz",16)

print(Emp.__name__)
print(Emp.__dict__)
print(Emp.__doc__)
# a=30
# b=40
# if a==b:
#     print('a==b')
# elif a>10:
#     print("a>10")
# elif b==30:
#     print("b>10")
# else:
#     print("else")
# count=1
# while count<10:
#     print(count)
#     count=count+1
# else:
#     print("end:"+str(count))

# for a in list_1:
#     print(a)
# else:
#     print("end")
#
# for index in range(len(list_1)):
#     print(index)
#     print(list_1[index])



# #df=pd.DataFrame(np.random.rand(1,3),index=dates,columns=(list('ABCD')))
# df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
# print(df);
#s=pd.Series([1,2,3])
#print(s)

# s=pd.SparseArray([1,2,3]);
# for i in s:
#     print(i+100)
#     print(i)
#
#
#
# print('end')



