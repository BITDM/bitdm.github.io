---
layout: page
mathjax: true
permalink: /2020/projects/10/proposal/
---

## 热点话题检测

## 成员

* 程浩东 3120190982
* 边晓航 3120190977
* 李雪宜 3220190832
* 林 宁 3220190838

### 问题描述

#### 1、问题背景及分析

随着信息传播手段的进步，尤其是互联网这一新媒体的出现，我们已经摆脱了信息贫乏的栓桔。由于网络信息数量庞大，与一个话题相关的信息往往孤立地分散在很多不同的地方并且出现在不同的时间，仅仅通过这些孤立的信息，人们对某些事件难以做到全面的把握。

我希望建立一个模型可以帮助人们把分散的信息有效地汇集并组织起来，从整体上了解一个事件的全部细节以及与该事件与其它事件之间的关系，实现对热点话题的检测发现。

#### 2、问题描述

2.1 数据准备

本项目涉及两个概念，一是话题topic, 二是报道report(语料)。 话题包括名称ID 和特征(feature)。 ID可以理解为关键词（主题词，事件名），比如“三星折叠屏”， “斯里兰卡爆炸”等。Feature是我们根据语料库挖掘出的特征。

首先,通过爬虫技术爬取了新浪、搜狐、新华网等新闻网页的大量实时新闻。

由于爬取到的内容存在大量的dirty数据，我们通过文本处理技术，对爬取​到的内容进行清洗. 其次，利用jieba,分词、TF-IDF技术、聚类算法对清洗过​的新闻文本进行特征提取与聚类分析。得到了新闻的聚合簇。最后，使用​TextRank算法对每一处 聚合簇中的新闻贡献度进行排名，结合聚类结果​与词向量分析，得到了对新闻热度的排名与分析。

2.2 准备采用的方法或模型

构建一个可以发现实时热点话题新闻的模型

### 项目评估

* 将微博的top100热门话题作为标签
* 用模型的召回率，精确率来衡量模型的效果

### 项目分工

* 程浩东 3120190982：分词、关键词提取、TextRank排序、文档撰写
* 边晓航 3120190977：分词、关键词提取、TextRank排序、文档撰写
* 李雪宜 3220190832：数据爬取、数据清洗、DBACAN聚类及可视化、文档撰写等
* 林宁 3220190838：数据爬取、数据清洗、DBACAN聚类及可视化、文档撰写等