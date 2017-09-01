# -*- coding: utf-8 -*-
"""
Created on Mon May 15 22:13:26 2017

@author: Roach
"""
from math import sqrt
import pandas as pd
#----------------------------------导入数据------------------------------------
def loadMovieLens():
    rating_col_name = ['user_id','movie_id','rating','timestamp']
    ratings = pd.read_csv('D:/BIT/DataMining/data/rating.csv',names=rating_col_name)
    movies_col_name = ['movie_id','title','type'];
    movie = pd.read_csv('D:/BIT/DataMining/data/movies.csv',names=movies_col_name)
    movies = {}
    items = len(movie['movie_id'])
    for i in range(items):
        id = movie['movie_id'][i]
        movies[id] = movie['title'][i]
    prefs = {}
    items = len(ratings['user_id'])
    for j in range(items):
        user = ratings['user_id'][j]
        movieid = ratings['movie_id'][j]
        rating = ratings['rating'][j]
#        ts = ratings['timestamp'][item]
        prefs.setdefault(user,{})
        prefs[user][movies[movieid]] = float(rating)
    return prefs  
#----------------------------------导入数据------------------------------------

#--------------------计算并返回p1和p2的皮尔逊相关系数---------------------------
def sim_pearson(prefs,p1,p2):
    # 得到双方都曾评价过的电影列表
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]: 
            si[item] = 1
    # 得到列表的元素个数
    n = len(si)
    # 当两个用户共同评分的电影少于6部时，相似度置为0
    if n <= 5:
        return 0
    
    #对所有偏好求和
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])
    
    #求平方和
    sum1sq = sum([pow(prefs[p1][it],2) for it in si])
    sum2sq = sum([pow(prefs[p2][it],2) for it in si])
    
    #求乘积之和
    pSum = sum([prefs[p1][it]*prefs[p2][it] for it in si])
    
    #计算皮尔逊评价值
    num = pSum-(sum1*sum2/n)
    den = sqrt((sum1sq-pow(sum1,2)/n)*(sum2sq-pow(sum2,2)/n))
    if den == 0:
        return 0
        
    r = num/den
    return r
#--------------------计算并返回p1和p2的皮尔逊相关系数---------------------------

#-----------------------从反映偏好的字典中返回最匹配者---------------------------
#返回的个数为可选参数
def topMatches(prefs,person,n=5):
    scores = [(sim_pearson(prefs,person,other),other) for other in prefs if other!=person]

    # 对列表进行排序，评价值最高的在前
    scores.sort()
    scores.reverse()
    return scores[0:n]
#-----------------------从反映偏好的字典中返回最匹配者---------------------------

#---------------根据所有用户进行加权平均来推荐电影，权重为相似度------------------
def getRecommendations(prefs,person):
    totals = {}
    simSums = {}
    for other in prefs:
        if other == person:
            continue
        sim = sim_pearson(prefs,person,other)
        # 忽略评价值为小于等于0的情况
        if sim <= 0.8:
            continue
        for item in prefs[other]:
            # 只对被推荐的用户未看过的电影进行评价
            if item not in prefs[person] or prefs[person][item] == 0:
                totals.setdefault(item,0)
                # 相似度*评价值
                totals[item]+=prefs[other][item]*sim
                # 相似度之和
                simSums.setdefault(item,0)
                simSums[item]+=sim
    # 建立一个归一化的列表
    rankings = [(total/simSums[item],item) for item,total in totals.items()]
                
    #返回经过排序的列表
    rankings.sort()
    rankings.reverse()
    return rankings

#---------------根据所有用户进行加权平均来推荐电影，权重为相似度------------------
prefs = loadMovieLens()
print(topMatches(prefs,1,n=5))
recommendation_list = getRecommendations(prefs,1)[0:20] 
for i in range(len(recommendation_list)) :
    print(recommendation_list[i])
