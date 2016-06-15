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

### 数据预处理

数据清理后

<div class="fig figcenter fighighlight">
    <a href="image/daily_by_artist.jpg"><img src="image/daily_by_artist.jpg" ></a>
    <div class="figcaption">只提取出用户名和微博内容。</div>
</div>

数据预处理后

<div class="fig figcenter fighighlight">
    <a href="image/daily_by_artist.jpg"><img src="image/daily_by_artist.jpg" ></a>
    <div class="figcaption">包括分词、去停用词。</div>
</div>

### LDA部分实验结果展示

<div class="fig figcenter fighighlight">
    <a href="image/daily_by_artist.jpg"><img src="image/daily_by_artist.jpg" ></a>
    <div class="figcaption">还是有一部分噪音，和短文本的影响。</div>
</div>
