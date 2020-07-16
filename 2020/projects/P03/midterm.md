---
layout: page
mathjax: true
permalink: /2020/projects/p03/midterm/
---

## 大数据职位招聘信息挖掘

### 1. 数据获取及预处理

#### 1.1 数据来源

用scrapy-redis框架对智联招聘网站中的大数据相关职位进行了爬取。爬虫采用分布式双向爬取，分为master-slaver两端。master节点通过将需要爬取的url存放到redis缓存队列来调度各个slaver节点来爬取数据，slaver节点将爬取到的数据写入到数据库。最终爬取到的数据共49248行，13列。

爬虫代码已上传仓库：[爬虫](https://github.com/PluckySaltyfish/DM-Hiring-Information/tree/master/spider)

#### 1.2 数据说明

* `j_name`职位名称
* `c_name`公司名称
* `c_nature`公司性质
* `c_scale`公司规模
* `description`岗位描述(岗位要求)
* `w_place`工作地点
* `w_filed`职位类别
* `w_experience`要求的经验
* `education`要求的学历
* `s_min`最低工资
* `s_max`最高工资
* `vacancies`职位空缺
* `welfare`福利

#### 1.3 数据预处理

##### 1.3.1数据去重

在数据分析过程中，原始数据常常会有一些重复的记录，因此数据去重是必不可少的一个步骤。针对数据集，自定义去重规则，删除重复行并对数据进行整合。

针对所爬取的数据集，将职位名称（j_name）和公司名称（c_name）同时相同的定义为重复数据。

采用drop_duplicate方法对数据进行去重，drop_duplicate方法是针对DataFrame格式的数据去除特定列下面的重复行，参数解释如下：

```python
DataFrame.drop_duplicates(subset=None, keep='first', inplace=False)
subset：列名，默认所有列
keep：keep= 'first' 表示去重时每组重复数据保留第一条数据，其余数据丢弃；keep='last' 表示去重时每组重复数据保留最后一条数据，其余数据丢弃；keep=False 表示去重时每组重复数据全部丢弃，不保留
inplace: inplace=False表示去重之后不覆盖原表格数据，inplace=True表示去重之后原表格数据被覆盖
```

代码如下：

```python
path='D:\\BIT\\Course\\数据挖掘\\大作业\\1.csv'
f=open(path,encoding='UTF-8')
df=pd.read_csv(f)
print(df.shape[0])#原始数据量输出
df.drop_duplicates(subset=['j_name','c_name'],keep='first',inplace=True)
print(df.shape[0])#去重后数据量输出
```

处理前数据量为49248行，13列；去重后数据量为39397行，13列。

##### 1.3.2 数据去噪

实际数据是数据挖掘算法的输入，它受多个组件的影响。其中，噪声的存在是关键因素。噪声是不可避免的问题，它会影响数据挖掘应用程序中经常发生错误的数据收集和数据准备过程。噪声有两个主要来源：隐式错误由测量工具引入；以及批处理或专家在收集数据时引入的随机错误。

针对所爬取的数据集进行分析，可看出数据集中包含了许多非大数据相关职业的数据。我们采取自定义筛选规则，将不符合要求的数据筛选掉。主要对属性职位名称（j_name）和职位类别（w_field)进行筛选，筛选掉含有某些字段的数据（例如含有字段：软件测试，销售，运营，商务等），最后进行数据整合。

使用pandas数据包中自带函数，筛选掉含有特殊字段的数据，再筛选后的数据合并起来。

伪代码如下：

