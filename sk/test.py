import numpy as np

dt=file = open('倚天屠龙记所有人物.txt')
val_list = file.readlines()
lists =[]
for string in val_list:
    #string = string.split('\t',3)
    print(string.split(' ')[0])
    lists.append(string.split(' ')[0])

for a in lists:
    print(a+"xxxx")

if "张无忌1111" in lists:
    print("yes")

dt.close()