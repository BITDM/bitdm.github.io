# -- coding:utf-8 --

import pandas as pd
import time
import warnings

############# 功能说明 #############

# -----------------------------添加气候特征.
#   对2.0csv文件添加气候源文件的温度、湿度特征.
#   add_weather_data(dataSet, create=1)
# -----------------------------添加日期特征.
#   对2.0csv文件添加与天有关的特征.
#   add_date_data(dataSet)
# -----------------------------添加同时刻负荷特征.
#   对6.0csv文件添加与同时刻负荷有关的特征.
#   add_load_data(dataSet)
#   -----------------------------添加负荷区间特征.
#   add_load_range(dataSet)

def add_weather_data(dataSet, create=1):
    """
    添加气候数据.
    暂未处理缺失气候数据.

    :param dataSet: 数据集.
    :param create: 是否创建新的csv文件.
    :return: dataSet: 数据集.
    """

    start = time.clock()

    dataSet = dataSet
    weatherData = pd.read_csv('weather-new.csv')
    weatherData.rename(columns={'times': 'Data_Time'}, inplace=True)
    weatherData.drop(['projectinfo_id', 'id', 'updatedata_date'], axis=1, inplace=True)
    # 原始气候数据偏移了8行.
    # weatherData.loc[8:] = weatherData[0:]
    # weatherData = weatherData.ix[8:]
    # weatherData.to_csv('weather.csv', index=False)
    # print(weatherData.head())

    dataSet = pd.merge(dataSet, weatherData, on='Data_Time', sort=False, copy=False, how='left')

    # 3.0版本诞生.
    if create == 1:
        dataSet.to_csv('DataSet3.0.csv', index=False)
    # print(data.head())

    end = time.clock()
    print('add_weather_data', end - start)     # 5s

    return dataSet

def add_date_data(dataSet):
    """
    添加星期几、是否为工作日、是否为节假日、季节数据.

    :return:
    """

    start = time.clock()
    # 这里暂时只是通过csv直接复制了数据.

    end = time.clock()
    print(end - start)
    pass

def add_load_data(dataSet):
    """
    添加下述负荷特征.
        ---前半个小时 同一消纳数据 F_half.
        ---前一天 同一时刻 同一消纳数据 F_day.
        ---前一周 同一时刻 同一消纳数据 F_week.

    :param dataSet: 数据集.
    :return:
    """

    start = time.clock()

    dataSet = dataSet
    data1 = dataSet.shift(6)
    data2 = dataSet.shift(288)
    data3 = dataSet.shift(2016)
    dataSet.insert(8, 'F_week', data3['Value'])
    dataSet.insert(8, 'F_day', data2['Value'])
    dataSet.insert(8, 'F_half', data1['Value'])
    # 对表头几列没有更前面时间的行数据, 用当前时刻真实值填充, 不考虑加噪声.
    indexes = dataSet[dataSet.F_week.isnull() == True].index.values
    dataSet.F_week.loc[indexes] = dataSet.Value.loc[indexes]
    indexes = dataSet[dataSet.F_day.isnull() == True].index.values
    dataSet.F_day.loc[indexes] = dataSet.Value.loc[indexes]
    indexes = dataSet[dataSet.F_half.isnull() == True].index.values
    dataSet.F_half.loc[indexes] = dataSet.Value.loc[indexes]
    
    # 7.0版本诞生.
    dataSet.to_csv('DataSet7.0.csv', index=False)

    end = time.clock()
    print(end - start)    # 5s
    pass

if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    start = time.clock()

    # -----------------------------添加气候特征.
    # dataSet = pd.read_csv('DataSet2.0.csv')
    # add_weather_data(dataSet)
    # -----------------------------添加日期特征.
    # add_data()
    # -----------------------------添加同时刻负荷特征.
    dataSet = pd.read_csv('DataSet6.0.csv')
    add_load_data(dataSet=dataSet)

    end = time.clock()
    print(end - start)  # 3.9s

