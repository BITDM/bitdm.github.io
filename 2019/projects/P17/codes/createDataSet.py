# -- coding:utf-8 --

import pandas as pd
import numpy as np
import time
import os

# DataSet1.0 对Load数据源文件合并之后的表格，不包括气候数据.
# DataSet2.0 对1.0版本进行行扩充.
# DataSet3.0 对2.0版本添加气候数据源文件中的数据，会有大量气候数据缺失值，至此，完整的原始数据集生成.
# DataSet4.0 对3.0版本使用均值填充缺失的气候数据.
# DataSet5.0 对4.0版本使用多种方法填充负荷数据的缺失值.
# DataSet6.0 对5.0版本负荷数据进行异常点检测与修正.
# DataSet7.0 对6.0版本增加负荷特征.

def createDataSet(path="./DatasetTwoYears/", create=1):
    """
    将2年的原始txt文件整合成DataFrame格式的一张表.
    ---删除['Type', 'Energysid', 'Expertsid', 'compsid', 'areaenergysid',
        'RecNo', 'Name', 'posisid', 'buildingsid', 'Load_Time'] 无效列.
    ---将Equsid列重新编码为123456.
    ---添加 Year Month Day Hour Half 列.

    :param path: 源文件路径.
    :param create: 是否创建新的csv文件.
    :return: dataSet: 数据集.
    """

    start = time.clock()

    path_list = os.listdir(path)
    path_list.sort()
    dataSet = pd.DataFrame()
    for filename in path_list:
        txtFileName = os.path.join(path, filename)
        data = pd.read_csv(txtFileName)
        # data['File'] = filename    # 标记数据的源文件.
        dataSet = dataSet.append(data, ignore_index=True)

    # 删除无效行.
    dataSet.drop(['Type', 'Energysid', 'Expertsid', 'compsid', 'areaenergysid',
                  'RecNo', 'Name', 'posisid', 'buildingsid', 'Load_Time'], axis=1, inplace=True)

    Half = []   # mark half hour, 1 corresponds to yes, 0 corresponds to no
    Hour = []
    Day = []
    Month = []
    Year = []
    for index, row in dataSet.iterrows():
        timeOriginal = row['Data_Time']
        a = timeOriginal.split('/')
        b = a[2].split()
        c = b[1].split(':')
        day = int(a[0])
        month = int(a[1])
        year = int(b[0])
        hour = int(c[0])
        half = 0 if c[1] == '00' else 1
        Half.append(half)
        Hour.append(hour)
        Day.append(day)
        Month.append(month)
        Year.append(year)
    dataSet.insert(1, 'Half', np.array(Half))
    dataSet.insert(1, 'Hour', np.array(Hour))
    dataSet.insert(1, 'Day', np.array(Day))
    dataSet.insert(1, 'Month', np.array(Month))
    dataSet.insert(1, 'Year', np.array(Year))

    # 转换消纳数据类型.
    dict_ = {150300000109: 1, 150300000110: 2, 150300000111: 3,
             150300000112: 4, 150500000078: 5, 150500000081: 6}
    dataSet['Equsid'].replace(dict_, inplace=True)

    # 1.0版本诞生.
    if create == 1:
        dataSet.to_csv('DataSet1.0.csv', index=False)

    end = time.clock()
    print('createDataSet', end-start)    # 18s

    return dataSet

def create_data_set(path="./DatasetTwoYears/"):
    """
    将2年的原始txt文件整合成DataFrame格式的一张表.

    :param path: 源文件路径.
    :param create: 是否创建新的csv文件.
    :return: dataSet: 数据集.
    """

    start = time.clock()

    path_list = os.listdir(path)
    path_list.sort()
    dataSet = pd.DataFrame()
    for filename in path_list:
        txtFileName = os.path.join(path, filename)
        data = pd.read_csv(txtFileName)
        # data['File'] = filename    # 标记数据的源文件.
        dataSet = dataSet.append(data, ignore_index=True)
    dataSet.to_csv('DataSet.csv', index=False)

if __name__ == '__main__':
    create_data_set()
    createDataSet()