#!/usr/bin/python
#-*- coding: utf-8 -*-
import pymysql
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


def getChineseFont():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

# 测试库
# config = {
#     'host':'rm-2ze886b0r63l4127w.mysql.rds.aliyuncs.com',
#     'port':3306,#MySQL默认端口
#     'user':'oss',#mysql默认用户名
#     'password':'JdmPi2URFCWyIaTh',
#     'db':'oss',#数据库
#     'charset':'utf8',
# }


config = {
    'host':'10.28.61.149',
    'port':3306,#MySQL默认端口
    'user':'yihui',#mysql默认用户名
    'password':'GMYAvsgzE9fRRC1r',
    'db':'oss',#数据库
    'charset':'utf8',
}

db=pymysql.connect(**config)
sql="""
  select e.id, nick_name,e.sex,education_first from  hr_resume as r left JOIN  agent_employee as e
  on e.id=r.employee_id
  where  real_status=1 and status=0 and agent_id=1
  order by e.id desc
"""


user=pd.read_sql(sql,con=db)

db.close()

user_clean=user.replace('','其他').replace('专科','大专').replace('函授大专','大专').replace('职高','高中').replace('无','其他').replace('市场营销','本科').replace('广告营销','本科').replace('建筑工程','本科').replace('建筑设计','本科').replace('硕士','研究生').replace('/','其他')
#print(user)


df_a=user_clean.groupby("education_first").count()

df_a["hikey"]= df_a.index+"["+df_a.id.map(str)+"人]"

# print(df_a)
# print(df_a.index.values)
# print(df_a.id.values)
# print(df_a.hikey.values)

df_sex= user.groupby("sex").count()
print(df_sex)


# ----------------------------------饼状图-------------------------------------------

from matplotlib.font_manager import FontManager, FontProperties
import matplotlib as mpl
import matplotlib.pyplot as plt


# 使用Mac系统自带的中问字体
def getChineseFont():
    return FontProperties(fname='/System/Library/Fonts/STHeiti Medium.ttc')

#设置图片大小
# plt.figure(figsize=(9,6))

#label = df_a.index.values
label=df_a.hikey.values
size = df_a.id.values # 各类别占比

# 绘制饼状图
pie = plt.pie(size,   labels=label, shadow=True, autopct='%1.1f%%')
# 饼状图呈正圆
for font in pie[1]:
    font.set_fontproperties(mpl.font_manager.FontProperties(
        fname='/System/Library/Fonts/STHeiti Light.ttc'))
    font.set_size(8)
for digit in pie[2]:
    digit.set_size(8)

plt.axis('equal')
plt.title(u'小电学历分布', fontproperties=getChineseFont(), fontsize=12)

plt.legend(prop=getChineseFont(), loc=0, bbox_to_anchor=(0.82, 1))  # 图例
#设置legend的字体大小
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize=6)

# 显示图
plt.show()





