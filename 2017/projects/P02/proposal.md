<html lang="en"><head>
    <meta charset="UTF-8">
    <title></title>
<style id="system" type="text/css">h1,h2,h3,h4,h5,h6,p,blockquote {    margin: 0;    padding: 0;}body {    font-family: "Helvetica Neue", Helvetica, "Hiragino Sans GB", Arial, sans-serif;    font-size: 13px;    line-height: 18px;    color: #737373;    margin: 10px 13px 10px 13px;}a {    color: #0069d6;}a:hover {    color: #0050a3;    text-decoration: none;}a img {    border: none;}p {    margin-bottom: 9px;}h1,h2,h3,h4,h5,h6 {    color: #404040;    line-height: 36px;}h1 {    margin-bottom: 18px;    font-size: 30px;}h2 {    font-size: 24px;}h3 {    font-size: 18px;}h4 {    font-size: 16px;}h5 {    font-size: 14px;}h6 {    font-size: 13px;}hr {    margin: 0 0 19px;    border: 0;    border-bottom: 1px solid #ccc;}blockquote {    padding: 13px 13px 21px 15px;    margin-bottom: 18px;    font-family:georgia,serif;    font-style: italic;}blockquote:before {    content:"C";    font-size:40px;    margin-left:-10px;    font-family:georgia,serif;    color:#eee;}blockquote p {    font-size: 14px;    font-weight: 300;    line-height: 18px;    margin-bottom: 0;    font-style: italic;}code, pre {    font-family: Monaco, Andale Mono, Courier New, monospace;}code {    background-color: #fee9cc;    color: rgba(0, 0, 0, 0.75);    padding: 1px 3px;    font-size: 12px;    -webkit-border-radius: 3px;    -moz-border-radius: 3px;    border-radius: 3px;}pre {    display: block;    padding: 14px;    margin: 0 0 18px;    line-height: 16px;    font-size: 11px;    border: 1px solid #d9d9d9;    white-space: pre-wrap;    word-wrap: break-word;}pre code {    background-color: #fff;    color:#737373;    font-size: 11px;    padding: 0;}@media screen and (min-width: 768px) {    body {        width: 748px;        margin:10px auto;    }}</style><style id="custom" type="text/css"></style></head>
<body marginheight="0"><h2>基于聚类算法的高价值目标客户分析—以某航空公司为例</h2>
<h3>成员</h3>
<ul>
<li>石鹏飞</li>
<li>王崛飞</li>
<li>聂玉冰</li>
<li>于大江</li>
<li>孙灿</li>
</ul>
<h2>问题描述</h2>
<h3>1、问题背景分析</h3>
<p>聚类分析以相似性为基础，在一个聚类中的模式之间比不在同一聚类中的模式之间具有更多的相似性。
在商业上，聚类可以帮助市场分析人员从消费者数据库中区分出不同的消费群体来，并且概括出每一类消费者的消费模式或者说习惯。它作为数据挖掘中的一个模块，可以作为一个单独的工具以发现数据库中分布的一些深层的信息，并且概括出每一类的特点，或者把注意力放在某一个特定的类上以作进一步的分析；并且，聚类分析也可以作为数据挖掘算法中其他分析算法的一个预处理步骤。
作为企业的核心问题之一——客户关系管理，其关键是针对不同类别的客户指定与其相对应的个性化服务方案，采取不同的营销策略，将有限资源集中于高价值客户，从而实现利润最大化目标。我们以某航空公司为例，通过采用聚类算法对其客户进行分群，旨在建立合理的客户价值评估模型，并分析不同客户群的特点，提供相对应的商业策略。

</p>
<h3>2、问题描述</h3>
<p>（1）数据预处理：包括数据抽取、对数据进行探索和分析、数据清洗、属性规约等操作；（2）特征工程：分析客户属性间的相关关系，去掉冗余的特征，构建更好反映客户群特点的新特征；（4）模型构建：用K-means聚类算法对客户数据进行分群；（5）依据计算出的LRFMC指标，结合业务对客户做出价值分析。

</p>
<h2>目标</h2>
<p>经过以上步骤，我们得到了用户的分群结果，依据聚类结果我们可以对不同用户进行分析，并制定相对应的营销策略。

</p>
<h2>项目分工</h2>
<ul>
<li>石鹏飞：数据整理和预处理</li>
<li>王崛飞、聂玉冰：算法实现和代码调试</li>
<li>于大江：特征工程</li>
<li>孙灿：数据分析和撰写报告</li>
</ul>
<p>Edit By <a href="http://mahua.jser.me">MaHua</a></p>
</body></html>