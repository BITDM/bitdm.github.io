---
layout: page
mathjax: true
permalink: /2020/projects/p13/midterm/
---

## 二手车交易价格预测

### 1. 数据获取及预处理

#### 1.1 数据来源

阿里天池比赛，二手车交易价格预测任务，数据来自某交易平台的二手车交易记录。

#### 1.2 数据说明

总数据量超过40w，包含31列变量信息，其中15列为匿名变量。其中抽取15万条作为训练集，5万条作为测试集，同时会对name、model、brand和regionCode等信息进行脱敏。

Tip:匿名特征，就是未告知数据列所属的性质的特征列。

**train.csv**

| Field | Description |
| --- | --- |
| SaleID | 交易ID，唯一编码 |
| name | 汽车交易名称，已脱敏 |
| regDate | 汽车注册日期 |
| model | 车型编码，已脱敏 |
| brand | 汽车品牌，已脱敏 |
| bodyType | 车身类型 |
| fuelType | 燃油类型 |
| gearbox | 变速箱 |
| power | 发动机功率 |
| kilometer | 汽车已行驶公里 |
| notRepairedDamage | 汽车有尚未修复的损坏 |
| regionCode | 地区编码，已脱敏 |
| seller | 销售方 |
| offerType | 报价类型 |
| creatDate | 汽车上线时间 |
| price | 二手车交易价格（预测目标） |
| v系列特征 | 匿名特征，包含v0-14在内15个匿名特征 |

数字全都脱敏处理，都为label encoding形式，即数字形式

#### 1.3 数据预处理

* ‘price’为长尾分布，对该特征进行了处理，更加符合高斯分布
* SaleID为交易ID，肯定没用，但是我们可以用来统计别的特征的group数量
* name为汽车交易名称，已经脱敏一般没什么好挖掘的，不过同名的好像不少，统计了一下同名数据个数，为name_count，然后删除了属性信息‘name’
* 'seller'、'offerType'特征严重倾斜，训练数据中'seller'有一个特殊值，删除了该样本，而且把‘seller’和‘offerType’属性删除了
* 在题目中规定了power范围为[0, 600]，对数据集中power属性进行了修正
* 'notRepairedDamage'属性中'-'应该也是空值，用nan替换
* 对于缺失值，用众数对缺失值进行了填充
* 对于时间属性信息，‘regDates’和‘creatDates’，增添了6列属性，分别为‘regDate_year’、‘regDate_month’、‘regDate_day’、‘creatDate_year’、‘creatDate_month’、‘creatDate_day’

### 2. 数据分析与可视化

#### 2.1 数据分析及可视化过程

* 通过describe()来熟悉训练数据、测试数据数值属性的相关统计量，包括均值，方差，最小值，第1四分位数，中位数，第3四分位数，最大值。
* 通过info()来熟悉数据类型
* 通过可视化方法分析了训练数据、测试数据中的数值属性趋势
* 分析训练数据、测试数据类别特征nunique分布
* 分析训练数据、测试数据缺失值情况
* 对预测属性‘price’ 进行了相关性分析

#### 2.2 数据分析代码及结果

