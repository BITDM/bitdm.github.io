
#把“数据及程序”文件夹拷贝到F盘下，再用setwd设置工作空间
setwd("F:/数据及程序/chapter15/示例程序")
#读入数据
Data1 = readLines("./data/meidi_jd_process_end_负面情感结果.txt",encoding = "UTF-8")
Data2 = readLines("./data/meidi_jd_process_end_正面情感结果.txt",encoding = "UTF-8")

for (i in 1:length(Data1))
  {
Data1[i] = unlist(strsplit(Data1[i], "\\t"))[2]
}
for (i in 1:length(Data2))
{
  Data2[i] = unlist(strsplit(Data2[i], "\\t"))[2]
}
write.table(Data1,"./tmp/meidi_jd_neg.txt",row.names=FALSE)
write.table(Data2,"./tmp/meidi_jd_pos.txt",row.names=FALSE)
