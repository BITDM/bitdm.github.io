---
layout: page
mathjax: true
permalink: /2019/assignment1/
---

## 数据挖掘大作业一：数据探索性分析与数据预处理

### 1. 问题描述

本次作业中，将选择2个数据集进行探索性分析与预处理。

### 2. 数据说明

可选数据集包括：

- [Consumer & Visitor Insights For Neighborhoods](https://www.kaggle.com/safegraph/visit-patterns-by-census-block-group)
- [Wine Reviews](https://www.kaggle.com/zynicide/wine-reviews)
- [Oakland Crime Statistics 2011 to 2016](https://www.kaggle.com/cityofoakland/oakland-crime-statistics-2011-to-2016)
- [Chicago Building Violations](https://www.kaggle.com/chicago/chicago-building-violations)
- [Trending YouTube Video Statistics](https://www.kaggle.com/datasnaek/youtube-new)
- [Melbourne Airbnb Open Data](https://www.kaggle.com/tylerx/melbourne-airbnb-open-data)
- [MLB Pitch Data 2015-2018](https://www.kaggle.com/pschale/mlb-pitch-data-20152018)

### 3. 数据分析要求

#### 3.1 数据可视化和摘要

##### 数据摘要

- 对标称属性，给出每个可能取值的频数，
- 数值属性，给出最大、最小、均值、中位数、四分位数及缺失值的个数。

##### 数据的可视化

针对数值属性，

- 绘制直方图，用qq图检验其分布是否为正态分布。
- 绘制盒图，对离群值进行识别

#### 3.2 数据缺失的处理

观察数据集中缺失数据，分析其缺失的原因。

分别使用下列四种策略对缺失值进行处理:

- 将缺失部分剔除
- 用最高频率值来填补缺失值
- 通过属性的相关关系来填补缺失值
- 通过数据对象之间的相似性来填补缺失值

处理后，可视化地对比新旧数据集。

### 4. 提交内容

- 分析过程的报告
- 分析程序
- 所选择的数据集在README中说明，相关的数据文件不要上传到Github中

**建议：**使用Jupyter Notebook或R Studio markdown将分析报告和代码组织在一起。