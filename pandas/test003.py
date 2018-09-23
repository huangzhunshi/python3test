import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(12, 8))
ax = Axes3D(fig)

# 生成X，Y
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X,Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)

# height value
Z = np.sin(R)

# 绘图
# rstride（row）和cstride(column)表示的是行列的跨度
ax.plot_surface(X, Y, Z,
                rstride=1,  # 行的跨度
                cstride=1,  # 列的跨度
                cmap=plt.get_cmap('rainbow')  # 颜色映射样式设置
                )

# offset 表示距离zdir的轴距离
ax.contourf(X, Y, Z, zdir='z', offest=-2, cmap='rainbow')
ax.set_zlim(-2, 2)

plt.show()
# x =  [5,8,10]
# y =  [12,16,6]
# x2 =  [6,9,11]
# y2 =  [6,15,7]
# plt.bar(x, y, align =  'center')
# plt.bar(x2, y2, color =  'g', align =  'center')
# plt.title('Bar graph')
# plt.ylabel('Y axis')
# plt.xlabel('X axis')
# plt.show()
# x=np.arange(0,3*np.pi,0.1)
# y=np.sin(x)
# print(x)
# print(y)
# plt.subplot(3,1,1)
# plt.plot(x,y,'x')
#
# plt.subplot(3,1,2)
# plt.plot(x,y,'o')
#
# plt.subplot(3,1,3)
# plt.plot(x,y,'o')
#
# plt.show()


# plt.plot(x,y)
# plt.show()
# x=np.arange(1,10,2)
# print(x)
#
# y=x*2+5
# print(y)
#
# plt.title("demo")
# plt.xlabel("my x")
# plt.ylabel("my y")
# plt.plot(x,y,'go')
# plt.show()

# x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
# print('我们的数组是：')
# print(x)
# print('\n')
# # 切片
# z = x[1:4,1:3]
# print('切片之后，我们的数组变为：')
# print(z)
# print('\n')
# # 对列使用高级索引
# y = x[1:4,[1,2]]
# print('对列使用高级索引来切片：')
# print(y)

# x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
# rows = np.array([[0,0],[3,3]])
# cols = np.array([[0,2],[0,2]])
#
# #y = x[rows,cols]
# print(x[rows,cols])
# x = np.array([[1,  2],  [3,  4],  [5,  6]])
# y = x[[0,1,2],  [0,1,0]]
# print(y)
# print(x[x>1])
# x=np.arange(10)
# print(x[2:7])

#x = np.empty([3,2], dtype =  int)

#numpy.zeros(shape, dtype = float, order = 'C')
#print(x)
# x = np.linspace(-1, 1, 50)
# print(x)
# y=x+1
# plt.plot(x,y)
# plt.show()

# a=np.array([[1,2,3],[4,5,6]])
# print(a.flags)
# print(a.reshape(1,6))


# b=[5,6,7]
# print(a[0])