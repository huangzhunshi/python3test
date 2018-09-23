from sklearn import tree
fearture=[[178,1],[155,0],[177,0],[165,0],[169,1],[160,0]]
leble= ['man','woman','woman','woman','man','woman']
clf=tree.DecisionTreeClassifier()
clf.fit(fearture,leble)
a=clf.predict([[171,1],[170,0]])
print(a)