---
layout: page
mathjax: true
permalink: /2018/projects/p11/midterm/
---

## 项目进展报告

### 数据获取及预处理

1. 采用了阿里云天池比赛提供的数据集，包括了20000用户的完整行为数据以及百万级的商品信息，数据包含两个部分。 第一部分是用户在商品全集上的移动端行为数据（D），第二个部分是商品子集（P）。
```python
user = pd.read_csv("../dataset/tianchi_fresh_comp_train_user.csv")
print 'len is %d' % user.shape[0]
print user.dtypes
print user.describe()
geohash = user.loc[user.loc[:,'user_geohash'].isnull()==True,'user_geohash']
time = user.loc[user.loc[:,'time'].isnull()==False,'time']
print 'missing count of geohash: %d' % geohash.shape[0]
print 'missing count of time: %d' % time.shape[0]

item = pd.read_csv("../dataset/tianchi_fresh_comp_train_item.csv")
print 'len is %d' % item.shape[0]
print item.dtypes
print item.describe()
geohash1 = item.loc[item.loc[:,'item_geohash'].isnull()==True,'item_geohash']
print 'missing count of geohash: %d' % geohash1.shape[0]
```
```
len is 23291027

user_id           int64
item_id           int64
behavior_type     int64
user_geohash     object
item_category     int64
time             object
dtype: object

            user_id       item_id  behavior_type  item_category
count  2.329103e+07  2.329103e+07   2.329103e+07   2.329103e+07
mean   7.006868e+07  2.023214e+08   1.106268e+00   6.835397e+03
std    4.569072e+07  1.167440e+08   4.599087e-01   3.812873e+03
min    4.920000e+02  3.700000e+01   1.000000e+00   2.000000e+00
25%    3.019541e+07  1.014417e+08   1.000000e+00   3.690000e+03
50%    5.626942e+07  2.022430e+08   1.000000e+00   6.054000e+03
75%    1.166482e+08  3.035325e+08   1.000000e+00   1.027100e+04
max    1.424430e+08  4.045625e+08   4.000000e+00   1.408000e+04

missing count of geohash: 15911010
missing count of time: 0
```

```
len is 620918

item_id           int64
item_geohash     object
item_category     int64
dtype: object

            item_id  item_category
count  6.209180e+05  620918.000000
mean   2.004351e+08    6970.213167
std    1.191648e+08    3479.627372
min    9.580000e+02       2.000000
25%    9.357641e+07    4245.000000
50%    2.053761e+08    6890.000000
75%    3.054015e+08   10120.000000
max    4.045624e+08   14071.000000

missing count of geohash: 417508

```
其中缺失较多的是记录了位置的geohash，但考虑到地点标记可能有用，不剔除这些数据。


2. 对数据中的的购买做统计分析


### 数据分析与可视化

> 描述对数据进行探索性分析的结果，采用可视化的技术呈现

### 模型选取

> 选择了哪些数据挖掘方法对数据进行分析与挖掘，及选择的理由

### 挖掘实验的结果

> 进行数据挖掘后得到的结果

### 存在的问题

> 到目前为止，遇到哪些问题，及解决方法或思路

### 下一步工作

> 准备如何完成后续的工作
