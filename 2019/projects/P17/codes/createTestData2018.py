# -- coding:utf-8 --

import pandas as pd
import numpy as np
import time
import warnings
from createDataSet import createDataSet
from fillRowData import fill_row_data
from addFeatures import add_weather_data
from fillLoseData import fill_wearther_data, fill_value_data
from dataAnalysis import detect_missing_value

# 创建2018年可用于测试模型的数据.
# 依旧进行了行扩充, 但是所有扩充行的Value均填补为0.

def create_test_data(create=1):
    """
    创建用于测试的2018年数据集.

    :param create: 是否创建新的csv文件.
    :return: test_Data2018: 2018年数据集.
    """

    test_Data2018 = createDataSet(path='./201801-201805/', create=0)
    detect_missing_value(test_Data2018, name='loss_data2018')
    test_Data2018 = fill_row_data(test_Data2018, create=0)
    test_Data2018 = add_weather_data(test_Data2018, create=0)
    print(test_Data2018.info())
    test_Data2018 = fill_wearther_data(test_Data2018, create=0)
    test_Data2018 = fill_value_data(test_Data2018, create=0, test=1)
    test_Data2018.to_csv('test_Data2018.csv', index=False)
    data = pd.read_csv('test_DataFina.csv')
    test_Data2018.insert(8, 'Season', data.Season)
    test_Data2018.insert(8, 'isHoliday', data.isHoliday)
    test_Data2018.insert(8, 'isWorkday', data.isWorkday)
    test_Data2018.insert(8, 'dayOfWeek', data.dayOfWeek)
    return test_Data2018

if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    create_test_data(create=1)
