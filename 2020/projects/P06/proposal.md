---
layout: page
mathjax: true
permalink: /2020/projects/p06/proposal/
---

## 天池竞赛-商家促销后的重复买家预测

### 成员

* 周泳宇（3120191079）
* 邵江逸（3120191038）
* 周田（3220190931）
* 林瀚熙（3120191020）
* 李彤（3120191018）

### 问题描述

#### 1、问题背景及分析

1.1 题目的背景，来源

本题目来自于天池IJCAI-15 Contest。我们知道，国内外的电商有各种各样促销活动，像国外的黑五（Black Friday），国内的双十一等等。大量商家通过打折促销吸引顾客。其中，有许多顾客是被商家的促销所吸引的新顾客，那么他们会不会在促销之后继续在这家店买东西呢？本次比赛题目就是预测这些会重复购买的顾客。

1.2 数据和分析

该数据集包含过去6个月“双11”日之前和当天匿名用户的购物日志，以及标签上是否重复购买的信息。由于隐私问题，数据以偏颇的方式进行采样，因此该数据集的统计结果将偏离天猫的实际数据，但它不会影响解决方案的适用性。该问题和数据集与推荐系统领域的Sequential Recommendation（序列推荐）类似：主要框架为，利用不同的模型（CNN，attention居多，逐渐取代RNN）学习每个user的item序列信息作为其short-term特征，单独的user embedding视作其long-term偏好，两者分开学习，或同时学习，并作最终预测。

#### 2、问题描述

2.1 数据准备

该数据集包含过去6个月“双11”日之前和当天匿名用户的购物日志，以及标签上是否重复购买的信息。由于隐私问题，数据以偏颇的方式进行采样，因此该数据集的统计结果将偏离天猫的实际数据，但它不会影响解决方案的适用性。

2.2 数据描述

**User Behaviour Logs**

| Data Fields | Definition |
| --- | --- |
| user_id | A unique id for the shopper. |
| item_id | A unique id for the item. |
| cat_id | A unique id for the category that the item belongs to. |
| merchant_id | A unique id for the merchant. |
| brand_id | A unique id for the brand of the item. |
| time_tamp | Date the action took place (format: mmdd) |
| action_type | It is an enumerated type {0, 1, 2, 3}, where 0 is for click, 1 is for add-to-cart, 2 is for purchase and 3 is for add-to-favourite. |

**User Profile**

| Data Fields | Definition |
| --- | --- |
| user_id | A unique id for the shopper. |
| age_range | User's age range: 1 for = 50;0 and NULL for unknown. |
| gender | User’ s gender: 0 for female, 1 for male, 2 and NULL for unknown. |

**Training and Testing Data**

| Data Fields | Definition |
| --- | --- |
| user_id | A unique id for the shopper. |
| merchant_id | A unique id for the merchant. |
| label | It is an enumerated type {0, 1}, where 1 means repeat buyer, 0 is for non-repeat buyer. This field is empty for test data. |

2.3 准备采用的方法或模型

* 对数据进行预处理，例如对缺失值进行处理，生成用户的序列数据；
* 挖掘数据集的管理规则，进行特征工程，人工提取一些特征；
* 采用序列推荐模型中的一些神经网络模型，输入序列数据和提取的特征，进行训练和预测

2.4 预期的挖掘结果

* 对于测试集中的用户和商家，预测用户是否会继续在该商家进行购买。

### 项目评估

比赛的评测标准是ROC曲线下面积（AUC），典型的二分类分类器评估标准。在本项目中，我们将采用推荐系统中常用的一些评价指标：如召回率，准确率，AUC来对预测结果进行评估。

### 项目分工

* 周泳宇（3120191079）：数据处理与分析，算法调研与实现，文档撰写
* 邵江逸（3120191038）：数据处理与分析，算法调研
* 周田（3220190931）：数据处理与分析，算法调研
* 林瀚熙（3120191020）：数据处理与分析，结果分析
* 李彤（3120191018）：数据处理与分析，算法实现
