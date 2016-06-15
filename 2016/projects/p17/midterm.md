---
layout: page
mathjax: true
permalink: /2016/projects/p17/midterm/
---

## 微博 主题 抽取-中期报告

### 成员

- 魏林静
- 王丹
- 李克南
- 郭一迪

### 当前成果

用数据爬虫技术从新浪微博上面抓取微博文本内容。

对抓取的数据进行预处理，主要包括数据清理、分词、去停用词等

利用LDA模型对微博主题进行抽取。


### 目标

对当前的结果进行改进，从两方面
- 短文本
- 噪声

### 数据处理

比赛中使用了两个数据表：用户行为表和歌曲信息表。结构如下：

用户行为表（mars_tianchi_user_actions，1.4G）

| name | data_type | describe | example |
| ------ | ----------- | --------- | ---------- |
| user_id | String | 用户唯一标识 | 7063b3d0c075a4d276c5f06f4327cf4a |
| song_id | String | 歌曲唯一标识 | effb071415be51f11e845884e67c0f8c |
| gmt_create | String | 用户播放时间（unix时间戳表示）精确到小时 | 1426406400 |
| action_type | String | 行为类型：1，播放；2，下载，3，收藏 | 1 |
| Ds | String | 记录收集日（分区） | 20150315 |

歌曲信息（mars_tianchi_songs，2.2M）

| name | data_type | describe | example |
| ------ | ----------- | --------- | ---------- |
| song_id | String | 歌曲唯一标识 | c81f89cf7edd24930641afa2e411b09c |
| artist_id | String | 歌曲所属的艺人Id | 03c6699ea836decbc5c8fc2dbae7bd3b |
| publish_time | String | 歌曲发行时间，精确到天 | 20150325 |
| song_init_plays | String | 歌曲的初始播放数，表明该歌曲的初始热度 | 0 |
| Language | String | 数字表示1,2,3… | 100 |
| Gender | String | 1,2,3 | 1 |

由于原始数据是类似log信息的条目，为了避免后续重复统计，需要先统计每天的播放量。这里我们使用了两个维度的统计角度：从歌曲角度统计和歌手角度统计。得到每日播放量的数据：

| name | data_type | describe | example |
| ---- | --------- | -------- | ------- |
| artist_id/song_id | string | 歌手ID/歌曲ID | 8fb3cef29f2c266af4c9ecef3b780e97|
| date | int | 日期 | 20150301 |
| play | int | 播放量 | 102 |
| download | int | 下载量 | 23 |
| like | int | 收藏量 | 4 |

### 数据分析

首先，我们将100个需要进行预测的歌手的历史播放量数据绘制曲线图，观察每个歌手的历史趋势和特征（图中绿色的圆点代表当天歌手发行了新歌）。

<div class="fig figcenter fighighlight">
    <a href="image/daily_by_artist.jpg"><img src="image/daily_by_artist.jpg" ></a>
    <div class="figcaption">歌曲播放量曲线,从这个大图中可以看到新歌发布会带来大量的播放量，同时每个歌手的播放量相差很大。</div>
</div>

### 模型探索

我们尝试对歌手的播放量进行趋势预测

<div class="fig figcenter fighighlight">
    <a href="image/predict1.jpg"><img src="image/predict1.jpg" width="40%"></a>
    <a href="image/predict2.jpg"><img src="image/predict2.jpg" width="48%"></a>
    <div class="figcaption"></div>
</div>
