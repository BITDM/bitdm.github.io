---
layout: page
mathjax: true
permalink: /projects/p17/proposal/
---

## 微博主题提取

### 成员

- 魏林静	2120151045
- 王丹	2120151036
- 李克南	2120151004
- 郭一迪	2120150985


### 参考  

Sources: spam detection dataset, full 20 Newsgroups dataset. With help from Jason Cho and Yanglei Song
The goal of this part of the assignment is classification of text documents. You will be using the following two datasets:

Spam detection
Eight newsgroups
Each dataset contains training and test documents that have already been preprocessed into a "bag of words" representation. Each line of the training and test files has the following format:
[label] [word1]:[count1] [word2]:[count2] ... [wordn]:[countn]

The email dataset contains 700 training documents and 260 test documents. Label of 0 denotes normal email, while 1 denotes spam. The newsgroups dataset contains 1900 training and 263 test documents, and the numeric class labels correspond to the following categories:

sci.space
comp.sys.ibm.pc.hardware
rec.sport.baseball
comp.windows.x
talk.politics.misc
misc.forsale
rec.sport.hockey
comp.graphics


For each dataset, train a Naive Bayes classifier on the training data and then apply it to the test data to predict the category labels of the test documents. In order to do this, you will first need to create dictionaries consisting of all unique words occurring in the training documents, and then estimate conditional probability tables over these dictionaries for each class. Be sure to use Laplace smoothing. Note that there will be words in the test documents that do not occur in the dictionary; simply ignore those.

As in Part 1.1, report your classification rate on the test documents for each class, as well as the confusion matrix. You should be able to get over 90% accuracy on the email dataset, and over 80% on the newsgroup dataset. Additionally, for each class, report the top 20 words with the highest likelihood. Finally, as in Part 1.1, take the pair of classes from the email dataset and four highest-confusion pairs from the newsgroup dataset, and display the top 20 words with the highest log-odds ratio for that pair of classes.
