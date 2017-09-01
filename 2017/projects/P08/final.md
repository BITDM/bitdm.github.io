---
layout: page
mathjax: true
permalink: /2017/projects/p08/final/
---


## 乳腺癌病症的分析——挖掘中医证素与乳腺癌TNM分期之间的关系 

### 成员

- 康丽琪：2120161006
- 马俊：2120161022
- 王阳：2120161060
- 张天夫：2120161079

### 1. 问题描述

乳腺癌是由乳房组织发展成的癌症。中医药物治疗乳腺癌具有广泛的适应症和独特的优势。从整体出发，调整机体气压、阴阳、肺腑功能的平衡，根据不同的临床病症进行辨证论治。确定“先症而治”的方向：即在后续症状未出现之前，需要截断恶化病情的后续症状。发现中医症状间的关联关系和诸多症状之间的规律性，可以根据规则分析病因、预测病情的发展以及为未来临床提供有效借鉴。

目前，中医的治疗一般采用中医辩证的原则，结合临床医师的经验和临床指南进行诊断，然而这种方法也存在一定的缺陷。面对临床不同症状的患者，初学者难以判断。面对中医的缺陷，随着数据挖掘技术的发展，我们可以用数据挖掘技术对数据进行分析，得到中医症素与乳腺癌TNM分期之间的关系，从而有助于中医对乳腺癌的治疗。

### 2. 目标

经过以下步骤：

（1） 数据预处理。包括对数据进行分析与整理、填补缺失数据、对数值数据进行离散化。 （2） 挖掘频繁模式、关联和相关性。利用Apriori算法和FP-tree算法进行关联信息挖掘。 （3） 过滤关联规则，根据决策树分析结果。

找到满足最小支持度和置信度的有用的关联规则，从而推断出中医症素与乳腺癌TNM分期之间的关系，弥补中医临床医师经验的缺陷。

### 3. 步骤

### 3.1	数据预处理

通过对所给数据的分析，得出：肝气郁结证型系数、热毒蕴结证型系数、冲任失调证型系数、气血两虚证型系数、脾胃虚弱证型系数、肝肾阴虚证型系数均为数值类型的数据，而病程阶段、TNM 分期、转移部位、确诊后几年发现转移均为标称类型的数据。观察数据发现，每一个属性的数据当中均存在缺失值。因此我们首先对缺失数据进行填补。

对于数值型数据填补，我们采用属性的中心度量填充缺失值。对每个属性的数据进行分析，对于对称分布的数据，用均值来填充，而对于倾斜数据，则用中位数来填充。

根据分析发现，肝气郁结证型系数、冲任失调证型系数、气血两虚证型系数、脾胃虚弱证型系数、肝肾阴虚证型系数均用均值来填补空缺值。而热毒蕴结证型系数的空值则需要用中位数来替换。

由于Apriori 算法无法处理连续型数值变量，还需要对数据进行规约，也就是对每个属性的数据进行离散化，使用一个标签来对应一个区间。在这里采用无监督学习的方法对数据进行离散化，所使用的算法是K-means。将各属性进行聚类然后进行离散化处理，使得每一个数据有一个对应的标签。分类结果如图：
肝气郁结证型系数：

