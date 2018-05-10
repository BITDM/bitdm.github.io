import pandas as pd
from sqlalchemy import create_engine
import re
import numpy as np
from pandas import DataFrame
import time

engine = create_engine('mysql+pymysql://root:@localhost:3306/datamining?charset=utf8')
data = pd.read_sql('all_gzdata', engine, chunksize = 10000)
'''
用create_engine建立连接，连接地址的意思依次为“数据库格式（mysql）+程序名（pymysql）+账号密码@地址端口/数据库名（test）”，最后指定编码为utf8；
all_gzdata是表名，engine是连接数据的引擎，chunksize指定每次读取1万条记录。这时候sql是一个容器，未真正读取数据。
'''
def Jaccard(a,b): #自定义杰卡德相似系数函数，仅对0-1矩阵有效
    return 1.0*(a*b).sum() /(a+b-a*b).sum()

class Recommender():
    sim = None # 相似度矩阵
    def similarity(self, x, distance): # 计算相似度矩阵的函数
        y = np.ones((len(x), len(x)))
        for i in range(len(x)):
            for j in range(len(x)):
                y[i,j] = distance(x[i], x[j])
        return y

    def fit(self, x, distance = Jaccard): # 训练函数
        self.sim = self.similarity(x, distance)
        return self.sim

    def recommend(self, a): # 推荐函数
        return np.dot(self.sim, a) * (1-a)
len(data['fullURL'].value_counts()) # 4339
len(data['realIP'].value_counts())
start0 = time.clock()
data.sort_values(by=['realIP','fullURL'],ascending=[True,True],inplace=True)
realIP = data['realIP'].value_counts().index
realIP = np.sort(realIP)
fullURL = data['fullURL'].value_counts().index #
fullURL = np.sort(fullURL)
D = DataFrame([], index = realIP, columns = fullURL )

for i in range(len(data)):
    a = data.iloc[i,0] # 用户名
    b = data.iloc[i,1] # 网址
    D.loc[a,b] = 1
D.fillna(0,inplace = True)
end0 = time.clock()
usetime0 = end0-start0
print( '转成0、1矩阵所花费的时间为'+ str(usetime0) +'s!')#34.5123141125s!
# D.shape=10333 rows × 4339 columns
#保存的表名命名格式为“3_1_k此表功能名称”，是本小节生成的第1张表格，功能为zero_one：整个数据集计算得到的0-1矩阵
D.to_csv('3_1_1zero_one.csv')

# 步骤：解决采用一次验证的方法，再创建十折交叉验证循环（此处只采用了一次具体十折交叉方法见3_2_10-fold cross-validation.py）
# 由于是基于物品（网址）的推荐，所以测试集需包含所有网址（全集），选择0.9*总用户数个用户记录来进行训练模型
# 注意：将数据随机打乱

# 随机打乱数据
# 注意 每次打乱数据，下面的都会改变
df = D.copy()

simpler = np.random.permutation(len(df))
df = df.take(simpler)# 打乱数据

train = df.iloc[:int(len(df)*0.9), :]
test = df.iloc[int(len(df)*0.9):, :]

df = df.as_matrix()

df_train = df[:int(len(df)*0.9), :]# 前90%为训练集len(df_train) = 9299
df_test = df[int(len(df)*0.9):, :]# 后10%为测试集len(df_test) = 103
df_train = df_train.T
df_test = df_test.T

print (df_train.shape) # (4339L, 9299L)
print (df_test.shape) # (4339L, 1034L)

#建立相似模型
start1 = time.clock()
r = Recommender()
sim = r.fit(df_train)# 计算物品的相似度矩阵
end1 = time.clock()

a = DataFrame(sim) # 保存相似度矩阵
usetime1 = end1-start1
print(u'建立相似矩阵耗时'+str(usetime1)+'s!')  #1981.60760257s!

print(a.shape )# (4339L, 9299L)

# 将所有数据保存
a.index = train.columns
a.columns = train.columns

#保存的表名命名格式为“3_1_k此表功能名称”，是本小节生成的第2张表格，功能为similarityMatrix：计算训练集的相似度矩阵
a.to_csv('3_1_2similarityMatrix.csv')
a.head(20)
# 使用测试集进行预测
df_test.shape # (4339L, 1034L)
start2 = time.clock()
result = r.recommend(df_test)
end2 = time.clock()

result1 = DataFrame(result)
usetime2 = end2-start2
print( u'推荐函数耗时'+str(usetime2)+'s!') # 推荐函数耗时2.60267174653s!

result1



# 定义展现具体协同推荐结果的函数，K为推荐的个数，recomMatrix为协同过滤算法算出的推荐矩阵的表格化
# type(K):int, type(recomMatrix):DataFrame

def xietong_result(K, recomMatrix ):
    recomMatrix.fillna(0.0,inplace=True)# 将表格中的空值用0填充
    n = range(1,K+1)
    recommends = ['xietong'+str(y) for y in n]
    currentemp = DataFrame([],index = recomMatrix.columns, columns = recommends)
    for i in range(len(recomMatrix.columns)):
        temp = recomMatrix.sort_values(by = recomMatrix.columns[i], ascending = False)
        k = 0
        while k < K:
            currentemp.iloc[i,k] = temp.index[k]
            if temp.iloc[k,i] == 0.0:
                currentemp.iloc[i,k:K] = np.nan
                break
            k = k+1

    return currentemp

start3 = time.clock()
xietong_result = xietong_result(3, result1)
end3 = time.clock()
print '按照协同过滤推荐方法为用户推荐3个未浏览过的网址耗时为' + str(end3 - start3)+'s!' #29.4996622053s!

#保存的表名命名格式为“3_1_k此表功能名称”，是本小节生成的第4张表格，功能为xietong_result：显示协同过滤推荐的结果
xietong_result.to_csv('3_1_4xietong_result.csv')

xietong_result # 结果中出现了全空的行，这是冷启动现象