```python
#不选取J_name中含有某些字段的数据行
df=df[~ df['j_name'].str.contains('软件测试|化工|扫描仪|实施|信息|测试|合伙人|售前|运维|电销|销售|律师|专员|机械|土木|商务|链家|运营|新媒体|岗位|教学|教务|整形|美容|微信|web|前端|行政|司机|助理|设计|策划|文案|架构')]
#不选取j_name为某些字段的数据行
df=df[~df['j_name'].isin(['软件工程师','高级软件工程师'])]
#选取j_name大于四个字的数据行
df=df[df['j_name'].str.len()>4]
#不选取w_field中含有某些字段的数据行
df=df[~ df['w_field'].str.contains('测试|售前|运维|合伙人|电销|销售|律师|专员|机械|土木|商务|链家|运营|新媒体|岗位|教学|教务|整形|美容|微信|web|前端|行政|司机|助理|设计|策划|文案|架构',na=False)]
print(df.shape[0])#去噪后数据量输出
```

去噪前数据量为39397行，13列，去噪后数据量为19872行，13列。

##### 1.3.3 缺失值处理

数据值缺失是数据分析中经常遇到的问题之一，当缺失比例很小时，可直接对缺失记录进行舍弃或进行手工处理。但在实际数据中，往往缺失数据占有相当的比重。这时如果手工处理非常低效，如果舍弃缺失记录，则会丢失大量信息，使不完全观测数据与完全观测数据间产生系统差异，对这样的数据进行分析，你很可能会得出错误的结论。

针对去噪后数据集进行缺失值统计，其中没有分层的数值属性（s_min,s_max,vacancies）中出现的非数字项（如“面议”，“若干”）视为缺失值。统计结果如下：

| 属性 | 缺失值个数 |
| --- | --- |
| j_name | 0 |
| c_name | 14 |
| c_nature | 5933 |
| c_scale | 5850 |
| description | 5796 |
| w_place | 0 |
| w_field | 2 |
| w_experience | 0 |
| education | 0 |
| s_min | 639 |
| s_max | 639 |
| vacancies | 5952 |
| welfare | 7532 |

接下来需要分别对以上属性进行缺失值处理。

* s_min，s_max，vacancies

    对于这三个属性，首先将属性转换成float类型，采用最高频率值填补缺失值。

    以s_min为例：

```python
df['s_min']=pd.to_numeric(df['s_min'],errors='coerce')
df['s_min']=df['s_min'].fillna(stats.mode(df['s_min'])[0][0])
```

* c_name

    对于c_name属性缺失的数据行直接删除。

```python
df=df.dropna(subset=['c_name'])
```

* description

    对于description属性缺失的数据行采用该行j_name进行填补。

```python
for index,row in df.iterrows():
     if row['description'] is np.NaN:
       df.at[index,'description']=row['j_name']
```

* c_nature，c_scale，welfare

    c_nature，c_scale，welfare利用数据属性的相关性填补。即用拥有同一其它属性的行的这列的值填补，比如A公司的两条数据i1，i2。i1缺少福利描述，由于i2的公司和i1的公司相同，将i2的福利描述填入i1。

```python
for index,row in df.iterrows():
     if row['welfare'] is np.NaN:
     flag=0
     df1=df.loc[df['c_name']==row['c_name']]
     for index1,row1 in df1.iterrows():
       if row1['welfare'] is np.NaN:
         continue
     else:
       df.at[index,'welfare']=row1['welfare']
     flag=1
     break
```

