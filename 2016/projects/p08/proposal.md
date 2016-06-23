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


### 数据来源

netflix prize 数据集

### 选题背景

DVD在线租赁商 Netflix 于 2006 年 10 月 2 日发起一项竞赛：Netflix Prize，任何组织或个人 只要能够提交比它现有电影推荐系统 Cinematch 效果好 10% 的新方法，就可以获得一百万美元的奖金。竞赛最多持续到 2011 年 10 月 2 日。同时，Netflix Prize 还提供每年五万美元的年度进步奖。

### 题目数据

统计：1亿打分，480189用户，17770电影

格式：
	
    training_set：
	MovieID：
	CustomerID,Rating,Date
	movie_titles：
 	MovieID,YearOfRelease,Title

 	probe：
	需要预测的数据

### 课题内容

1 通过分析用户的评分行为，对用户构建用户与用户之间的相似度矩阵

2 通过分析电影的评分，对电影构建电影与电影之间的相似度矩阵

3 利用Item based collective filtering算法进行预测

4 利用user based collective filtering算法进行预测

5 选着较好的算法进行进一步优化（从相似度方面优化）