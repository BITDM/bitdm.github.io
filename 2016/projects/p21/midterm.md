---
layout: page
mathjax: true
permalink: /2016/projects/p21/midterm/
---

## 代码片段分析与标签预测-中期报告

### 成员

- 扶聪
- 廖心怡

### 目前进展

使用爬虫技术从gist.github.com和code.csdn.net两个网站上得到代码数据，对得到的代码进行初步的分析处理，得到代码的一些特性，并将其可视化。同时对两个网站上的数据特征进行对比

### 目前成果

#### 代码片段属性

    特征         gist@GitHub     code@CSDN
    标题            很少          没有
    描述            很少          很多
    标签            没有          很多
    描述语言      英语和其他语言    中文
    来源          用户提交的       网站整合的
    代码片段数量      65k          145k
    用户数量         35k          36k

#### 可视化

<div class="fig figcenter fighighlight">
    <a href="pic/2.png"><img src="pic/2.png" ></a>
    <div class="figcaption">代码大小分布</div>
</div>

<div class="fig figcenter fighighlight">
    <a href="pic/3.png"><img src="pic/3.png" ></a>
    <div class="figcaption">程序员提交的代码片段数目大小</div>
</div>

<div class="fig figcenter fighighlight">
    <a href="pic/4.png"><img src="pic/4.png" ></a>
    <div class="figcaption">不同语言代码分布情况</div>
</div>

<div class="fig figcenter fighighlight">
    <a href="pic/5.png"><img src="pic/5.png" ></a>
    <div class="figcaption">代码片段描述长度</div>
</div>
