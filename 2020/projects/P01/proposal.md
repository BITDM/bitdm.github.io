---
layout: page
mathjax: true
permalink: /2020/projects/p01/proposal/
---

## 基于数据挖掘技术的个性化微博推荐

### 成员

* 彭成（3120191033）
* 高佳萌（3220190942）
* 赵嘉旌（3220190923）
* 李家硕（3220190952）
* 张博（3220190995）

### 问题描述

#### 1、问题背景及分析

随着移动互联网的发展，各种移动社交应用不断涌现，如国外的Facebook、Twitter，国内的微博等，社交应用的出现和飞速发展深深影响了人们的交流和娱乐方式，成为人们生活中不可或缺的一部分。用户可以通过PC、手机等多种移动终端，实现信息的即时分享、传播互动。微博由于其自身内容的丰富性和实时性吸引了大量的用户，是当下最热门的社交平台之一。目前，微博内容存量已超过千亿，庞大的用户生成内容带来的信息过载问题，使得用户难以从大量的信息中获取自己感兴趣的。微博用户主要的信息获取方式来源于主页，也就是通过关注其他用户，接收他们的微博，形成自己的收听列表。一个活跃的微博用户每天在主页能收取到成百上千的微博，用户无法看完所有微博，并且其中很多微博未必是用户感兴趣的内容。所以，准确的挖掘用户兴趣，利用好的推荐算法，优先给用户展现其感兴趣的内容，对提升用户体验起着至关重要的作用。本项目以微博为例，利用数据挖掘技术挖掘用户兴趣，为用户提供准确和高效的知识服务，辅助解决信息过载问题。

#### 2、问题描述

2.1 数据准备

本课题利用从新浪微博API爬取的真实用户数据进行实验。随机选择20名活跃用户作为目标用户，爬取其一个月内发布的微博，以及目标用户的主页微博，即关注列表的微博信息，共包括3217名用户的216176条微博。其中每条微博包含ID、作者ID、发布时间、内容、点赞数、评论数、转发数等信息。

2.2 准备采用的方法或模型

采用关键词挖掘、关联规则等数据挖掘技术从不同角度挖掘用户兴趣，并根据得到的用户兴趣召回待推荐的微博。从微博中提取用于分类的特征，对这些特征进行数据分析和可视化。从用户历史行为中提取正负样本，采用深度神经网络，利用分类特征训练模型。使用训练好的模型对待推荐微博进行排序，得到推荐集。

2.3 预期的挖掘结果

为目标用户生成推荐微博集

### 项目评估

本项目采用推荐的准确率和召回率进行效果评估。

### 项目分工

* 彭成：算法实现，数据分析
* 高佳萌：算法实现，文档编写
* 赵嘉旌：算法实现，可视化
* 李佳硕：提取特征，文档编写
* 张博：构建模型，文档编写