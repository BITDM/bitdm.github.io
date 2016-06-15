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
选题背景：
DVD在线租赁商 Netflix 于 2006 年 10 月 2 日发起一项竞赛：Netflix Prize，任何组织或个人 只要能够提交比它现有电影推荐系统 Cinematch 效果好 10% 的新方法，就可以获得一百万美元的奖金。竞赛最多持续到 2011 年 10 月 2 日。同时，Netflix Prize 还提供每年五万美元的年度进步奖。

题目数据：
统计：1亿打分，480189用户，17770电影
格式：
	training_set：
	MovieID：
	CustomerID,Rating,Date

	movie_titles：
 	MovieID,YearOfRelease,Title

 	probe：
	需要预测的数据

课题内容：
1 通过分析用户的评分行为，对用户构建用户与用户之间的相似度矩阵
2 通过分析电影的评分，对电影构建电影与电影之间的相似度矩阵
3 利用Item based collective filtering算法进行预测
4 利用user based collective filtering算法进行预测
5 选着较好的算法进行进一步优化（从相似度方面优化）


中期总结：
Item based collective filtering
总结：物以类聚
原因：item的增长速度远小于user的增长速度
方法：离线计算item的相似度矩阵供线上使用
缺点：由于基于item的相似性，故推荐的item相似，缺乏多样性

针对课题的解决方法：
Item <＝> movie
相似性度量的特征： 用户群体
规则：观看的用户群体重合度越高，电影相似度越高
评分：将相同用户对另一个电影的评分作为相似电影的评分

user based collective filtering
总结：人以群分，找和用户有相同品味的其他用户
适用范围：item更新频繁的应用
方法：通过相似用户喜欢的item推荐给该用户
缺点：相似用户群比较敏感，要频繁地计算出用户的相似用户矩阵，运算量会非常大。  推荐的大多是大家都喜欢的热门推荐，有点趋于大众化了

针对课题的解决方法：
相似性度量的特征： 
1 看过的电影
2 历史评分
规则：历史观看电影重合度越高，用户越相似
            对同一电影评分越相近，用户越相似
	      历史评分平均值越相近，用户越相似
评分：对于某个用户，要对A电影评分，将A电影的评分用户    中与A相似度达到一定程度的用户的平均分作为这个电影对A的评分

代码已上传到github上：
网址为：https://github.com/BitrSky/MLProject