仓库地址：[https://github.com/Zening-Li/BIT_DataMining_project](https://github.com/Zening-Li/BIT_DataMining_project)

**比赛数据集**

* 训练数据：data/used_car_train_20200313.csv

* 测试数据：data/used_car_testB_20200421.csv

* 提交数据：data/used_car_sample_submit.csv

**数据分析及预处理**

* **代码及结果展示：**data_process.ipynb

* 预处理后数据： process_data/train_data_v1.csv，process_data/test_data_v1.csv

### 3. 模型选取

#### 3.1 算法一：线性回归模型

**数据集**

* [训练数据：data/train_data_v1.csv](https://github.com/Zening-Li/BIT_DataMining_project/tree/master/process_data)

* [测试数据：data/test_data_v1.csv](https://github.com/Zening-Li/BIT_DataMining_project/tree/master/process_data)

* [提交数据：output/submit.csv](https://github.com/ZedB/BIT-DataMining-project/blob/master/output)

**代码实现**

[algorithm1_linear_regression.ipynb](https://github.com/ZedB/BIT-DataMining-project/blob/master/algorithm1_linear_regression.ipynb)

**说明**

* 算法1使用的训练模型为线性回归模型，评测标准为MAE(Mean Absolute Error)
* 将数据集data/train_data_v1.csv中的数据拆分为训练集与测试集两部分，进行训练与评测
* 使用数据集data/test_data_v1.csv进行比赛结果预测
* 比赛预测结果按照指定格式生成output/submit.csv文件以便提交

#### 3.2 算法二：回归决策树模型

**数据集**

* [训练数据：data/train_data_v1.csv](https://github.com/Zening-Li/BIT_DataMining_project/tree/master/process_data)
* [测试数据：data/test_data_v1.csv](https://github.com/Zening-Li/BIT_DataMining_project/tree/master/process_data)
* [提交数据：output/submit.csv](https://github.com/ZedB/BIT-DataMining-project/blob/master/output)
* [输出数据：output/algo2_predict.csv](https://github.com/liucc1997/DMC/blob/master/DataMining_project/output/algo2_predict.csv)

**代码实现**

[algorithm2_decision_tree.ipynb](https://github.com/liucc1997/DMC/blob/master/DataMining_project/algorithm2_decision_tree.ipynb)

**说明**

* 使用回归决策树模型
* 训练集中，根据creatDates和creatDates计算得到used_time
* 作为特征的属性包括:

```
["bodyType","brand","fuelType","gearbox","kilometer",'model', 'notRepairedDamage', 'power', 'regDate','v_0'- 'v_9', 'name_count','used_time']
```

* 训练集80%的数据用于训练，20%用于评价模型，使用AE和决定系数R^2评价模型
* 最后使用模型预测测试集，结果保存在```output/algo2_predict.csv```文件中

### 4. 挖掘实验的结果

#### 4.1 算法一：线性回归模型的可视化

##### 4.1.1代码实现

[visual1.ipynb](https://github.com/shl5133/BIT-Data-Mining-assignments/blob/master/project/visual1.ipynb)

##### 4.1.2 可视化过程

* 构建训练和测试数据集，切分数据集（Train, Val）使用线性回归模型进行模型训练，使用MAE标准进行评价，并进行模型预测
* 由于'v_12' ,'v_8', 'v_0'与price相关度较高所以进行可视化观察，可以看到线性回归模型进行预测时对于同属性值的高price和低price预测较差，更倾向于预测为中间大小price
* 绘制模型学习率曲线及验证曲线
* 将预测值生成指定格式的csv文件

#### 4.2 算法二：回归决策树模型的可视化

##### 4.2.1 代码实现

[visual2.ipynb](https://github.com/shl5133/BIT-Data-Mining-assignments/blob/master/project/visual2.ipynb)

##### 4.2.2 可视化过程

* 特征构造，划分训练数据并选择作为特征的属性，同时计算模型使用时间
* 训练模型
* 评价模型，对预测结果计算决定系数​
* 可视化预测误差
* 对模型进行MAE标准评价
* 使用回归模型预测测试集中的数据，并对预测结果进行可视化
* 由于'v_12' ,'v_8', 'v_0'与price相关度较高所以进行可视化观察，可以看到与线性回归模型相比，预测效果是较好的

### 5. 存在的问题

线性回归模型进行预测时对于同属性值的高price和低price预测较差，更倾向于预测为中间大小price，而回归决策树模型虽然预测效果更好一些，但还存在可提升空间。

### 6. 下一步工作

为达到更优的表现，将进行以下几种尝试：

* 对模型的参数进行调试
* 尝试使用其他模型进行建模预测

### 7. 任务分配与完成情况

* 李泽宁：数据分析及预处理，文档编写
* 张博：算法1实现及分析，文档编写
* 刘聪聪：算法2实现及分析，文档编写
* 宋昊霖: 数据可视化，文档编写
* 曹健: 文档整合与编写