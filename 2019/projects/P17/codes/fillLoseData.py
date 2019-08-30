# -- coding:utf-8 --

import pandas as pd
import numpy as np
import time
import warnings

############# 功能说明 #############

# -----------------------------填补缺失气候数据.
#   fill_wearther_data(dataSet, create=1)
# -----------------------------填补缺失负荷数据.
#   fill_value_data(dataSet, create=1, test=0)
# -----------------------------查找特定index、column前后值函数.
#   searchValue(data, column, index, divide, mark)

def fill_value_data(dataSet, create=1, test=0):
    """
    填补缺失的负荷数据.
    大电网为主要负荷, 辅以风力消纳与光伏消纳. 消纳顺序大致为6 5 1 2 3 4.
    当6的Value为0时, 12345必为0. 当5为0时, 1234必为0. 当1为0时, 234必为0.
    因此填补策略为:
        ---第一步, 156全部填0, 234每天的0~6点、19~24点全部填0.
        ---第二步, 234剩下时段采用平滑处理.
        注意, 两步的顺序不可以颠倒.

    测试数据集所有缺失值均填0.

    :param dataSet: 数据集.
    :param create: 是否创建新的csv文件.
    :param test: 1表示创建测试数据集, 所有缺失值均填0.
    :return: dataSet: 数据集.
    """

    start = time.clock()

    if test == 0:
        # 156缺失值填0.
        indexes = dataSet[((dataSet.Equsid == 1) | (dataSet.Equsid == 5) | (dataSet.Equsid == 6))
                        & (dataSet.Value.isnull() == True)].index.values
        dataSet.Value.loc[indexes] = 0

        # 234每天的0~6点、19~24点全部填0.
        indexes = dataSet[((dataSet.Equsid == 2) | (dataSet.Equsid == 3) | (dataSet.Equsid == 4))
                        & (dataSet.Value.isnull() == True) & (((dataSet.Hour >= 0) & (dataSet.Hour <= 6))
                        | ((dataSet.Hour >= 19) & (dataSet.Hour <= 23)))].index.values
        dataSet.Value.loc[indexes] = 0

        # 234缺失值平滑处理.
        count = 0
        indexes = dataSet[dataSet.Value.isnull() == True].index.values
        print('The total missing Value is ', len(indexes))
        for index in indexes:
            fvalue, divide1 = searchValue(data=dataSet, column='Value', index=index - 6, divide=0, mark=-1)
            lvalue, divide2 = searchValue(data=dataSet, column='Value', index=index + 6, divide=2, mark=1)
            if fvalue != 'nan' and lvalue != 'nan':
                value = (lvalue - fvalue) / (divide1 + divide2) + fvalue
                dataSet.Value.loc[index] = value
                count += 1
        print(count, ' has already been finished')
        if dataSet.Value.isnull().sum() != 0:
            dataSet.Value.fillna(method='ffill', axis=0, inplace=True)
            dataSet.Value.fillna(method='bfill', axis=0, inplace=True)

        print(dataSet.info())

        # 5.0版本诞生.
        if create == 1:
            dataSet.to_csv("DataSet5.0.csv", index=False)
    else:
        indexes = dataSet[dataSet.Value.isnull() == True].index.values
        dataSet.Value.loc[indexes] = 0
        print(dataSet.info())

    end = time.clock()
    print('fill_value_data', end - start)   # 84s

    return dataSet

def fill_wearther_data(dataSet, create=1):
    """
    采用纵向均值填补缺失的气候数据, 即利用前后半个小时的气候数据的均值填充.

    :param dataSet: 数据集.
    :param create: 是否创建新的csv文件
    :return: dataSet: 数据集.
    """

    start = time.clock()

    dataSet = dataSet
    # 去除0值.
    indexes = dataSet[dataSet.t_10 == 0].index.values
    dataSet.t_10.loc[indexes] = np.nan
    indexes = dataSet[dataSet.rh_10 == 0].index.values
    dataSet.rh_10.loc[indexes] = np.nan
    data = dataSet[dataSet.Equsid == 1]
    totalNum = data[['t_10', 'rh_10']].isnull().sum().sum()
    print('The total missing Value is ', totalNum)
    count = 0
    for index, row in data.iterrows():
        if np.isnan(row['t_10']) == True:
            ftmp, divide1 = searchValue(data=data, column='t_10', index=index-6, divide=0, mark=-1)
            ltmp, divide2 = searchValue(data=data, column='t_10', index=index+6, divide=2, mark=1)
            if ftmp != 'nan' and ltmp != 'nan':
                value = (ltmp - ftmp) / (divide1 + divide2) + ftmp
                dataSet.t_10.loc[index] = value
                count += 1
        if np.isnan(row['rh_10']) == True:
            frh, divide1 = searchValue(data=data, column='rh_10', index=index-6, divide=0, mark=-1)
            lrh, divide2 = searchValue(data=data, column='rh_10', index=index+6, divide=2, mark=1)
            if frh != 'nan' and lrh != 'nan':
                value = (lrh - frh) / (divide1 + divide2) + frh
                dataSet.rh_10.loc[index] = value
                count += 1
    print(count, ' has already been finished')
    if dataSet[['t_10', 'rh_10']].isnull().sum().sum() != 0:
        dataSet['t_10'].fillna(method='ffill', axis=0, inplace=True)
        dataSet['t_10'].fillna(method='bfill', axis=0, inplace=True)
        dataSet['rh_10'].fillna(method='ffill', axis=0, inplace=True)
        dataSet['rh_10'].fillna(method='bfill', axis=0, inplace=True)

    print(dataSet.info())

    # 4.0版本诞生.
    if create == 1:
        dataSet.to_csv('DataSet4.0.csv',  index=False)

    end = time.clock()
    print('fill_wearther_data', end - start)  # 600s

    return dataSet

def searchValue(data, column, index, divide, mark):
    """
    在data表的column列中查找索引为index且不为空值的数据.
    若为空值, 当mark为-1时, 向前查找; mark为1时, 向后查找.
    当索引超过data表限制时, 如index<0, 则返回'nan'.

    :param data:
    :param column:
    :param index:
    :param divide:
    :param mark:
    :return:
    value: 查找的值.
    divide： 均值/平滑填充的除数.
    """

    if index < 0 or index > data.index[-1]:
        return 'nan', 'nan'
    value = data[column].loc[index]
    if np.isnan(value) == False:
        return value, divide
    else:
        if mark == -1:
            value, divide = searchValue(data=data, column=column, index=index-6, divide=divide+1, mark=-1)
        else:
            value, divide = searchValue(data=data, column=column, index=index+6, divide=divide+1, mark=1)
        return value, divide
    pass

if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    start = time.clock()

    # -----------------------------填补缺失气候数据.
    # dataSet = pd.read_csv('DataSet3.0.csv')
    # fill_wearther_data(dataSet=dataSet)
    # -----------------------------填补缺失负荷数据.
    dataSet = pd.read_csv('dataSet4.0.csv')
    fill_value_data(dataSet=dataSet)

    end = time.clock()
    print(end - start)  # 3.9s
