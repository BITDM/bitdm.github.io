---
layout: page
mathjax: true
permalink: /2019/projects/p07/midterm/
---

> 注意: 上方的内容不要删除

## 最终报告 

### 背景分析

当今社会已经步入大数据时代，如何更好的利用信息，如何从海量数据中发现知识创造价值是人类面对的一个重要课题。由于庞大的客流量，商家往往不能及时
根据累计的顾客购物信息获取有效的研究信息。本次实验的研究重点在于发现顾客购买不同商品之间的关联，分析顾客的购物习惯，从而帮助商家开发更好的营
销策略。

### 问题描述

数据集是取自Kaggle的Black Friday，来源于Analytics Vidhya举办的竞赛，内容为零售商店中进行交易的条款，还包含了部分顾客信息。
拟采用Aprior算法实现，基本思想是首先是找出所有大于最小支持度的频繁项集，然后由频繁项集产生关联规则，这些规则必须满足最小支持度和最小可信度。
希望通过频繁模式挖掘了解顾客的购物习惯，提出有助于商品销售的摆放方式。

### 模型选取

采用经典算法Aprior算法实现，基本思想是首先是找出所有大于最小支持度的频繁项集，然后由频繁项集产生关联规则，这些规则必须满足最小支持度和最小可
信度。Apriori算法的两个输入参数分别是最小支持度和数据集。该算法首先生成所有单个物品的项集列表，遍历之后去掉不满足最小支持度要求的项集；接下
来对剩下的集合进行组合生成包含两个元素的项集，去掉不满足最小支持度的项集；重复该过程直到去掉所有不满足最小支持度的项集。

其步骤是：依据支持度找出所有频繁项集（频度），依据置信度产生关联规则（强度），根据最后产生的关联规则，并考虑到利润因素，辅助商家做出商品的营
销决策。

### 数据获取及预处理

初次使用的数据集部分如下所示

![ex2data](https://github.com/zhangcongyao/bitdm.github.io/blob/master/2019/projects/P07/image/ex2data.PNG)

将其中同批次购物整合到一起，组成列表

![ex2result](https://github.com/zhangcongyao/bitdm.github.io/blob/master/2019/projects/P07/image/ex2result.PNG)

### 实验结果

在简单测试数据上算法工作良好，如下所示

数据

![ex1data](https://github.com/zhangcongyao/bitdm.github.io/blob/master/2019/projects/P07/image/ex1data.PNG)

结果

![ex1result](https://github.com/zhangcongyao/bitdm.github.io/blob/master/2019/projects/P07/image/ex1result.PNG)

真实数据集（537578行）上由于产品种类过多，算法工作较慢，目前还没有运行结果。通过将数据减少到10行，可得到结果，证明算法无误，但效率较低

![ex3result](https://github.com/zhangcongyao/bitdm.github.io/blob/master/2019/projects/P07/image/ex3result.PNG)

### 总结

虽然在产品种类过多的大数据集上无法高效工作，但通过频繁挖掘找出产品之间的关系是可行的。数据挖掘技术将为管理者提供更理性可靠的依据，从而提高企
业竞争力，获得更大的利益。