目前的预处理代码已上传仓库：[预处理](https://github.com/PluckySaltyfish/DM-Hiring-Information/tree/master/preprocess)

### 2\. 数据分析与可视化

目前的代码已上传仓库：[可视化](https://github.com/PluckySaltyfish/DM-Hiring-Information/tree/master/preprocess)

#### 2.1 分词

首先对属性岗位描述(岗位要求)(description)进行粗粒度的分词，并将分词结果保存。在此调用腾讯[TexSmart HTTP API](https://ai.tencent.com/ailab/nlp/texsmart/zh/api.html)进行粗粒度分词。

```python
#调用api获取结果object
def request_texSmart(obj):
 req_str = json.dumps(obj).encode()
 url = 'https://texsmart.qq.com/api'
 r = requests.post(url, data=req_str)
 r.encoding = 'utf-8'
 return json.loads(r.text)
#从object中抽取出粗粒度的分词结果
def generate_segment_info(obj):
 seg_sent = [seg_obj['str'] for seg_obj in obj['phrase_list']]
 return ','.join(str(seg) for seg in seg_sent), seg_sent

if __name__ == '__main__':
 #对数据集中的每一个description都进行分词
 for i in range(len(df)):
 add_sentence_to_request_obj(df.loc[i, 'description'])
 seg_description, seg_lst = generate_segment_info(request_texSmart(request_obj))
 df.loc[i, 'description'] = seg_description
 seg_words += seg_lst
```

#### 2.2 词云生成

对分词后的description和welfare进行词云生成。


```python
def generate_word_cloud(seg_words, res_path):
 #设置停用词
 stop_words = set(load_file('segment/result/stop_words.txt'))
 #获取分词文本
 text = ' '.join(str(seg) for seg in seg_words)
 #词云生成
 image = Image.open('word_cloud/background.png')
 graph = np.array(image)
 wc = WordCloud(font_path='word_cloud/Songti.ttc', background_color='White', max_words=50, mask=graph, stopwords=stop_words, collocations=False)
 wc.generate(text)
 image_color = ImageColorGenerator(graph)
 plt.imshow(wc)
 plt.imshow(wc.recolor(color_func=image_color))
 plt.axis("off")
 plt.show()
 wc.to_file(res_path)
```

* 岗位描述(岗位要求)`description`词云生成：

```python
segment_words = load_file('segment/result/seg_words.txt')
generate_word_cloud(segment_words, 'word_cloud/result/description.png')
```

<div class="fig figcenter fighighlight">
  <a href="/2020/projects/P03/midterm/images/1.png"><img src="/2020/projects/P03/midterm/images/1.png" ></a>
</div>

* 福利`welfare`词云生成：

```python
df = pd.read_csv('../data/去噪声后数据.csv')
segment_words = df['welfare'].dropna().to_list()
generate_word_cloud(segment_words, 'word_cloud/result/welfare.png')
```

<div class="fig figcenter fighighlight">
    <a href="/2020/projects/P03/midterm/images/2.png"><img src="/2020/projects/P03/midterm/images/2.png" ></a>
</div>

### 3. 模型选取

本项目建立的模型能通过求职者的基本信息(渴望薪资、学历、工作经验等)，生成可求职企业的基本画像。该功能可以帮助各招聘门户网站完善其求职搜索功能，在用户进行搜索后迅速缩小适合企业的范围，进行更加迅速有效的职位推荐。

该问题的本质是多标签分类问题。

#### 3.1 输入输出

* 输入
  * 最低工资
  * 最高工资
  * 经验
  * 学历
  * 工作地点
* 输出
  * 公司性质
  * 公司规模

#### 3.2 数据集划分

数据集一共有19872条数据，将数据集按照`4:1`的比例进行训练集与测试集的划分。

#### 3.3 拟采用的模型

拟采用多层的CNN与LSTM进行模型训练，最后一层使用sigmoid函数进行预测，训练阶段使用binary_crossentropy作为损失函数。

#### 3.4 评估方法

使用精确率(Precision)、召回率(Recall)和 F 值(F-measure)来进行结果的评估。

### 4. 挖掘实验的结果

待预处理完成之后，再进行挖掘工作，将对不同城市、不同企业等对大数据岗位待遇的影响进行挖掘。

### 5. 存在的问题

* 预处理时噪声太大，处理得不知道干不干净
* 模型选择需要进一步的实验确定是否合适

### 6. 下一步工作

下一步将继续完善之前的工作，展开关联挖掘的实验，对数据进行进一步的可视化，完成最终报告。

### 7. 任务分配与完成情况

* 爬虫(唐雨馨) - 已完成
* 数据预处理(黄宇婷、邬成浩) - 部分完成
* 数据分析与关联挖掘 （徐园、李杨晓、唐雨馨）- 进行中
* 数据可视化(邬成浩、唐雨馨) - 进行中
* 模型建立(邬成浩) - 部分完成
* 报告撰写(全员) - 部分完成
