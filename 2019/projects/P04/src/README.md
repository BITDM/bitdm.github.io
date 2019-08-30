社交广告高校算法大赛-相似人群拓展：
郑安庆 3120181078	
白雪峰 3120180977
卞西墨 3120180978	
沙  九 3120181023

项目说明:
			---当前目录下有两个文件夹分别为：ffm、lgd
			---在ffm下的脚本为本程序主函数、程序的切入口
			---在lgd下两个文件分别为offline和online两个文件
			---在lgd下三个脚本gen_feat.py、train_model.py和train_data.py分别为数据的预处理、模型的训练、数据的预处理
			---online下的四个脚本分别为:eda.py、gen_feat.py、train_model.py、train_data.py分别为数据属性的取值 、数据预处理、模型的训练和数据的清洗
运行环境：
			---python3.6
			---tensorflow==1.4.1
			---其他包
			import numpy as np
			import pandas as pd
			import xgboost as xgb
			import lightgbm as lgb
			import pickle
			import time
			import datetime
			import math
			import os
			import gc
			import warnings
			
数据集下载：
			---数据的具体说明请点击链接查看：https://share.weiyun.com/5eBrbpT
