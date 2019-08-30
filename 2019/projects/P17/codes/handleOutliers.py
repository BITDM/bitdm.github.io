# -- coding:utf-8 --

import pandas as pd
import numpy as np
import time as time
import warnings

############# 功能说明 #############

# -----------------------------修改异常值.
#   handle_outliers(dataSet)

def handle_outliers(dataSet):
    """
    查找异常值. 异常值类型有 波峰异常、冲击负荷.
    波峰异常的判定依据如下, 超过阈值则改为阈值.
        ---消纳1 > 1333
        ---消纳2 > 78    消纳3 > 78    消纳4 > 78
        ---消纳5 > 444    消纳6 > 1133
    冲击负荷的判定依据如下, 超过阈值则调整为相邻值加/减阈值.
        ---消纳1前后差值 > 875.5
        ---消纳2前后差值 > 32    消纳3前后差值 > 32    消纳4 后差值 > 32
        ---消纳5前后差值 > 269.5    消纳6前后差值 >1059.5
    前后差值意为与前后半个小时同一消纳的差值的绝对值.

    :param dataSet: 数据集.
    :return:
    """

    start = time.clock()

    dataSet = dataSet

    # 波峰异常.
    Eid1 = [1, 2, 3, 4, 5, 6]
    value1 = [1333, 78, 78, 78, 444, 1133]
    for eid, value in zip(Eid1, value1):
        indexes = dataSet[(dataSet.Equsid == eid) & (dataSet.Value > value)].index.values
        dataSet.Value.loc[indexes] = value
    print('Wave peak abnormal has already been fixed')

    # 冲击负荷
    Eid2 = [1, 2, 3, 4, 5, 6]
    value2 = [875.5, 32, 32, 32, 269.5, 1059.5]

    diff = dataSet[['Value', 't_10']] - dataSet[['Value', 't_10']].shift(6)   # 表格后移6位.
    for eid, value in zip(Eid2, value2):
        data = diff.fillna(method='bfill', axis=0)
        data.insert(2, 'Equsid', dataSet.Equsid)
        indexes = data[(data.Equsid == eid) & (data['Value'] > value)].index.values
        # print(indexes)
        for index in indexes:
            dataSet.Value.loc[index] = value + dataSet.Value.loc[index - 6]
        indexes = data[(data.Equsid == eid) & (data['Value'] < -value)].index.values
        # print(indexes)
        for index in indexes:
            dataSet.Value.loc[index] = dataSet.Value.loc[index - 6] - value
        print('Impact load {} abnormal has already been fixed'.format(eid))

    diff = dataSet[['Value', 't_10']] - dataSet[['Value', 't_10']].shift(-6)   # 表格后移6位.
    for eid, value in zip(Eid2, value2):
        data = diff.fillna(method='ffill', axis=0)
        data.insert(2, 'Equsid', dataSet.Equsid)
        indexes = data[(data.Equsid == eid) & (data['Value'] > value)].index.values
        # print(indexes)
        for index in indexes:
            dataSet.Value.loc[index] = value + dataSet.Value.loc[index + 6]
        indexes = data[(data.Equsid == eid) & (data['Value'] < -value)].index.values
        # print(indexes)
        for index in indexes:
            dataSet.Value.loc[index] = dataSet.Value.loc[index + 6] - value
        print('Impact load {} abnormal has already been fixed'.format(eid))
    print('Shock load abnormal has already been fixed')

    # 6.0版本诞生.
    dataSet.to_csv('DataSet6.0.csv', index=False)

    end = time.clock()
    print(end - start)     # 4s
    pass


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    start = time.clock()
    # -----------------------------修改异常值.
    dataSet = pd.read_csv('DataSet5.0.csv')
    handle_outliers(dataSet=dataSet)
    # -----------------------------气温/湿度偏移校正.
    # handle_weather(dataSet)

    end = time.clock()
    print(end - start)

