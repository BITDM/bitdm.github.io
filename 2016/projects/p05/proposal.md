---
layout: page
mathjax: true
permalink: /2016/projects/p05/proposal/
---

## 基于Expedia公司数据集的旅馆推荐

### 成员

- 李杨
- 魏思杰
- 李苏畅
- 罗伟

### 项目简介

人们在计划旅行时经常遇到选择旅馆的问题。对于每个目的地而言，有成百上千的旅馆可供选择。如何选择到与个人喜好相符合的旅馆是一个难题。我们是选择一个以前住过的有喜欢的甜点的旅馆？还是冒着风险选择一个以前没有住过的有游泳池的旅馆？

Expedia公司希望改进旅馆推荐算法，对每个用户提供个性化的旅馆推荐。这个问题的规模为每个月数百万条记录。

近来，Expedia使用搜索参数改进了他们的旅馆推荐算法，但是没有足够的用户数据进行个性化推荐。所以，他们提供了他们的数据集，在Kaggle平台上发布了竞赛。

### 数据集

#### 数据集介绍

Expedia 提供了大量的用户行为数据。包括了用户在搜索什么，他们如何看待搜索结果（点击还是预定），搜索结果是不是一个旅行计划的一部分。数据是随机选择的，并且不具有对整体数据的代表性。

Expdeia 关注的是用户倾向于预定哪种旅馆类型。Expedia已经通过内部算法构建了旅馆的分类，将价格、用户评价、相距城市中心等因素作为考虑的变量将旅馆进行了聚类。这些旅馆类别将会准确地代表用户将要预测的旅馆类型，这样就避免了有的新旅馆没有历史数据的问题。
比赛的目标就是预测每一个用户将会预定哪一个旅馆类。

训练数据集和测试数据集在时间上是分开的：训练数据集来自2013年和2014年的数据，而测试数据集来自2015年的数据。训练数据包括了日志中的所有用户，包括了点击事件和预定事件，而测试数据集只包括预定事件。

#### 数据集大小

训练数据文件：4.07G

测试数据文件：263M

#### 数据集内容

| Column name | Description | Data type |
| --------------- | ---------- | ----------- |
| date_time | Timestamp | string |
| site_name | ID of the Expedia point of sale (i.e. Expedia.com, Expedia.co.uk, Expedia.co.jp, ...) | int |
| posa_continent | ID of continent associated with site_name | int |
| user_location_country | The ID of the country the customer is located | int |
| user_location_region | The ID of the region the customer is located | int |
| user_location_city | The ID of the city the customer is located | int |
| orig_destination_distance | Physical distance between a hotel and a customer at the time of search. A null means the distance could not be calculated | double |
| user_id | ID of user | int |
| is_mobile | 1 when a user connected from a mobile device, 0 otherwise | tinyint |
| is_package | 1 if the click/booking was generated as a part of a package (i.e. combined with a flight), 0 otherwise | int |
| channel | ID of a marketing channel | int |
| srch_ci | Checkin date | string |
| srch_co | Checkout date | string |
| srch_adults_cnt | The number of adults specified in the hotel room | int |
| srch_children_cnt | The number of (extra occupancy) children specified in the hotel room | int |
| srch_rm_cnt | The number of hotel rooms specified in the search | int |
| srch_destination_id | ID of the destination where the hotel search was performed | int |
| srch_destination_type_id | Type of destination | int |
| hotel_continent | Hotel continent | int |
| hotel_country | Hotel country | int |
| hotel_market | Hotel market | int |
| is_booking | 1 if a booking, 0 if a click | tinyint |
| cnt | Numer of similar events in the context of the same user session | bigint |
| hotel_cluster | ID of a hotel cluster | int
