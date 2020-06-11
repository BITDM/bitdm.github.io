---
layout: page
mathjax: true
permalink: /2019/projects/p07/midterm/
---

> 注意: 上方的内容不要删除

## 项目进展报告 

### 数据获取及预处理

初次使用的数据集部分如下所示

![ex2data](https://github.com/zhangcongyao/bitdm.github.io/blob/master/2019/projects/P07/image/ex2data.PNG)

将其中同批次购物整合到一起，组成列表

![ex2result](https://github.com/zhangcongyao/bitdm.github.io/blob/master/2019/projects/P07/image/ex2result.PNG)

### 模型选取

采用经典算法Aprior算法实现，基本思想是首先是找出所有大于最小支持度的频繁项集，然后由频繁项集产生关联规则，这些规则必须满足最小支持度和最小可
信度。Apriori算法的两个输入参数分别是最小支持度和数据集。该算法首先生成所有单个物品的项集列表，遍历之后去掉不满足最小支持度要求的项集；接下
来对剩下的集合进行组合生成包含两个元素的项集，去掉不满足最小支持度的项集；重复该过程直到去掉所有不满足最小支持度的项集。

其步骤是：依据支持度找出所有频繁项集（频度），依据置信度产生关联规则（强度），根据最后产生的关联规则，并考虑到利润因素，辅助商家做出商品的营
销决策。

### 实验结果

在简单测试数据上算法工作良好，如下所示

数据

![ex1data](https://github.com/zhangcongyao/bitdm.github.io/blob/master/2019/projects/P07/image/ex1data.PNG)

结果

![ex1result](https://github.com/zhangcongyao/bitdm.github.io/blob/master/2019/projects/P07/image/ex1result.PNG)

真实数据集（537578行）上算法工作较慢，目前还没有运行结果。通过将数据减少到10行，可得到结果，证明算法无误，但效率较低

![ex3result](https://github.com/zhangcongyao/bitdm.github.io/blob/master/2019/projects/P07/image/ex3result.PNG)

### 存在问题

在大数据集上无法高效工作

### 改进计划

对数据集进行再次预处理，去除对实验结果贡献小的数据，减少无用运算

改进算法，提高运算效率

可视化数据，使结果更直观
