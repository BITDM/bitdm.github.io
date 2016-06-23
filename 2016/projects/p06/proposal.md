---
layout: page
mathjax: true
permalink: /2016/projects/p06/proposal/
---

## N-gram based input text predictor

### 成员

- 钱钧

### 项目描述
  使用 amazon web services 上的 google books ngram 数据集做一个输入预测工具

### 数据集

  aws 上的 google books ngram data

### 处理步骤
  
  1.配置与搭建aws环境
  2.在aws上创建emr集群
  3.使用apache hive在集群上创建要查询的数据库
  4.尝试用本地command line命令连接集群并查询
  5.写本地web客户端页面，尝试用aws java api连接集群
  6.整合完成项目

### 项目难点

  1.集群的搭建
  2.集群的连接查询
  3.使用java api


