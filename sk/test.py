import numpy as np

from sklearn import preprocessing

import numpy as np

X = np.array([[ 1., -1.,  2.],[ 2.,  0.,  0.],[ 0.,  1., -1.]])

X_scaled = preprocessing.scale(X)

#print(X)
#print(X_scaled)


b=np.array([1,2,3,4,5,7])
print(b)
print(preprocessing.scale(b))