![](https://github.com/mrkingsun/bitdm.github.io/blob/master/2017/projects/P08/images/%E8%82%9D%E6%B0%94%E9%83%81%E7%BB%93%E8%AF%81%E5%9E%8B%E7%B3%BB%E6%95%B0.png)   

热毒蕴结证型系数：

![](https://github.com/mrkingsun/bitdm.github.io/blob/master/2017/projects/P08/images/%E7%83%AD%E6%AF%92%E8%95%B4%E7%BB%93%E8%AF%81%E5%9E%8B%E7%B3%BB%E6%95%B0.png)   

冲任失调证型系数： 

![](https://github.com/mrkingsun/bitdm.github.io/blob/master/2017/projects/P08/images/%E5%86%B2%E4%BB%BB%E5%A4%B1%E8%B0%83%E8%AF%81%E5%9E%8B%E7%B3%BB%E6%95%B0.png)   

气血两虚证型系数： 

![](https://github.com/mrkingsun/bitdm.github.io/blob/master/2017/projects/P08/images/%E6%B0%94%E8%A1%80%E4%B8%A4%E8%99%9A%E8%AF%81%E5%9E%8B%E7%B3%BB%E6%95%B0.png)   

脾胃虚弱证型系数：

![](https://github.com/mrkingsun/bitdm.github.io/blob/master/2017/projects/P08/images/%E8%84%BE%E8%83%83%E8%99%9A%E5%BC%B1%E8%AF%81%E5%9E%8B%E7%B3%BB%E6%95%B0.png)   

肝肾阴虚证型系数：

![](https://github.com/mrkingsun/bitdm.github.io/blob/master/2017/projects/P08/images/%E8%82%9D%E8%82%BE%E9%98%B4%E8%99%9A%E8%AF%81%E5%9E%8B%E7%B3%BB%E6%95%B0.png)   

对于标称属性的数据，其每个值可以看作是一个类标号，利用经过离散化后的数据来对空缺值进行预测。  
例如，填 TNM 分期的空缺值，则每条记录的类标号就是其对应的 TNM 分期的属性值，找到空缺的记录，根据贝叶斯方法对其进行预测：

![](https://github.com/mrkingsun/bitdm.github.io/blob/master/2017/projects/P08/images/eg.png)   

P(X| TNM 分期=H1)= P(肝气郁结证型系数=A2|TNM 分期=H1)×P(热毒蕴结证型系数=B1|TNM 分期=H1) ×P(冲任失调证型系数=C2|TNM 分期=H1)×P(气血两虚证型系数=D3|TNM 分期=H1)×P(脾胃虚弱证型系数=E3|TNM 分期=H1)×P(脾胃虚弱证型系数=F3|TNM 分期=H1)

同理，计算出P(X| TNM 分期=H2)、P(X| TNM 分期=H3)和P(X| TNM 分期=H4)，取概率最大值对应的TNM 分期。

最终，数据填补后的完整数据如图：

![](https://github.com/mrkingsun/bitdm.github.io/blob/master/2017/projects/P08/images/full-data.png)

### 3.2 挖掘关联信息

我们首先使用Apriori算法对关联信息进行挖掘。

算法步骤如下：

1) 依据支持度找出所有频繁项集（频度）
扫描、计数、比较、产生频繁项集、连接、剪枝、产生候选项集。重复上述步骤直到不能发现更大的频繁项集。

2) 依据置信度产生关联规则（强度）

根据置信度的定义，关联规则的产生如下：

a) 对于每个频繁项集 L，产生 L的所有非空子集；
b) 对于 L的每个非空子集 S，如果 P(L)/P(S)≧min_conf，则输出规则“L->S”。

挖掘结果如下：

![](https://github.com/mrkingsun/bitdm.github.io/blob/master/2017/projects/P08/images/Apriori-result.png)


由于Apriori算法需要大量候选项集，并且可能需要重复地扫描整个数据库，通过模式匹配检查一个很大的候选集合。因此算法开销过大，FP-tree 算法就解决了这个问题。它采取分治策略，第一步是利用事物数据库中的数据构造FP-tree，第二步是从FP-tree中挖掘频繁模式。 

FP-tree 算法由构造 FP 树和挖掘 FP 树两部分构成。 

构造 FP 树：

(1) 扫描事务库 D，获得 D 中所包含的全部频繁项集 1F，及它们各自的支持度。对 1F 中的频繁项按其支持度降序排序得到 L。

(2) 创建 FP-tree 的根结点 T，以“null”标记。再次扫描事务库。对于 D 中每个事务，将其中的频繁项选出并按 L 中的次序排序。设排序后的频繁项表为[p|P]，其中 p 是第一个频繁项，而 P 是剩余的频繁项。调用 insert_tree([p|P],T)，insert_tree([p|P],T)过程执行情况如下：如果 T 有子女 N 使 N .item_name=p.item_name，则 N 的计数增加 1；否则创建一个新结点 N，将其计数设置为1，链接到它的父结点 T，并且通过 node_link 将其链接到具有相同 item_name的结点。如果 P 非空，递归地调用 insert_tree(P，N)。FP-tree 是一个高度压缩的结构，它存储了用于挖掘频繁项集的全部信息。FP-tree 所占用的内存空间与树的深度和宽度成比例，树的深度一般是单个事务中所含项目数量的最大值；树的宽度是平均每层所含项目的数量。由于在事务处理中通常会存在着大量的共享频繁项，所以树的大小通常比原数据库小很多。频繁项集中的项以支持度降序排列，支持度越高的项与 FP-tree 的根距离越近，因此有更多的机会共享结点，这进一步保证了 FP-tree 的高度压缩。 

挖掘 FP 树:

procedure FP_growth(Tree, a)
if Tree 含单个路径 P then{ 
for 路径 P 中结点的每个组合（记作 b） 
产生模式 b U a，其支持度 support = b 中结点的最小支持度； 
} else {
for each a i 在 Tree 的头部(按照支持度由低到高顺序进行扫描){
产生一个模式 b = a i U a，其支持度 support = a i .support；
构造 b 的条件模式基，然后构造 b 的条件 FP-树 Treeb；
if Treeb 不为空 then
调用 FP_growth (Treeb, b)；
}
} 

挖掘出频繁项集部分展示如下： 

频繁 1 项集：
frozenset({'F4'})
frozenset({'H4'})
frozenset({'A4'}) 

频繁 2 项集：
frozenset({'A4', 'F1'})
frozenset({'A3', 'C2'})
frozenset({'D2', 'E2'}) 

频繁 3 项集：
frozenset({'A3', 'B2', 'F3'})
frozenset({'B2', 'D2', 'H4'})
frozenset({'A3', 'E2', 'H4'}) 

### 3.3 结果分析
根据实验目标，即考察中医症素与乳腺癌 TNM 分期之间的关系，我们对挖掘的规则进行过滤，只关注那些以 TNM 分期作为结果的规则。并设置最小支持度为 6%，最小置信度为 75%。最终得到的有用关联规则如下： 

D3∧F4=>H4   support = 0.73210   confidence = 0.86765 

A4∧F4=>H4   support = 0.08073   confidence = 0.86867 

C4∧F4=>H4   support = 0.06674   confidence = 0.83871 

E3∧F3=>H4   support = 0.06566   confidence = 0.80328 

B2∧F4=>H4   support = 0.07750   confidence = 0.79167 

A3∧E3=>H4   support = 0.09795   confidence = 0.76923 

A3∧E4=>H4   support = 0.07643   confidence = 0.76056 


根据以上的频繁项集的挖掘，我们可以发现 TNM 分期为 H4 的患者有很多，并且也是我们所重点关注的数据，因此挖掘出的频繁项集基本上都是与 H4分期相关的。为了得到中医症素与其他 TNM 分期之间的关系，我们使用决策树模型进行实验，使用信息增益作为属性选择度量，并随机选取 100 条数据进行训练。
根据决策树得到的规则如下： 

if 肝肾阴虚证型系数 = F2 and 肝气郁结证型系数 = A1 then TNM=H1

if 肝肾阴虚证型系数 = F2 and 肝气郁结证型系数 = A2 and 热毒蕴结证型系数 =B2 then TNM = H1

if 肝肾阴虚证型系数 = F1 and 热毒蕴结证型系数 = B1 and 冲任失调证型系数 = C3 then TNM = H2

if 肝肾阴虚证型系数 = F1 and 热毒蕴结证型系数 = B2 then TNM = H2

if 肝肾阴虚证型系数 = F2 and 肝气郁结证型系数 = A2 and 热毒蕴结证型系数 = B1 then TNM = H2

if 肝肾阴虚证型系数 = F1 and 热毒蕴结证型系数 = B3 then TNM = H3

if 肝肾阴虚证型系数 = F2 and 肝气郁结证型系数 = A3 then TNM = H3

if 肝肾阴虚证型系数 = F2 and 肝气郁结证型系数 = A5 then TNM = H3

if 肝肾阴虚证型系数 = F1 and 热毒蕴结证型系数 = B1 and 冲任失调证型系数 = C1 then TNM = H4

if 肝肾阴虚证型系数 = F2 and 肝气郁结证型系数 = A2 and 热毒蕴结证型系数 = B3 then TNM = H4

if 肝肾阴虚证型系数 = F2 and 肝气郁结证型系数 = A3 and 脾胃虚弱证型系数 = E3 then TNM = H4

if 肝肾阴虚证型系数 = F2 and 肝气郁结证型系数 = A4 then TNM = H4

if 肝肾阴虚证型系数 = F3 then TNM = H4

if 肝肾阴虚证型系数 = F4 then TNM = H4

### 4. 总结
在本次关于中医症素与乳腺癌 TNM 分期之间的关系的数据挖掘项目当中，我们可以发现，TNM 分期处于 IV 期的乳腺癌患者，其证型主要为：肝肾阴虚证、肝气郁结证以及脾胃虚弱证。其中肝肾阴虚证、肝气郁结证的临床表现较为突出，置信度与支持度都很高，且肝肾阴虚证几乎存在于所有的能得出IV 分期的关联规则当中，因此，对于乳腺癌患者，应当选取以滋养肝肾的药物为主，并且，除了服用药物外，也可以在饮食上注意使用一些对提高肝功能和肾功能有帮助的食物。
