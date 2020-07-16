---
layout: page
mathjax: true
permalink: /2020/projects/p15/midterm/
---

## Covid-19 全球性预测

### 1. 数据获取及预处理

#### 1.1 数据来源

数据来源于[Kaggle COVID-19预测项目（COVID19 Global Forecasting (Week 5)](https://www.kaggle.com/c/covid19-global-forecasting-week-5)，数据有训练集和测试集, 在训练集包含969640个样本及9个字段，在测试集上包括311670个样本及8个字段。该项目目的是通过训练集上COVID-19确诊/死亡数据，预测未来各日期在世界各地的已确诊的COVID19病例数量，以及死亡人数。，以及识别出可能影响COVID19传输速率的因素。

#### 1.2 数据说明

训练集，测试集字段相同，各字段说明如下表所示：

```
字段名 说明
ID 数据集样本id
County 县/郡
Province_State 省份/州
Country_Region 国家
Population 人口数
Date 时间
Target 类型（确诊病例，死亡人数）
TargetValue 确诊病例/死亡人数
```

#### 1.3 数据预处理

数据预处理部分包括以下内容：

1. 缺失值检测及处理,字段County和Province_State存在缺失,使用Province_State填充County，使用Country_Region填充Province_State；
2. Country_Region，Target为分类型变量，Target取值为：ConfirmedCases，Fatalities,Country_Region为各国家英文名称，对这两个字段数据进行数据编码，转换为数据型变量。
3. Date字段为时间，转换为整型。

### 2. 数据分析与可视化

数据探索性分析将在数据预处理之后进行。该可视化部分将从地区分布以及各个地区随着时间变化过程中COVID-19确诊数量增长趋势的角度（同样也包括其他一些角度信息）进行分析。所选用的工具主要是Python的pandas库与matplotlib库。

### 3. 模型选取

1. 因为预测全球新冠肺炎感染和死亡人数属于回归问题，因此考虑使用线性回归，随机森林、xgboost方法进行模型预测。
2. 理由如下：

> 通过观察提供的数据，可以发现，该任务属于回归任务。即Country_Region 、Population 、Weight 、Target等若干个自变量对因变量TargetValue的作用。作为回归问题，随机森林结构虽然复杂，但是却极易使用，需要假设的条件要少很多，比如不需要考虑变量的独立性、正态性等。同时也不需要检查变量之间的交互作用和非线性作用。在大多数情况下给以给出接近最有的结果。并且随机森林的学习过程很快，尤其在处理含有较多自变量的海量数据时效率很高。并且对缺失值的不太敏感，即使有一部分数据丢失，仍然可以保持一定的准确率。由于XGBoost处理标准表格型数据的主要模型，因此处理DataFrames中的数据XGBoost比较适合。并且XGBoost处理回归任务同样效果较好。最后，我们也使用了比较简单的线性回归进行预测。

### 4. 挖掘实验的结果

实验发现，RandomForestRegressor、XGBRegressor、LinearRegression三种方法中RandomForestRegressor的效果最好，LinearRegression效果最次。评价指标我们选择的是均方误差mse.并且基于三个模型，在数据集test.csv上对感染人数和死亡人数进行了预测。总体来说，预测效果良好。

其结果如下表所示：

| Model | MSE |
| --- | --- |
| RandomForestRegressor | 1.687 |
| XGBRegressor | 1.766 |
| LinearRegression | 1.833 |

### 5. 存在的问题

无。

### 6. 下一步工作

继续完善当前工作，并开始准备“最终报告”。

### 7. 任务分配与完成情况

任务分配：

* 杜建成：模型构建，模型相关部分文档撰写
* 聂宇翔：模型间对比分析，数据可视化，主要文档撰写
* 陈子康：模型构建，模型相关部分文档撰写
* 赵菊文：模型构建，模型相关部分文档撰写
* 窦京伟：数据收集与预处理，以及相关部分文档撰写‘

完成情况：

* 杜建成：基本上完成模型构建与相关文档撰写
* 聂宇翔：基本上完成开题与中期文档撰写，模型间对比分析与数据可视化尚未开展。
* 陈子康：基本上完成模型构建与相关文档撰写
* 赵菊文：基本上完成模型构建与相关文档撰写
* 窦京伟：基本上完成数据获取和预处理方面的工作，以及相关部分的文档撰写。 