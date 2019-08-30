---
layout: page
mathjax: true
permalink: /2019/projects/p15/final/
---

> 注意: 上方的内容不要删除

## 基于神经网络的个性化电影推荐

### 一、小组成员及分工
- 1 巩卫参：3220180798 数据预处理、文档撰写
- 2 戴云鹏：5720182061 构建模型、训练模型
- 3 赵仁豪：3220180773 模型优化、文档撰写
- 4 肖恩：3220180881 数据可视化、文档撰写


### 二、问题描述
由于个人喜好不同，喜欢的电影风格也就不尽相同，如果能够根据用户喜欢的电影类型，进行个性化的内容推荐，可以给用户带来很好的体验。为了解决这个问题，推荐系统应运而生，其中协同过滤是推荐系统中使用广泛的技术，该方法根据用户的历史记录、个人喜好等信息，计算与其他用户的相似度，利用相似用户的评价来预测目标用户对特定项目的喜欢程度。优点是会给用户推荐未浏览的项目，缺点是对于新用户来说，由于没有任何与商品的交互记录和个人喜好等信息，导致模型无法找到相似的用户或商品。本项目使用文本卷积神经网络，并使用MovieLens数据集完成电影推荐的任务。

### 三、数据集描述
使用MovieLens 1M 数据集， 数据集分为三个文件：用户数据users.dat，电影数据movies.da和评分数据ratings.dat。    
用户数据有用户ID、性别、年龄、职业ID和邮编等，字段如下图所示：  
![](https://github.com/x3e7/bitdm.github.io/blob/master/2019/projects/P15/picture/1.png)  
电影数据有电影ID、电影名和电影风格等，如下图所示：  
![](https://github.com/x3e7/bitdm.github.io/blob/master/2019/projects/P15/picture/2.png)  
评分数据有用户ID、电影ID、评分和时间戳等，如下图所示：    
![](https://github.com/x3e7/bitdm.github.io/blob/master/2019/projects/P15/picture/3.png)  
### 四、评价指标
在对模型的性能进行评价方面，这里采用了均方误差（Mean squared error，MSE）进行评估：
![](https://github.com/x3e7/bitdm.github.io/blob/master/2019/projects/P15/picture/4.png)   
其中，n为样本数量， 为电影的真实评分， 为电影的预测评分。

### 五、模型描述
整个模型大致如下图所示：  
![](https://github.com/x3e7/bitdm.github.io/blob/master/2019/projects/P15/picture/5.png)    
在预处理数据时将数据集中的字段类型转成数字，用这个数字当做嵌入矩阵的索引，在网络的第一层使用嵌入层，电影名的处理用文本卷积网络，从嵌入层索引出特征以后，将各特征传入全连接层，将输出再次传入全连接层，最终分别得到用户特征和电影特征两个特征向量。将两个特征做向量乘法，将结果与真实评分做回归，采用MSE优化损失。  
其中文本卷积网络的内容参考了论文《Convolutional Neural Networks for Sentence Classification》中的CNN模型，如图所示：  
![](https://github.com/x3e7/bitdm.github.io/blob/master/2019/projects/P15/picture/6.png)    
网络的第一层是词嵌入层，由每一个单词的嵌入向量组成的嵌入矩阵。下一层使用多个不同尺寸（窗口大小）的卷积核在嵌入矩阵上做卷积，窗口大小指的是每次卷积覆盖几个单词。这里跟对图像卷积不太一样，图像的卷积通常用2x2、3x3、5x5之类的尺寸，而文本卷积要覆盖整个单词的嵌入向量，所以尺寸是（单词数，向量维度），比如每次滑动3个，4个或者5个单词。第三层网络是max pooling得到一个长向量，最后使用dropout做正则化，最终得到了电影Title的特征。


### 六、实验结果与分析
Training loss  
![](https://github.com/x3e7/bitdm.github.io/blob/master/2019/projects/P15/picture/7.png)   
随着迭代次数的增加，Training loss 减小后开始收敛  
Test loss  
![](https://github.com/x3e7/bitdm.github.io/blob/master/2019/projects/P15/picture/8.png)   
随着迭代次数的增加，Test loss 减小后开始收敛

本文使用文本卷积神经网络，并利用MovieLens数据集完成电影推荐的任务。可以通过指定用户和电影进行评分，并且为用户推荐同类型的电影，用户喜欢的电影，看过这个电影的人还喜欢的其他电影。从实验结果看，本模型可以顺利完成为用户推荐电影的任务，但是推荐的效率还可以进行进一步的提高，未来的工作可以考虑进一步对模型进行优化。
  
 

