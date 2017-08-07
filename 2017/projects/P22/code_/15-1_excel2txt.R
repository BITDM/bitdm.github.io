

setwd("F:/数据及程序/chapter15/示例程序")
Data = read.csv("./data/huizong.csv",header=T,encoding='utf-8')
colnames(Data) = c("x1","x2","x3","x4","x5","x6","x7","x8","x9")
index = which(Data$x5=="美的")
meidi_jd = Data[index,6]
write.table(meidi_jd,"./tmp/meidi_jd.txt",row.names=FALSE)
