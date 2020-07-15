---
layout: page
mathjax: true
permalink: /2020/projects/p08/proposal/
---

## 基于多种回归方法的Kaggle房价预测

### 成员

* 韩亚辉_3220190803
* 郝家辉_3220190804
* 许达_3220190905
* 李生椰_3220190827
* 李思远_3220190828

### 问题描述

#### 1、问题背景及分析

Kaggle房价预测：[House Prices: Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniqueshttps://www.kaggle.com/c/house-prices-advanced-regression-techniques)

房价与我们的生活息息相关，房价的波动牵动着无数购房者的心。如果能够预测房价的走势，可以有效地帮助购买者做出合理的决策。本项目中，我们选择kaggle竞赛中的爱荷华州艾姆斯住宅数据集，数据集中有 79 个变量几乎描述了爱荷华州艾姆斯 (Ames, Iowa) 住宅的方方面面。我们将对数据集建模分析，并对房价进行预测。

影响房价的因素有很多，我们将进行数据可视化来分析各个因素对房价的影响，使用特征工程选择最相关的因素，利用多个机器学习算法（如决策树回归、xgboost等 ）构建房价回归模型，并对比分析预测结果。

#### 2、问题描述

2.1 数据准备

本项目使用kaggle上的Ames Housing dataset（爱荷华州埃姆斯市住宅数据集），该数据集包含以下四个部分:

* train.csv - 训练集
* test.csv - 测试集
* data-description.txt - 对每一列属性的描述文本
* sample-submission.csv - 根据销售年份和月份，地皮尺寸和卧室数量进行线性回归的基准提交

训练集和测试集合中的每条记录包含79项特征，用于描述市区住宅的属性，其部分属性简短描述如下所示：

* SalePrice-该房产的售价。这是我们要预测的目标变量。
* MSSubClass：建筑分类
* MSZoning：常规分区分类
* LotFrontage：街道的线性尺寸
* LotArea：以平方英尺为单位的地块大小
* Street：街道的类型
* Alley：胡同的类型
* LotShape：房产的一般形状
* LandContour：房产的平坦度
* Utilities：可用的公共设施类型
* LotConfig：地块配置
* LandSlope：房产的坡度
* Neighborhood：埃姆斯市区范围内的地理位置
* Condition1：接近主干道或铁路
* Condition2：接近主要道路或铁路（如果有）
* BldgType：住宅类型
* HouseStyle：住宅风格
* OverallQual：总体材料和加工质量
* OverallCond：总体状况的评价
* YearBuilt：原始施工日期
* YearRemodAdd：改型日期
* RoofStyle：屋顶类型
* RoofMatl：屋顶材料
* Exterior1st：房屋外墙
* Exterior2nd：房屋的外墙覆盖物（如果使用一种以上的材料）
* MasVnrType：砖石饰面类型
* MasVnrArea：砌面贴面面积（平方英尺）
* ExterQual：外部材料质量
* ExterCond：外部材料的当前状态
* Foundation：基金会的类型
* BsmtQual：地下室的高度
* BsmtCond：地下室的一般状况
* BsmtExposure：罢工或花园水平的地下室墙壁
* BsmtFinType1：地下室成品区域的质量
* BsmtFinSF1：1型成品的尺寸（平方英尺）
* BsmtFinType2：第二个完成区域的质量（如果存在）
* BsmtFinSF2：2型成品尺寸（平方英尺）
* BsmtUnfSF：未完成的地下室面积（平方英尺 ）
* TotalBsmtSF：地下室总平方英尺
* Heating：供热方式
* HeatingQC：供热质量和条件
* CentralAir：中央空调
* Electrical：电气系统
* 1stFlrSF：一楼面积
* 2ndFlrSF：二楼面积
* LowQualFinSF：低质量完成面积（所有楼层）
* GrLivArea：地面（地面）以上居住面积
* BsmtFullBath：地下室全浴室
* BsmtHalfBath：地下室半浴室
* FullBath：地上全浴室
* HalfBath：地上半浴室
* Bedroom：地下室以上的卧室数量
* Kitchen：厨房数量
* KitchenQual：厨房质量
* TotRmsAbvGrd：上等客房总数（不包括浴室）
* Functional：家庭功能等级
* Fireplaces：壁炉数量
* FireplaceQu：壁炉质量
* GarageType：车库位置
* GarageYrBlt：车库建成年份
* GarageFinish：车库的内部装饰
* GarageCars：车库中车库的大小
* GarageArea：车库的大小（平方英尺）
* GarageQual：车库质量
* GarageCond：车库条件
* PavedDrive：铺装的车道
* WoodDeckSF：木制地板面积（平方英尺）
* OpenPorchSF：开放式阳台面积（平方英尺）
* EnclosedPorch：封闭的走廊面积（以平方英尺为单位）
* 3SsnPorch：三季走廊面积（以平方英尺为单位）
* ScreenPorch：纱窗走廊面积（以平方英尺为单位）
* PoolArea：游泳池面积
* PoolQC：泳池质量
* Fence：围栏质量
* MiscFeature：未包括在其他类别中的各方面特点
* MiscVal：各方面特点的价值
* MoSold：已售月份
* YrSold：已售年份
* SaleType：销售类型
* SaleCondition：销售条件

2.2 准备采用的方法或模型

准备使用线性回归，随机森林回归，xgBoost等算法，线性回归算法对线性数据有很好的解释性，随机森林用于回归任务，其非线性特性可以使其比线性算法更具优势，而XGBoost高效地实现了GBDT并进行了改进，速度快，效果好。使用这些算法构建房价回归模型，并进行对比和模型优化。

2.3 预期的挖掘结果

建立起房价预测模型，实现对房价的预测，对于测试集的每一个ID，都能大致预测出它的销售价格。

### 项目评估

评价标准使用MAE(Mean Absolute Error)。若真实值为​，模型预测值为​,那么该模型的MAE计算公式为

$$
\text{MAE} = \frac{\sum_{i=1}^{n}\left | y_{i} - \hat{y}_{i}\right |}{n}
$$

MAE越小代表模型预测越准确。

### 项目分工

* 郝家辉、韩亚辉：数据分析和可视化、数据预处理、特征工程、文档编写
* 许达、李生椰、李思远：频繁模式挖掘、模型构建和优化、文档编写 
