import pymysql
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import time
from matplotlib.font_manager import FontProperties


"""
mac中文编码
"""
def getChineseFont():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

"""
获取用户列表
"""
def getEmpList():
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
      select e.id, nick_name,e.sex,education_first,r.birth_date,e.level_id ,recruite_channel from  hr_resume as r left JOIN  agent_employee as e
      on e.id=r.employee_id
      where  real_status=1 and status=0 and agent_id=1
      order by e.id desc
    """
    user=pd.read_sql(sql,con=db)
    db.close()
    return user

"""
清洗和统计用户的学历数据
"""
def getCleanCountEduDf(df):
    user_clean=user.replace('','其他').replace('专科','大专').replace('函授大专','大专').\
        replace('职高','高中').replace('无','其他').replace('市场营销','本科').\
        replace('广告营销','本科').replace('建筑工程','本科').\
        replace('建筑设计','本科').replace('硕士','研究生').replace('/','其他').\
        groupby("education_first").count().reset_index()

    user_clean["lable"]= user_clean.education_first+"["+user_clean.id.map(str)+"人]"
    return user_clean


"""
将性别标记位转换成文字
"""
def getSex(sex):
    if sex==1:
        return '男'
    else:
        return '女'

"""
清洗和统计性别数据
"""
def getCleanCountSex(df):
    user_clean=df.groupby("sex").count().reset_index()
    user_clean["lable"]= user_clean.apply(lambda x: getSex(x.sex),axis=1)+"["+user_clean.id.map(str)+"人]"
    return user_clean

"""
时间转换成年代
"""
def getBirthDay(birth_date):
    dt95='1995-01-01'
    dt90='1990-01-01'
    dt85='1985-01-01'
    dt80='1980-01-01'

    birth=str(birth_date)
    if birth>dt95:
        return '95后'
    if birth<dt95 and birth>dt90:
        return '90-95'
    if birth>dt85 and birth<dt90:
        return '85-90'
    if birth>dt80 and birth<dt85:
        return '80-85'
    if birth<dt80:
        return '70后'
    return '未知'

'''
清洗和统计年龄数据
'''
def getCleanCountBirth(df):
    df["era"]= df.apply(lambda x: getBirthDay(x.birth_date),axis=1)
    user_clean=df.groupby("era").count().reset_index()
    user_clean["lable"]= user_clean.era+"["+user_clean.id.map(str)+"人]"

    #print(user_clean)
    return user_clean

'''
level转换
'''
def getLevel(level_id):
    if level_id==1:
        return "p3"
    if level_id==2:
        return "p4"
    if level_id==3:
        return "p5"
    if level_id==4:
        return "p6"
    if level_id==5:
        return "p7"
    if level_id==6:
        return "p8"
    if level_id==7:
        return "p9"
    if level_id==8:
        return "p10"
    if level_id==9:
        return "M1"
    if level_id==10:
        return "M2"
    if level_id==11:
        return "M3"
    if level_id==12:
        return "M4"
    if level_id==13:
        return "M5"
    if level_id==14:
        return "M6"

'''
清洗和统计level数据
'''
def getCleanCountLevel(df):
    df["level"]= df.apply(lambda x: getLevel(x.level_id),axis=1)

    user_clean=df.replace('M1','P7').replace('M2','p8').replace('M3','P9').replace('M4','p10').\
               groupby("level").count().reset_index()
    user_clean["lable"]= user_clean.level +"["+user_clean.id.map(str)+"人]"
    return user_clean
    # user_clean_sort=user_clean.sort_values(by = 'lable',axis = 0,ascending = True)
    # print(user_clean_sort)
    # return user_clean_sort

'''
清洗和统计来源
'''
def getCleanCountChannel(df):
  user_clean=df.replace("boss直聘","Boss直聘").replace("","其他网络").replace("网络招聘","其他网络").\
      replace("猎聘","其他网络").replace("大街网","其他网络").replace("58同城","其他网络").replace("51job","其他网络").\
      replace("大街网","其他网络").replace("智联招聘","其他网络").replace("其他","其他网络").groupby("recruite_channel").count().reset_index()
  user_clean["lable"]= user_clean.recruite_channel +"["+user_clean.id.map(str)+"人]"
  #print(user_clean)
  return user_clean


'''
设置报表的中文字体，解决中文乱码
'''
def setChinafont(chart):
    for font in chart[1]:
      font.set_fontproperties(mpl.font_manager.FontProperties(
            fname='/System/Library/Fonts/STHeiti Light.ttc'))
      font.set_size(8)

'''
显示饼状图
'''
def showChart(df_edu,df_sex,df_birth,df_level,df_channel):
   edu_lable=df_edu["lable"].values
   edu_value=df_edu["id"].values
   ax1=plt.subplot(321)
   ax1.set_title(u'学历分布',fontproperties=getChineseFont(),fontsize=12)
   pie1=ax1.pie(edu_value,   labels=edu_lable, shadow=True, autopct='%1.1f%%')
   setChinafont(pie1)

   sex_lable=df_sex["lable"].values
   sex_value=df_sex["id"].values
   ax2=plt.subplot(322)
   ax2.set_title(u'性别分布',fontproperties=getChineseFont(),fontsize=12)
   pie2=ax2.pie(sex_value,   labels=sex_lable, shadow=True, autopct='%1.1f%%')
   setChinafont(pie2)

   birth_lable=df_birth["lable"].values
   birth_value=df_birth["id"].values
   ax3=plt.subplot(323)
   ax3.set_title(u'年龄分布',fontproperties=getChineseFont(),fontsize=12)
   pie3=ax3.pie(birth_value,   labels=birth_lable, shadow=True, autopct='%1.1f%%')
   setChinafont(pie3)

   level_lable=df_level["lable"].values
   level_value=df_level["id"].values
   ax4=plt.subplot(324)
   ax4.set_title(u'level分布',fontproperties=getChineseFont(),fontsize=12)

   pie4=ax4.pie(level_value,   labels=level_lable, shadow=True, autopct='%1.1f%%')

   setChinafont(pie4)

   channel_lable=df_channel["lable"].values
   channel_value=df_channel["id"].values
   ax5=plt.subplot(325)
   ax5.set_title(u'来源渠道分布',fontproperties=getChineseFont(),fontsize=12)

   pie5=ax5.pie(channel_value,   labels=channel_lable, shadow=True, autopct='%1.1f%%')

   #ax5.legend(prop=getChineseFont(), loc=0, bbox_to_anchor=(0.82, 1))  # 图例
   #设置legend的字体大小
   # leg = ax5.get_legend()
   # ltext = leg.get_texts()
   # pie5.setp(ltext, fontsize=6)
   setChinafont(pie5)

   plt.show()




if __name__ == '__main__':
    user=getEmpList()

    df_edu=getCleanCountEduDf(user)
    df_sex=getCleanCountSex(user)
    df_birth=getCleanCountBirth(user)
    df_level=getCleanCountLevel(user)
    df_channel=getCleanCountChannel(user)

    showChart(df_edu,df_sex,df_birth,df_level,df_channel)


