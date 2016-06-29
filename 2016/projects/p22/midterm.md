---
layout: page
mathjax: true
permalink: /2016/projects/p22/midterm/
---

## 中期报告

### 当前结果

已搭设实验平台，采集了大量数据，并初步进行了数据分析

### 目标

通过分析能量波形数据，确定key的真值

### 数据处理

1. 搭设能量采集平台，能够记录随机明文数据并采集能量波形数据
2. 通过分析可以看出AES加密的十轮过程有明显的能量变化

### 数据分析过程

1. 获取AES加密第一轮的能量变化波形，明文随机选取，key固定不变
2. 将能量波形进行聚类分析，分成8类
3. 任取一类中的数据，同时进行0~255秘钥猜测，计算出第一轮异或值
4. 在同一类中，异或值差异最小的即可确定Key!即为真值
![](https://github.com/Darkmoon123/DM/blob/master/Sakura%E6%9D%BF%E8%BF%9E%E6%8E%A5%E5%9B%BE2.jpg)

![](https://github.com/Darkmoon123/DM/blob/master/%E7%A4%BA%E6%B3%A2%E5%99%A8+Sakura%E6%9D%BF%E5%AD%90.jpg)

![](https://github.com/Darkmoon123/DM/blob/master/%E5%8E%9F%E5%A7%8B%E6%B3%A2.jpg)
