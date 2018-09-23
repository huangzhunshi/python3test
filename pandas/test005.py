import sklearn as sk
import numpy as np
import matplotlib.pyplot as plt

def createDataSet():
    group=np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    lables=['A','A','B','B']
    return  group,lables

group,lebles=createDataSet()
print(group)
print(lebles)


def abc():
    '''abc注释'''
    print(abc.__doc__)

abc()