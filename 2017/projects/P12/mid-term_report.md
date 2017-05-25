## 基于协同过滤算法的电影推荐系统及相关电影数据挖掘
### 成员
- 郭强：2120160993
- 尚子钰：2120161034
- 廖晨宇：2120161014

### 问题描述
#### 1.问题背景分析及相关工作
推荐系统是一种信息过滤系统，用于预测用户对物品的“评分”或者“偏好”。推荐系统近年来非常流行，应用于各行各业。推荐的对象包括：电影、音乐、新闻、书籍、学术论文、搜索查询、分众分类以及其他产品。也有一些推荐系统专门为寻找专家、合作者、笑话、餐厅、美食、金融服务、生命保险、网络交友以及twitter页面设计。协同过滤，简单来说就是利用某些兴趣相投、拥有共同经验之群体的喜好来推荐用户感兴趣的信息，个人通过合作的机制给予信息相当程度的回应（如评分，回应不一定局限于特别感兴趣的，特别不感兴趣的信息记录也相当重要）并记录下来以达到过滤的目的，进而帮助别人筛选信息。
#### 2.问题描述
（1）数据预处理。包括对数据进行分析与整理、填补缺失数据、对数值数据进行离散化。（2）挖掘关联信息和相关性信息，挖掘不同性别、年龄的观影者对不同电影的评分倾向性和关联性，挖掘不同性别的观影人群最具差异性评分的50部电影。（3）电影推荐系统。利用协同过滤算法对观影者进行推荐，推荐其最可能想看的电影。于此同时，为新上映电影预测目标观影人群。
### 3.目标
经过实验操作，挖掘电影评分当中蕴含的关联信息和相关性，为观影者推荐适合其的电影。
### 4.完成情况
#### 4.1数据集及数据预处理工作
我们使用movielens提供的一个小型数据集作为本次实验的使用数据。该数据集包含三个文件，movies.dat, users.dat和ratings.dat，分别表示电影信息，用户信息以及用户对电影的评分情况。数据集包含3,883部电影信息，包括电影名称及类型；6,040个用户信息，包含用户的ID，性别，年龄，职业，邮编；1,000,209条评分信息，包含用户ID，电影ID，评分以及时间戳。由于原始数据集使用文本文件形式存放，不利于程序的读取与操作，且由于编码问题，原始数据存在一些乱码，所以首先要进行数据格式转换及预处理。我们使用matlab2016b，将原始数据导入程序，最终以csv格式分行分列存储，一遍python程序的下一步操作。数据格式介绍

![](https://github.com/upTina/bitdm.github.io/blob/master/2017/projects/P12/source/images/original_movies_data.png)             
> 上图为原始数据截图            
![](https://github.com/upTina/bitdm.github.io/blob/master/2017/projects/P12/source/images/movies_data.png)            
> 上图为处理以后的“movies”数据截图，每一列分别表示电影ID，电影名称，电影类型，其中类型可以有多种
![](https://github.com/upTina/bitdm.github.io/blob/master/2017/projects/P12/source/images/users_data.png)              
> 上图为处理后的“users”截图，包含用户的ID，性别，年龄，职业，邮编
![](https://github.com/upTina/bitdm.github.io/blob/master/2017/projects/P12/source/images/ratings.png)               
> 上图为处理后的“ratings”截图，包含用户ID，电影ID，评分以及时间戳
#### 4.2评价最多的前50部电影
对每一部电影获得的评分个数进行排序，得到前50个评分最多的电影。这个指标并不能表示电影获得评价最高，但是却可以告诉我们什么类型的电影最火爆，观众最喜爱观看      
![](https://github.com/upTina/bitdm.github.io/blob/master/2017/projects/P12/source/images/watched_top50(1).png)               
![](https://github.com/upTina/bitdm.github.io/blob/master/2017/projects/P12/source/images/watched_top50(2).png)               
> 获得评价最多的50部电影

#### 4.3评分最高的50部电影
这项指标显示了从开始有评分到现在所有电影里，观众评价最高的前50部电影。这有助于我们知道什么电影是观众真正喜爱的电影。      
![](https://github.com/upTina/bitdm.github.io/blob/master/2017/projects/P12/source/images/ranked_top50(1).png)               
![](https://github.com/upTina/bitdm.github.io/blob/master/2017/projects/P12/source/images/ranked_top50(2).png)               
> 评分最高的50部电影
### 5.下阶段目标
- 电影评分数据挖掘
- 基于协同过滤的电影推荐系统
