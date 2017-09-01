
#加载工作空间
library(NLP)
library(tm)
library(slam)
library(wordcloud) 
library(topicmodels)
#R语言环境下的文本可视化及主题分析
setwd("F:/数据及程序/chapter15/示例程序")
Data1 = readLines("./data/meidi_jd_pos_cut.txt",encoding = "UTF-8")
Data2 = readLines("./data/meidi_jd_neg_cut.txt",encoding = "UTF-8")
stopwords <- unlist (readLines("./data/stoplist.txt",encoding = "UTF-8"))
#删除stopwords
removeStopWords = function(x,words) {  
  ret = character(0)
  index <- 1
  it_max <- length(x)
  while (index <= it_max) {
    if (length(words[words == x[index]]) <1) ret <- c(ret,x[index])
    index <- index +1
  }
  ret
}
#删除空格、字母
Data1 = gsub("([a~z])","",Data1)
Data2 = gsub("([a~z])","",Data2)
#删除停用词
sample.words1 <- lapply(Data1, removeStopWords, stopwords)
sample.words2 <- lapply(Data2, removeStopWords, stopwords)
#构建语料库
corpus1 = Corpus(VectorSource(sample.words1))

#建立文档-词条矩阵
sample.dtm1 <- DocumentTermMatrix(corpus1, control = list(wordLengths = c(2, Inf)))

#主题模型分析
Gibbs = LDA(sample.dtm1, k = 3, method = "Gibbs",control = list(seed = 2015, burnin = 1000,thin = 100, iter = 1000))
#最可能的主题文档
Topic1 <- topics(Gibbs, 1)
table(Topic1)
#每个Topic前10个Term
Terms1 <- terms(Gibbs, 10)
Terms1
####负面评价LDA分析
#构建语料库
corpus2 = Corpus(VectorSource(sample.words2))
#建立文档-词条矩阵
sample.dtm2 <- DocumentTermMatrix(corpus2, control = list(wordLengths = c(2, Inf)))
#主题模型分析
library(topicmodels)
Gibbs2 = LDA(sample.dtm2, k = 3, method = "Gibbs",control = list(seed = 2015, burnin = 1000,thin = 100, iter = 1000))
#最可能的主题文档
Topic2 <- topics(Gibbs2, 1)
table(Topic2)
#每个Topic前10个Term
Terms2 <- terms(Gibbs2, 10)
Terms2
