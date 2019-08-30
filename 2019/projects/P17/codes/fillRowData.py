# -- coding:utf-8 --

import pandas as pd
import numpy as np
from dataAnalysis import detect_missing_value
import time
import warnings

############# 功能说明 #############

#   当某个半点/整点/某天存在一台/几台消纳数据缺失时, 称之为行扩充.
# -----------------------------对源文件生成的1.0csv文件进行行扩充.
#   fill_row_data(dataSet, create=1)
#   insertItem(supData, year, month, day, hour, half, dis)


def fill_row_data(dataSet, create=1):
    """
    检测是否存在整行数据缺失, 整行数据缺失指的是某个时刻(整点或半点)某台消纳的数据完全没有.
    将缺失数据补充在supData这张表中.

    :param dataSet: 数据集.
    :param create: 是否创建新的csv文件
    :return: dataSet: 数据集.
    """

    start = time.clock()

    supData = pd.DataFrame()    # 待合并的数据集.
    Year = set(dataSet['Year'])
    Month = set(dataSet['Month'])  # 每个月的天数不一样.
    hourSet = set(range(0, 24))
    halfSet = set(range(0, 2))
    ESet = set(range(1, 7))
    sumDayItem = 12 * 24  # 每1天应有24个小时的12条6台电机消纳数据.
    sumHourItem = 12  # 每1小时应有12条6台电机消纳数据.
    sumHalfItem = 6  # 每0.5小时应有6条6台电机消纳数据.
    countDay = 0  # the number of day lack of data.
    countHour = 0  # the number of hour lack of data, including lack of total hour or lack of half.
    countHalf = 0  # the number of half lack of data, including lack of total half or lack of columns.
    for year in Year:
        for month in Month:
            df_year = dataSet[dataSet['Year'] == year]
            df_month = df_year[df_year['Month'] == month]
            Day = set(df_month['Day'])
            for day in Day:
                df_day = df_month[df_month['Day'] == day]
                if sumDayItem == len(df_day):
                    continue
                else:
                    # print(year, month, day)
                    countDay += 1
                    Hour = set(df_day['Hour'])
                    for hour in hourSet:
                        if hour not in Hour:
                            countHour += 1
                            # print(year, month, day, hour, 'not in')
                            supData = insertItem(supData, year, month, day, hour, 0, ESet)
                            supData = insertItem(supData, year, month, day, hour, 1, ESet)
                        else:
                            df_hour = df_day[df_day['Hour'] == hour]
                            if sumHourItem == len(df_hour):
                                continue
                            else:
                                # print(year, month, day, hour, 'in')
                                Half = set(df_hour['Half'])
                                for half in halfSet:
                                    if half not in Half:
                                        countHalf += 6
                                        # print(year, month, day, hour, half, 'not in')
                                        supData = insertItem(supData, year, month, day, hour, half, ESet)
                                    else:
                                        df_half = df_hour[df_hour['Half'] == half]
                                        if sumHalfItem == len(df_half):
                                            continue
                                        else:
                                            # 观察缺失的消纳, 逐行添加1行半点数据.
                                            dis = ESet - set(df_half['Equsid'])     # 缺失的消纳标签集合.
                                            countHalf += len(dis)
                                            # print(year, month, day, hour, half, dis, 'in')
                                            supData = insertItem(supData, year, month, day, hour, half, dis)
        print(month, 'month has already been finished')
    # 拼接和排序数据.
    dataSet = dataSet.append(supData, ignore_index=True)
    dataSet = dataSet.sort_values(by=['Year', 'Month', 'Day', 'Hour', 'Half', 'Equsid'])

    # 2.0版本诞生.
    if create == 1:
        dataSet.to_csv('DataSet2.0.csv', index=False)
    print(countDay)
    print(countHour)
    print(countHalf)
    end = time.clock()
    print('fill_row_data', end - start)  # 50s

    return dataSet


def insertItem(supData, year, month, day, hour, half, dis):
    """
    在supData表中, 逐条插入数据.

    :param year:
    :param month:
    :param day:
    :param hour:
    :param half:
    :param dis: 缺失的消纳标签集合
    :return: supData: 待合并的数据集.
    """

    time1 = '/'.join([str(day), str(month), str(year)])
    if hour < 10:
        if half == 0:
            time2 = ':'.join(['0' + str(hour), '00', '00'])
        else:
            time2 = ':'.join(['0' + str(hour), '30', '00'])
    else:
        if half == 0:
            time2 = ':'.join([str(hour), '00', '00'])
        else:
            time2 = ':'.join([str(hour), '30', '00'])
    data_time = ' '.join([time1, time2])
    for e in dis:
        insertRow = pd.DataFrame([[data_time, year, month, day, hour, half, np.nan, e]],
                                 columns=['Data_Time', 'Year', 'Month', 'Day', 'Hour', 'Half', 'Value', 'Equsid'])
        supData = supData.append(insertRow, ignore_index=True)      # 在行尾插入数据.

    return supData


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    start = time.clock()

    # -----------------------------对源文件生成的1.0csv文件进行行扩充.
    dataSet = pd.read_csv('DataSet1.0.csv')
    # 收集缺失数据
    # detect_missing_value(dataSet, name='lose_data')
    fill_row_data(dataSet)

    end = time.clock()
    print(end - start)  # 50s
