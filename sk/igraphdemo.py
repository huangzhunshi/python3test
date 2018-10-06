'''
node大小
https://blog.csdn.net/daiyao666/article/details/78366936
'''
#coding=utf-8
import networkx as nx
import matplotlib.pyplot as plt
#有向图
from matplotlib.font_manager import FontProperties
import pyplotz.pyplotz as pz
import matplotlib as mpl

pltz= pz.PyplotZ()
pltz.enable_chinese()

# G = nx.Graph()   # or DiGraph, MultiGraph, MultiDiGraph, etc
# G.add_nodes_from('黄准哈哈')
# K3 = nx.Graph([(0, 1), (1, 2), (2, 0)])
# G.add_nodes_from(K3)
# sorted(G.nodes(), key=str)
#
#
# G.add_nodes_from([1, 2], size=10)
# G.add_nodes_from([3, 4], weight=0.4)
#
#
# G.add_nodes_from([(1, dict(size=11)), (2, {'color':'blue'})])
# G.nodes[1]['size']
#
# H = nx.Graph()
# H.add_nodes_from(G.nodes(data=True))
# H.nodes[1]['size']
# nx.draw(G,with_labels=True)
# pltz.show()
DG = nx.DiGraph()

#添加一个节点
DG.add_node(u'叶问')
DG.add_node('B')
DG.add_edge(u'李小龙','B')

for font in DG:
    font.set_fontproperties(mpl.font_manager.FontProperties(
        fname='/System/Library/Fonts/STHeiti Light.ttc'))
    font.set_size(8)

#DG.add_nodes_from([(1, dict(size=11)), (2, {'color':'blue'})])

#作图，设置节点名显示,节点大小，节点颜色
nx.draw(DG,with_labels=True,node_size=1000,node_color = 'blue')
pltz.show()




#
# pltz.plot(lable='黄准')
# pltz.title("相关标题")
# pltz.show()



# from igraph import *
#
# count_fans=0 #粉丝数
# count_following=0 #关注人数
# fans_name=[]#粉丝昵称
# following=[]#关注人昵称
# #打开爬取下的昵称文件
# # with open('fans.txt','r') as f:
# #     lines=f.readlines()
# #     for line in lines:
# #         if (line!=None)&(line!='\n'):
# #             fans_name.append(line)
# #             count_fans+=1
# # with open('follow.txt','r') as c:
# #      lines=c.readlines()
# #  for line in lines:
# #       if (line!=None)&(line!='\n'):
# #        following.append(line)
# #    count_following+=1
#
# g = Graph() #创建
# g.add_vertices(3+count_fans+count_following)
# g.add_edges([(0,1),(1,2)])
#
# g.vs[0]["name"]='Ta的粉丝'
# g.vs[1]["name"]='目标用户'
# g.vs[2]["name"]='Ta的关注'
# g.es["trunk"] = [True, True]
# g.vs["main_node"]=[1.5,3,1.5]
#
# for i in range(3,count_fans+3):
#     g.add_edges((0,i))
#     g.es[i-1]["trunk"]=False
# for j in range(count_fans+3,3+count_fans+count_following):
#     g.add_edges((2,j))
#     g.es[j-1]["trunk"]=False
# index=3
# for fans in fans_name:
#     g.vs[index]["name"]=fans
#     g.vs[index]["main_node"]=False
#     index+=1
# for name in following:
#     g.vs[index]["name"]=name
#     g.vs[index]["main_node"]=False
#     index+=1
#
# visual_style = {}
# color_dic={1.5:"#cfe6ff",3:"#7299a7",False:"#cfe6ff"}
# visual_style["vertex_label_size"]=11
# visual_style["vertex_label_dist"]=1
# visual_style["vertex_shape"]="circle"
# visual_style["vertex_size"] = [7+ 10*int(main_node) for main_node in g.vs["main_node"]]
# visual_style["edge_width"] = [1 + 2 * int(trunk) for trunk in g.es["trunk"]]
# visual_style["vertex_color"] =[color_dic[main_node] for main_node in g.vs["main_node"]]
# visual_style["vertex_label"] = g.vs["name"]
# visual_style["bbox"] = (1000, 1000)
# visual_style["margin"] = 150
# #layout = g.layout("grid_fr")
# visual_style["layout"] = layout
# plot(g, **visual_style)
