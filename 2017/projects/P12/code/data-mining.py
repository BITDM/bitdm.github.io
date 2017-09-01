# -*- coding: utf-8 -*-
"""
Created on Sun May 14 11:28:23 2017

@author: Roach
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#---------------------------------读入数据-------------------------------------
users_col_name = ['user_id','sex','age','occupation','zip_code']
users= pd.read_csv('D:/BIT/DataMining/data/users.csv',names=users_col_name)
rating_col_name = ['user_id','movie_id','rating','timestamp']
rating = pd.read_csv('D:/BIT/DataMining/data/rating.csv',names=rating_col_name)
movies_col_name = ['movie_id','title','type'];
movies = pd.read_csv('D:/BIT/DataMining/data/movies.csv',names=movies_col_name)
# 将三个数据集关联合并
rating_movie = pd.merge(rating,movies)
data = pd.merge(rating_movie,users)
#---------------------------------读入数据-------------------------------------

#---------------------------评分最多的前50部电影--------------------------------
most_rated = data.title.value_counts()[:50]
print("评分数目最多的前50部电影：")
print(most_rated)
#---------------------------评分最多的前50部电影--------------------------------

#-------------------评分最高的前50部电影(评分数量大于100)------------------------
#计算每部电影的平均评分
movie_ave = data.groupby('title').agg({'rating':[np.size,np.mean]})
#对评分数目大于100的电影进行排序，选取前50名
threshold = movie_ave['rating']['size'] > 100
sort_rating = movie_ave[threshold].sort_values([('rating','mean')],ascending=False)[:50]
print("评分数目大于100的平均评分最高的前50部电影：")
print(sort_rating)
#-------------------评分最高的前50部电影(评分数量大于100)------------------------

#----------------------------------性别差异------------------------------------
data.reset_index('movie_id', inplace=True)
most_50 = data.groupby('movie_id').size().sort_values(ascending=False)[:50]
pivoted = data.pivot_table(index = ['movie_id', 'title'], columns = ['sex'],
                          values = 'rating', fill_value = 0)
#print(pivoted)
pivoted['diff'] = pivoted.M - pivoted.F
pivoted.reset_index('movie_id', inplace=True)
disagreements = pivoted[pivoted.movie_id.isin(most_50.index)]['diff']
disagreements.sort_values().plot(kind='barh', figsize=[9, 15])
plt.title('Male vs. Female Avg. Ratings\n(Difference > 0 = Favored by Men)')
plt.ylabel('Title')
plt.xlabel('Average Rating Difference');
plt.show()

#----------------------------------性别差异------------------------------------

#----------------------------年龄对评分的影响-----------------------------------
#不同年龄段的评分情况
age_label = ['under 18','18-24','25-34','35-44','45-49','50-55','56+']
data['age_group'] = pd.cut(data.age, range(1, 9, 1), right=False, labels=age_label)
age_rating = data.groupby('age_group').agg({'rating':[np.mean]})
print("不同年龄段的评分情况")
print(age_rating)
#年龄分布情况
print("参与评分的用户年龄分布图")
plt.figure()
plt.ylabel("count")
plt.xlabel("age")
plt.xticks((1.5,2.5,3.5,4.5,5.5,6.5,7.5),('under 18','18-24','25-34','35-44','45-49','50-55','56+'))
users.age.plot.hist(bins=7,range=(1,8));
#----------------------------年龄对评分的影响-----------------------------------



