import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:@localhost:3306/datamining?charset=utf8')
sql = pd.read_sql('all_gzdata', engine, chunksize = 10000)
'''
用create_engine建立连接，连接地址的意思依次为“数据库格式（mysql）+程序名（pymysql）+账号密码@地址端口/数据库名（test）”，最后指定编码为utf8；
all_gzdata是表名，engine是连接数据的引擎，chunksize指定每次读取1万条记录。这时候sql是一个容器，未真正读取数据。
'''

#counts
counts1 = [ i['fullURLId'].value_counts() for i in sql] #逐块统计
counts1
counts1 = pd.concat(counts1).groupby(level=0).sum() #合并统计结果，把相同的统计项合并（即按index分组并求和）
counts1
counts1 = counts1.reset_index() #重新设置index，将原来的index作为counts的一列。
counts1
counts1.columns = ['index', 'num'] #重新设置列名，主要是第二列，默认为0
counts1['type'] = counts1['index'].str.extract('(\d{3})') #提取前三个数字作为类别id（！！！）
counts1
counts1_ = counts1[['type', 'num']].groupby('type').sum() #按类别合并
counts1_.sort_values(by='num', ascending=False,inplace=True) #降序排列
counts1_['percentage'] = (counts1_['num']/counts1_['num'].sum())*100

#保存的表名命名格式为“1_1_k此表功能名称”，此表表示生成的第1张表格，功能为type_counts：计算各个大类占的比例
counts1_.to_excel('1_1_1type_counts.xlsx')

def count107(i): #自定义统计函数
    j = i[['fullURL']][i['fullURLId'].str.contains('107')].copy() #找出类别包含107的网址
    j['type'] = None # 添加空列
    j['type'][j['fullURL'].str.contains('info/.+?/')]= u'知识首页'
    j['type'][j['fullURL'].str.contains('info/.+?/.+?')]= u'知识列表页'
    j['type'][j['fullURL'].str.contains('/\d+?_*\d+?\.html')]= u'知识内容页'
    return j['type'].value_counts()
# 注意：获取一次sql对象就需要重新访问一下数据库(!!!)
engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/jing?charset=utf8')
sql = pd.read_sql('all_gzdata', engine, chunksize = 10000)

counts2 = [count107(i) for i in sql] # 逐块统计
counts2 = pd.concat(counts2).groupby(level=0).sum() # 合并统计结果
counts2

#统计带"?"问号网址类型统计
def countquestion(i): #自定义统计函数
    j = i[['fullURLId']][i['fullURL'].str.contains('\?')].copy() #找出类别包含107的网址
    return j

engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/jing?charset=utf8')
sql = pd.read_sql('all_gzdata', engine, chunksize = 10000)

counts3 = [countquestion(i)['fullURLId'].value_counts() for i in sql]
counts3 = pd.concat(counts3).groupby(level=0).sum()
counts3

def page199(i): #自定义统计函数
    j = i[['fullURL','pageTitle']][(i['fullURLId'].str.contains('199')) & (i['fullURL'].str.contains('\?'))]
    j['pageTitle'].fillna(u'空',inplace=True)
    j['type'] = u'其他' # 添加空列
    j['type'][j['pageTitle'].str.contains(u'法律快车-律师助手')]= u'法律快车-律师助手'
    j['type'][j['pageTitle'].str.contains(u'咨询发布成功')]= u'咨询发布成功'
    j['type'][j['pageTitle'].str.contains(u'免费发布法律咨询' )] = u'免费发布法律咨询'
    j['type'][j['pageTitle'].str.contains(u'法律快搜')] = u'快搜'
    j['type'][j['pageTitle'].str.contains(u'法律快车法律经验')] = u'法律快车法律经验'
    j['type'][j['pageTitle'].str.contains(u'法律快车法律咨询')] = u'法律快车法律咨询'
    j['type'][(j['pageTitle'].str.contains(u'_法律快车')) | (j['pageTitle'].str.contains(u'-法律快车'))] = u'法律快车'
    j['type'][j['pageTitle'].str.contains(u'空')] = u'空'

    return j
# 注意：获取一次sql对象就需要重新访问一下数据库
engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/jing?charset=utf8')
sql = pd.read_sql('all_gzdata', engine, chunksize = 10000)# 分块读取数据库信息

counts4 = [page199(i) for i in sql] # 逐块统计
counts4 = pd.concat(counts4)
d1 = counts4['type'].value_counts()

d2 = counts4[counts4['type']==u'其他']
def xiaguang(i): #自定义统计函数
    j = i[['fullURL','fullURLId','pageTitle']][(i['fullURL'].str.contains('\.html'))==False]
    return j

# 注意获取一次sql对象就需要重新访问一下数据库
engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/jing?charset=utf8')
sql = pd.read_sql('all_gzdata', engine, chunksize = 10000)# 分块读取数据库信息

counts5 = [xiaguang(i) for i in sql]
counts5 = pd.concat(counts5)


xg1 = counts5['fullURLId'].value_counts()
xg1

# 求各个部分的占比并保存数据
xg_ =  pd.DataFrame(xg1)
xg_.reset_index(inplace=True)
xg_.columns= ['index', 'num']
xg_['perc'] = xg_['num']/xg_['num'].sum()*100
xg_.sort_values(by='num',ascending=False,inplace=True)

xg_['type'] = xg_['index'].str.extract('(\d{3})') #提取前三个数字作为类别id

xgs_ = xg_[['type', 'num']].groupby('type').sum() #按类别合并
xgs_.sort_values(by='num', ascending=False,inplace=True) #降序排列
xgs_['percentage'] = xgs_['num']/xgs_['num'].sum()*100

#保存的表名命名格式为“1_1_k+此表功能名称”，此表表示生成的第6张表格，功能为xiaguang，计算瞎逛用户中各个类型占比
xgs_.round(4).to_excel('1_1_6xiaguang.xlsx')
xgs_.round(4)


