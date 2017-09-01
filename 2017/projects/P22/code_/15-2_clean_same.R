
setwd("F:/数据及程序/chapter15/示例程序")
Data = readLines("./data/meidi_jd.txt",encoding = "UTF-8")
length(Data)
#删除重复值
Data1 = unique(Data)
length(Data1)