import pandas as pd
from sqlalchemy import create_engine
import re
import numpy as np
from pandas import DataFrame

engine = create_engine('mysql+pymysql://root:@localhost:3306/datamining?charset=utf8')
sql = pd.read_sql('all_gzdata', engine, chunksize = 10000)
'''
用create_engine建立连接，连接地址的意思依次为“数据库格式（mysql）+程序名（pymysql）+账号密码@地址端口/数据库名（test）”，最后指定编码为utf8；
all_gzdata是表名，engine是连接数据的引擎，chunksize指定每次读取1万条记录。这时候sql是一个容器，未真正读取数据。
'''
#统计中间类型网页（带midques_关键字）
def countmidques(i):
    j = i[['fullURL','fullURLId','realIP']].copy()
    j['type'] = u'非中间类型网页'
    j['type'][j['fullURL'].str.contains('midques_')]= u'中间类型网页'
    return j['type'].value_counts()
counts1 = [countmidques(i) for i in sql]
counts1 = pd.concat(counts1).groupby(level=0).sum()
counts1

#主网址去掉无.html点击行为的用户记录
def countnohtml(i):
    j = i[['fullURL','pageTitle','fullURLId']].copy()
    j['type'] = u'有html页面'
    j['type'][j['fullURL'].str.contains('\.html')==False] = u'无.html点击行为的用户记录'

    return j['type'].value_counts()
counts2 = [countnohtml(i) for i in sql]
counts2 = pd.concat(counts2).groupby(level=0).sum()
counts2

# *备注：此规则中要删除的记录的网址均不含有.html，所以，规则三需要过滤的信息包含了规则2中需要过滤的
engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/jing?charset=utf8')
sql = pd.read_sql('all_gzdata', engine, chunksize = 10000)

#主网址是律师的浏览信息网页（快车-律师助手）、咨询发布成功、快搜免费发布法律
def countothers(i):
    j = i[['fullURL','pageTitle','fullURLId']].copy()
    j['type'] = u'其他'
    j['pageTitle'].fillna(u'空',inplace=True)
    j['type'][j['pageTitle'].str.contains(u'快车-律师助手')]= u'快车-律师助手'
    j['type'][j['pageTitle'].str.contains(u'咨询发布成功')]= u'咨询发布成功'
    j['type'][(j['pageTitle'].str.contains(u'免费发布法律咨询')) | (j['pageTitle'].str.contains(u'法律快搜'))] = u'快搜免费发布法律咨询'

    return j['type'].value_counts()
counts3 = [countothers(i) for i in sql]
counts3 = pd.concat(counts3).groupby(level=0).sum()
counts3

#去掉网址中问号后面的部分，截取问号前面的部分;去掉主网址不包含关键字
def deletquesafter(i):
    j = i[['fullURL']].copy()
    j['fullURL'] = j['fullURL'].str.replace('\?.*','')
    j['type'] = u'主网址不包含关键字'
    j['type'][j['fullURL'].str.contains('lawtime')] = u'主网址包含关键字'
    return j

counts4 = [deletquesafter(i) for i in sql]
counts4 = pd.concat(counts4)

counts4['type'].value_counts()

#数据清洗
for i in sql:
    d = i[['realIP', 'fullURL','pageTitle','userID','timestamp_format']].copy() # 只要网址列
    d['fullURL'] = d['fullURL'].str.replace('\?.*','') # 网址中问号后面的部分
    d = d[(d['fullURL'].str.contains('\.html')) & (d['fullURL'].str.contains('lawtime')) & (d['fullURL'].str.contains('midques_') == False)] # 只要含有.html的网址
    # 保存到数据库中
    d.to_sql('cleaned_one', engine, index = False, if_exists = 'append')

for i in sql:
    d = i[['realIP','fullURL','pageTitle','userID','timestamp_format']]# 只要网址列
    d['pageTitle'].fillna(u'空',inplace=True)
    d = d[(d['pageTitle'].str.contains(u'快车-律师助手') == False) & (d['pageTitle'].str.contains(u'咨询发布成功') == False) & \
          (d['pageTitle'].str.contains(u'免费发布法律咨询') == False) & (d['pageTitle'].str.contains(u'法律快搜') == False)\
         ].copy()
    # 保存到数据库中
    d.to_sql('cleaned_two', engine, index = False, if_exists = 'append')

def dropduplicate(i):
    j = i[['realIP','fullURL','pageTitle','userID','timestamp_format']].copy()
    return j

count6 = [dropduplicate(i) for i in sql]
count6 = pd.concat(count6)

count7 = count6.drop_duplicates(['fullURL','userID','timestamp_format']) # 一定要进行二次删除重复，因为不同的块中会有重复值


#数据变换
for i in sql:
    d = i.copy()
    # 获取所有记录的个数
    temp0 = len(d)
    l0 = l0 + temp0

    # 获取类似于http://www.lawtime.cn***/2007020619634_2.html格式的记录的个数
    # 匹配1 易知，匹配1一定包含匹配2
    x1 = d[d['fullURL'].str.contains('_\d{0,2}.html')]
    temp1 = len(x1)
    l1 = l1 + temp1

    # 匹配2
    # 获取类似于http://www.lawtime.cn***/29_1_p3.html格式的记录的个数
    x2 = d[d['fullURL'].str.contains('_\d{0,2}_\w{0,2}.html')]
    temp2 = len(x2)
    l2 = l2 + temp2

    x1.to_sql('l1', engine, index=False, if_exists = 'append') # 保存
    x2.to_sql('l2', engine, index=False, if_exists = 'append') # 保存

