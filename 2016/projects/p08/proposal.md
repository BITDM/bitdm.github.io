---
layout: page
mathjax: true
permalink: /2016/projects/p08/proposal/
---

## 基于用户对电影的历史评分数据解决电影评分预测问题

### 成员

- 高志伟
- 王子硕
- 刘云洋
- 张露露

*翻译成中文*

数据来源：netflix prize 数据集
课题内容：
1 Predict the rating a user will give on a movie from the movies that user has rated in the past, as well as the ratings similar users have given similar movies。
2 Discover clusters of similar movies or users。
QUALIFYING AND PREDICTION DATASET FILE DESCRIPTION
The qualifying dataset for the Netflix Prize is contained in the text file
“qualifying.txt”. It consists of lines indicating a movie id, followed by a
colon, and then customer ids and rating dates, one per line for that movie id.
The movie and customer ids are contained in the training set. Of course the
ratings are withheld. There are no empty lines in the file.

MovieID1:
CustomerID11,Date11
CustomerID12,Date12
…
MovieID2:
CustomerID21,Date21
CustomerID22,Date22

For the Netflix Prize, your program must predict the all ratings the customers
gave the movies in the qualifying dataset based on the information in the
training dataset.

The format of your submitted prediction file follows the movie and customer id,
date order of the qualifying dataset. However, your predicted rating takes the
place of the corresponding customer id (and date), one per line.

For example, if the qualifying dataset looked like:

111:
3245,2005-12-19
5666,2005-12-23
6789,2005-03-14
225:
1234,2005-05-26
3456,2005-11-07

then a prediction file should look something like:
111:
3.0
3.4
4.0
225:
1.0
2.0

which predicts that customer 3245 would have rated movie 111 3.0 stars on the
19th of Decemeber, 2005, that customer 5666 would have rated it slightly higher
at 3.4 stars on the 23rd of Decemeber, 2005, etc.

You must make predictions for all customers for all movies in the qualifying
dataset.

THE PROBE DATASET FILE DESCRIPTION
To allow you to test your system before you submit a prediction set based on the
qualifying dataset, we have provided a probe dataset in the file “probe.txt”.
This text file contains lines indicating a movie id, followed by a colon, and
then customer ids, one per line for that movie id.

MovieID1:
CustomerID11
CustomerID12
…
MovieID2:
CustomerID21
CustomerID22

Like the qualifying dataset, the movie and customer id pairs are contained in
the training set. However, unlike the qualifying dataset, the ratings (and
dates) for each pair are contained in the training dataset.
