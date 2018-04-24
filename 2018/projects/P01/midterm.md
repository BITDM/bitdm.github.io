---
layout: page
mathjax: true
permalink: /2018/projects/p01/midterm/
---

## 项目进展报告

### 数据获取及预处理

首次使用数据为从CSDN上获取的购物篮数据集,总计1000条购买数据,进行模型的简单测试。其后将使用kaggle数据集网站中的Instacart Market Basket Analysis数据集,目前正对该数据集进行预处理,提取出product,aisle和department三类数据集,进行后期对单类商品关系规则及大类商品(如肉类,日用品等)的关系规则挖取。

### 数据分析与可视化

初次使用的数据集部分数据如下所示:

![product.PNG](https://github.com/kangyang94/bitdm.github.io/blob/master/2018/projects/P01/product.PNG)

对于初次使用的数据集,商品频繁集统计支持度如下图所示:

![itemset.png](https://github.com/kangyang94/bitdm.github.io/blob/master/2018/projects/P01/itemset.png)


### 模型选取

经过分析和讨论，决定采用经典算法Aprior算法实现，而Aprior算法的基本思想是首先是找出所有大于最小支持度的频繁项集，然后由频繁项集产生关联规则，这些规则必须满足最小支持度和最小可信度。Apriori算法是用来发现频繁项集的一种方法。Apriori算法的两个输入参数分别是最小支持度和数据集。该算法首先生成所有单个物品的项集列表，遍历之后去掉不满足最小支持度要求的项集；接下来对剩下的集合进行组合生成包含两个元素的项集，去掉不满足最小支持度的项集；重复该过程直到去掉所有不满足最小支持度的项集。

其步骤是：依据支持度找出所有频繁项集（频度），依据置信度产生关联规则（强度），根据最后产生的关联规则，并考虑到利润因素，辅助商家做出商品的营销决策。


### 挖掘实验的结果

本次数据挖掘采用参数为最小支持度等于0.2,最小置信度等于0.8,对于初次的数据集挖掘商品规则如下所示:

![re.png](https://github.com/kangyang94/bitdm.github.io/blob/master/2018/projects/P01/re.png)

关联规则统计置信度如下图所示:

![rule.png](https://github.com/kangyang94/bitdm.github.io/blob/master/2018/projects/P01/rule.png)

### 存在的问题

首次使用的CSDN中的数据集过小，挖取到的关联规则过于简单

### 下一步工作

改用Instacart Market Basket Analysis数据集进行最终实验,并根据数据集对参数进行进一步的调优, 并且在传统的关联规则分析的基础上加上商品分类参考因素，不仅获取商品种类相同时关联规则,还获取相异商品种类间的关联规则, 使得最后产生的营销决策能够使商家在更大程度上获益。
