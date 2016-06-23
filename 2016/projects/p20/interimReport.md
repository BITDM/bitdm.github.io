---
layout: page
mathjax: true
permalink: /2016/projects/p20/midterm/
---

## 进度报告

### 成员

* 唐育洋
* 敖权
* 付升宇

### 目前进展

对下载的数据进行处理，可视化分析数据，选择一个模型预测结果

### 数据解释

本次实验数据涉及到两个表，分别代表着歌曲与艺人的关系数据和用户操作歌曲的行为数据。

歌曲数据表如下：

列名|类型|说明
---|---|---
|song_id|String|歌曲唯一标识
|artist_id|String|歌曲所属的艺人Id
|publish_time|String|歌曲发行时间，精确到天
|song\_init\_plays|String|歌曲的初始播放数，表明该歌曲的初始热度
|Language|String|数字表示1,2,3…
|Gender|String|1,2,3,代表男、女、乐队

行为数据表如下：

列名|类型|说明
---|---|---
user_id|String|用户唯一标识
song_id|String|歌曲唯一标识
gmt_create|String|用户播放时间（unix时间戳表示）精确到小时
action_type|String|行为类型：1，播放；2，下载，3，收藏
Ds|String|记录收集日（分区）

本次数据包括100个艺人，超过26000首歌曲，15000000条用户行为记录，行为记录为2015.3.1到2015.8.30，需要预测这100位艺人在接下来的两个月里每一天的播放量，输出表格式和举例如下：

|列名|类型|说明|示例
---|---|---|---
|artist_id|String|歌曲所属的艺人Id|023406156015ef87f99521f3b343f71f
|Plays|String|艺人当天的播放数据|5000
|Ds|String|日期|20150901


### 预处理

由于需要按照艺人进行分别预测，因此考虑了将下载的用户行为数据按照歌曲对应的艺人进行分割得到100个子文件，分别进行处理；对于每一个艺人，可以得到与他相关音乐六个月的播放、下载、收藏数量；此外，我们也考虑每天不同时间的播放影响，按照小时对每个艺人进行了处理。

### 可视化

将上述得到的文件，利用python的matplotlib库进行可视化。例如如下三个例子的可视化：

<div class="fig figcenter fighighlight">
    <a href="https://github.com/SparkFour/datamining_homework/blob/master/homework_project/original/b15e8846dc61824c1242a6b36796117b.jpg?raw=true"><img src="https://github.com/SparkFour/datamining_homework/blob/master/homework_project/original/b15e8846dc61824c1242a6b36796117b.jpg?raw=true" width="30%"></a>
    <a href="https://github.com/SparkFour/datamining_homework/blob/master/homework_project/original/b7522cc91cf57ada15de2298bfd6a3ee.jpg?raw=true"><img src="https://github.com/SparkFour/datamining_homework/blob/master/homework_project/original/b7522cc91cf57ada15de2298bfd6a3ee.jpg?raw=true" width="30%"></a>
    <a href="https://github.com/SparkFour/datamining_homework/blob/master/homework_project/original/b79593426f5360c38beacd2a940b5f22.jpg?raw=true"><img src="https://github.com/SparkFour/datamining_homework/blob/master/homework_project/original/b79593426f5360c38beacd2a940b5f22.jpg?raw=true" width="30%"></a>
</div>

### 预测

根据这个场景，我们首先想到的是时间序列模型，因此我们查阅了相关资料，了解到时间序列模型预测常用的方法包括：AR、MA、ARIMA、STL分解等方法。这里，我们采用R语言里的STL分解进行预测分析。STL分解算法将时间序列分解为三个分量，分别为：趋势项、季节项、残余项。在应用STL分解算法之前，需要对序列预处理得到平稳序列，在这里，我们可以简单理解为序列的均值没有系统的变化（无趋势）、方差没有系统变化，消除了周期性变化。通过对序列做差分操作可以得到平稳序列。

例如，

<div class="fig figcenter fighighlight">
    <a href="https://github.com/SparkFour/datamining_homework/blob/master/homework_project/timeseries.png?raw=true"><img src="https://github.com/SparkFour/datamining_homework/blob/master/homework_project/timeseries.png?raw=true" width="40%"></a>
    <a href="https://github.com/SparkFour/datamining_homework/blob/master/homework_project/timeseries_diff.png?raw=true"><img src="https://github.com/SparkFour/datamining_homework/blob/master/homework_project/timeseries_diff.png?raw=true" width="40%"></a>
    <div class="figcaption">左图是不平稳的时间序列; 对上面的序列做一阶差分后，得到如下的序列，它就可以认为是平稳序列</div>
</div>


是上面三个例子，我们得到的预测为：

<div class="fig figcenter fighighlight">
    <a href="https://github.com/SparkFour/datamining_homework/blob/master/homework_project/predict_stl/b15e8846dc61824c1242a6b36796117b.jpg?raw=true"><img src="https://github.com/SparkFour/datamining_homework/blob/master/homework_project/predict_stl/b15e8846dc61824c1242a6b36796117b.jpg?raw=true" width="30%"></a>
    <a href="https://github.com/SparkFour/datamining_homework/blob/master/homework_project/predict_stl/b7522cc91cf57ada15de2298bfd6a3ee.jpg?raw=true"><img src="https://github.com/SparkFour/datamining_homework/blob/master/homework_project/predict_stl/b7522cc91cf57ada15de2298bfd6a3ee.jpg?raw=true" width="30%"></a>
    <a href="https://github.com/SparkFour/datamining_homework/blob/master/homework_project/predict_stl/b79593426f5360c38beacd2a940b5f22.jpg?raw=true"><img src="https://github.com/SparkFour/datamining_homework/blob/master/homework_project/predict_stl/b79593426f5360c38beacd2a940b5f22.jpg?raw=true" width="30%"></a>
</div>

### 下一步工作内容

对当前预测进行优化，由于目前仅仅用到了部分信息，因此还可以利用其他很多信息来优化。此外，可以尝试使用神经网络等算法进行预测，看是否可以得到更好的效果。


