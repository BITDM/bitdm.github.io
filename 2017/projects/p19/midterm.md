---
layout: page
mathjax: true
permalink: /2017/projects/p19/midterm/
---

## 阶段报告

### 项目简介

+ 通过使用过往股票交易数据对模型训练，使它可以对下一天的股票价格进行预测。


### 一、数据清洗

首先需要对从网易财经获得上证综值进行清洗，具体包括：

> 1)填补日期，并对非交易日的数据进行剔除；

> 2)除去股票中不需要的属性；

### 二、模型训练

分为以下几步：

#### 1. 将股票数据标准化，并分为训练集和测试集。

训练集：测试集 = 9：1

标准化公式：

![公式](http://latex.codecogs.com/gif.latex?n_i=\frac{p_i}{p_0}-1)

![公式](http://latex.codecogs.com/gif.latex?n_i) 为处理后数据

![公式](http://latex.codecogs.com/gif.latex?p_i) 为处理前数据

![公式](http://latex.codecogs.com/gif.latex?p_0) 为处理窗口的第一个数据

#### 2. 构建神经网络模型

采用两层LSTM结构，每层LSTM层后接Dropout层用来防治过拟合

第一层输出维度为50，第二层为100

准确率计算公式：

![公式](http://latex.codecogs.com/gif.latex?acc=1-|\frac{y_t-y_p}{y_t+1}|)

损失函数采用的是MSE（均方误差），优化器采用的是RMSProp

#### 3.训练结果

在训练集上迭代500次：

训练集损失图如下：

![图片](https://github.com/lucifer443/bitdm.github.io/blob/master/2017/projects/p19/train_loss.png)

验证集准确率：

![图片](https://github.com/lucifer443/bitdm.github.io/blob/master/2017/projects/p19/val_acc.png)

测试集结果：

![图片](https://github.com/lucifer443/bitdm.github.io/blob/master/2017/projects/p19/test.png)
 

测试集误差：
 
* 误差0.01以内:81.5126%
* 误差0.02以内:96.2185%
* 误差0.05以内:100.0000%
 
### 三、后续工作
 
利用训练好的模型对个股的情况进行预测