for i in sql:
    d = i.copy()

    # 注意！！！替换1和替换2的顺序不能颠倒，否则删除不完整
    # 替换1 将类似于http://www.lawtime.cn***/29_1_p3.html下划线后面部分"_1_p3"去掉，规范为标准网址
    d['fullURL'] = d['fullURL'].str.replace('_\d{0,2}_\w{0,2}.html','.html')#这部分网址有　9260　个

    # 替换2 将类似于http://www.lawtime.cn***/2007020619634_2.html下划线后面部分"_2"去掉，规范为标准网址
    d['fullURL'] = d['fullURL'].str.replace('_\d{0,2}.html','.html') #这部分网址有　55455-9260 = 46195 个

    d = d.drop_duplicates(['fullURL','userID']) # 删除重复记录(删除有相同网址和相同用户ID的)【不完整】因为不同的数据块中依然有重复数据
    temp = len(d)
    l4 = l4 + temp
    d.to_sql('changed_1', engine, index=False, if_exists = 'append') # 保存
for i in sql:
    d = i.copy()
    # 获取所有记录的个数
    temp0 = len(d)
    l0 = l0 + temp0

    # 获取类似于http://www.lawtime.cn***/2007020619634_2.html格式的记录的个数
    # 匹配1 易知，匹配1一定包含匹配2
    x1 = d[d['fullURL'].str.contains('_\d{0,2}.html')]
    temp1 = len(x1)
    l1 = l1 + temp1

    # 匹配2
    # 获取类似于http://www.lawtime.cn***/29_1_p3.html格式的记录的个数
    x2 = d[d['fullURL'].str.contains('_\d{0,2}_\w{0,2}.html')]
    temp2 = len(x2)
    l2 = l2 + temp2

#网页分类
pattern = re.compile('/info/(.*?)/',re.S)
e = d[d['iszsk'] == 'infoelsezsk']
for i in range(len(e)):
    e.iloc[i,2] = re.findall(pattern, e.iloc[i,0])[0]
    e.head()

# 对于http://www.lawtime.cn/zhishiku/laodong/info/***.html类型的网址进行这样匹配,获取二级类别名称"laodong"
# 由于还有一类是http://www.lawtime.cn/zhishiku/laodong/***.html，所以使用'zhishiku/(.*?)/'进行匹配
pattern1 = re.compile('zhishiku/(.*?)/',re.S)
f = d[d['iszsk'] == 'zsk']
for i in range(len(f)):
#     print i
    f.iloc[i,2] = re.findall(pattern1, f.iloc[i,0])[0]
e.columns = ['fullURL', 'type1', 'type2']
e.head()

f.columns = ['fullURL', 'type1', 'type2']
f.head()

# 将两类处理过二级类别的记录合并，求二级类别的交集
g = pd.concat([e,f])
h = g['type2'].value_counts()

# 求两类网址中的二级类别数，由结果可知，两类网址的二级类别的集合的并集满足所需条件
len(e['type2'].value_counts()) # 66
len(f['type2'].value_counts()) # 31
len(g['type2'].value_counts()) # 69

h.head()

h.index # 列出知识类别下的所有的二级类别
detailtypes = h.index
for i in range(len(detailtypes)):
    x = g[g['type2'] == h.index[i]]
# 复制e的备份进行处理，避免操作中改变了数据
q = e.copy()
q['type3'] = np.nan
resultype3 = DataFrame([],columns=q.columns)
for i in range(len(h.index)):
    pattern2 = re.compile('/info/'+h.index[i]+'/(.*?)/',re.S)
    current = q[q['type2'] == h.index[i]]
    current.head()
    for j in range(len(current)):
        findresult = re.findall(pattern2, current.iloc[j,0])
        if findresult == []: # 若匹配结果是空，则将空值进行赋值给三级类别
            current.iloc[j,3] = np.nan
        else:
            current.iloc[j,3] = findresult[0]
    resultype3 = pd.concat([resultype3,current])# 将处理后的数据拼接
resultype3.head()

# 统计婚姻类下面的三级类别的数目
j = resultype3[resultype3['type2'] == 'hunyin']['type3'].value_counts()
len(j) # 145
j.head()

# 方式1
Type3nums = resultype3.pivot_table(index = ['type2','type3'], aggfunc = 'count')
# 方式2: Type3nums = resultype3.groupby([resultype3['type2'],resultype3['type3']]).count()
r = Type3nums.reset_index().sort_values(by=['type2','type1'],ascending=[True,False])
r.set_index(['type2','type3'],inplace = True)
#保存的表名命名格式为“2_2_k此表功能名称”，此表表示生成的第1张表格，功能为Type3nums：得出所有三级类别
r.to_excel('2_2_3Type3nums.xlsx')
r

#属性归约
for i in sql:
    zixun = i[['userID','fullURL']][i['fullURL'].str.contains('(ask)|(askzt)')].copy()
    l1 = len(zixun) + l1
    hunyin = i[['userID','fullURL']][i['fullURL'].str.contains('hunyin')].copy()
    l2 = len(hunyin) + l2
    zixun.to_sql('zixunformodel', engine, index=False,if_exists = 'append')
    hunyin.to_sql('hunyinformodel', engine, index=False,if_exists = 'append')  
