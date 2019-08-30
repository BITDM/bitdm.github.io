# -- coding:utf-8 --

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import csv
import warnings
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
from sklearn import preprocessing
from sklearn.externals import joblib
import time

def createDayLoadSet(dataSet):
    """
    生成以天为单位的负荷数据.
    暂未加入 F_half F_day F_week 3列特征.

    :param dataSet: 数据集.
    :return:
    """

    start = time.clock()

    dataSet = dataSet
    fill = {'Value': 0}
    dataSet.fillna(fill, inplace=True)
    dataSet.fillna(method='ffill', axis=0, inplace=True)
    DayLoadSet = pd.DataFrame()
    Data_Time = []
    Year = []
    Month = []
    Day = []
    Value = []
    Value1 = [];
    Value11 = []
    Value2 = [];
    Value21 = [];
    Value22 = [];
    Value23 = [];
    Value3 = []
    Value31 = [];
    Value32 = []
    dayOfWeek = [];
    isWorkday = [];
    isHoliday = [];
    Season = []
    tem = []
    rh = []
    RH_max = []
    RH_min = []
    Tem_max = []
    Tem_min = []

    data_time = dataSet.iloc[0].Data_Time
    year = dataSet.iloc[0].Year
    month = dataSet.iloc[0].Month
    day = dataSet.iloc[0].Day
    value = 0
    value1 = 0;
    value11 = 0
    value2 = 0;
    value21 = 0;
    value22 = 0;
    value23 = 0
    value3 = 0;
    value31 = 0;
    value32 = 0
    dayofweek = dataSet.iloc[0].dayOfWeek
    holiday = dataSet.iloc[0].isHoliday
    workday = dataSet.iloc[0].isWorkday
    season = dataSet.iloc[0].Season

    for index, row in dataSet.iterrows():
        # print(index)
        # print(len(dataSet))
        if day != row['Day']:
            Data_Time.append(data_time)
            Day.append(day)
            Month.append(month)
            Year.append(year)
            Value.append(value)
            Value1.append(value1)
            Value11.append(value11)
            Value2.append(value2)
            Value21.append(value21)
            Value22.append(value22)
            Value23.append(value23)
            Value3.append(value3)
            Value31.append(value31)
            Value32.append(value32)
            dayOfWeek.append(dayofweek)
            isWorkday.append(workday)
            isHoliday.append(holiday)
            Season.append(season)
            tem = np.array(tem)
            Tem_max.append(tem.max())
            Tem_min.append(tem.min())
            rh = np.array(rh)
            RH_max.append(rh.max())
            RH_min.append(rh.min())
            tem = []
            rh = []
            value = 0
            value1 = 0;
            value11 = 0
            value2 = 0;
            value21 = 0;
            value22 = 0;
            value23 = 0
            value3 = 0;
            value31 = 0;
            value32 = 0
            if day != row['Day']:
                day = row['Day']
            if month != row['Month']:
                month = row['Month']
            if year != row['Year']:
                year = row['Year']
            if data_time != row['Data_Time']:
                data_time = row['Data_Time']
            if dayofweek != row['dayOfWeek']:
                dayofweek = row['dayOfWeek']
            if workday != row['isWorkday']:
                workday = row['isWorkday']
            if holiday != row['isHoliday']:
                holiday = row['isHoliday']
            if season != row['Season']:
                season = row['Season']
        tem.append(row['t_10'])
        rh.append(row['rh_10'])
        if row['Equsid'] == 1:
            value11 += row['Value']
        if row['Equsid'] == 2:
            value21 += row['Value']
        if row['Equsid'] == 3:
            value22 += row['Value']
        if row['Equsid'] == 4:
            value23 += row['Value']
        if row['Equsid'] == 5:
            value31 += row['Value']
        if row['Equsid'] == 6:
            value32 += row['Value']
        value1 = value11
        value2 = value21 + value22 + value23
        value3 = value31 + value32
        value = value1 + value2 + value3
        if index == len(dataSet) - 1:
            Day.append(day)
            Month.append(month)
            Year.append(year)
            Data_Time.append(data_time)
            Value.append(value)
            Value1.append(value1)
            Value11.append(value11)
            Value2.append(value2)
            Value21.append(value21)
            Value22.append(value22)
            Value23.append(value23)
            Value3.append(value3)
            Value31.append(value31)
            Value32.append(value32)
            dayOfWeek.append(dayofweek)
            isWorkday.append(workday)
            isHoliday.append(holiday)
            Season.append(season)
            tem = np.array(tem)
            Tem_max.append(tem.max())
            Tem_min.append(tem.min())
            rh = np.array(rh)
            RH_max.append(rh.max())
            RH_min.append(rh.min())

    DayLoadSet.insert(0, 'Value3', np.array(Value3))
    DayLoadSet.insert(0, 'Value2', np.array(Value2))
    DayLoadSet.insert(0, 'Value1', np.array(Value1))
    DayLoadSet.insert(0, 'Value', np.array(Value))
    DayLoadSet.insert(0, 'RH_min', np.array(RH_min))
    DayLoadSet.insert(0, 'RH_max', np.array(RH_max))
    DayLoadSet.insert(0, 'Tem_min', np.array(Tem_min))
    DayLoadSet.insert(0, 'Tem_max', np.array(Tem_max))
    DayLoadSet.insert(0, 'Season', np.array(Season))
    DayLoadSet.insert(0, 'isHoliday', np.array(isHoliday))
    DayLoadSet.insert(0, 'isWorkday', np.array(isWorkday))
    DayLoadSet.insert(0, 'dayOfWeek', np.array(dayOfWeek))
    DayLoadSet.insert(0, 'Value32', np.array(Value32))
    DayLoadSet.insert(0, 'Value31', np.array(Value31))
    DayLoadSet.insert(0, 'Value23', np.array(Value23))
    DayLoadSet.insert(0, 'Value22', np.array(Value22))
    DayLoadSet.insert(0, 'Value21', np.array(Value21))
    DayLoadSet.insert(0, 'Value11', np.array(Value11))
    DayLoadSet.insert(0, 'Day', np.array(Day))
    DayLoadSet.insert(0, 'Month', np.array(Month))
    DayLoadSet.insert(0, 'Year', np.array(Year))
    DayLoadSet.insert(0, 'Data_Time', np.array(Data_Time))

    # supplementaryData_2 = pd.read_csv('Supplementary_data_2.csv')
    # for index, row in DayLoadSet.iterrows():
    #     year = row['Year']
    #     month = row['Month']
    #     day = row['Day']
    #     a = supplementaryData_2[supplementaryData_2['Year']==year]
    #     b = a[a['Month'] == month]
    #     c = b[b['Day'] == day]
    #     dayOfWeek.append(c['dayOfWeek'].iloc[0])
    #     isHoliday.append(c['isHoliday'].iloc[0])
    # HourLoadSet.insert(8, 'dayOfWeek', np.array(dayOfWeek))
    # HourLoadSet.insert(10, 'isHoliday', np.array(isHoliday))

    DayLoadSet.to_csv('DayLoadSet2018.csv', index=False)

    end = time.clock()
    print(end - start)  # 47s


def createMonthLoadSet(dataSet):
    """
    生成以月为单位的负荷数据.
    暂未加入 F_half F_day F_week 3列特征.

    :param dataSet: 数据集.
    :return:
    """

    start = time.clock()

    dataSet = dataSet
    fill = {'Value': 0}
    dataSet.fillna(fill, inplace=True)
    dataSet.fillna(method='ffill', axis=0, inplace=True)
    MonthLoadSet = pd.DataFrame()
    Data_Time = []
    Year = [];
    Month = []
    Value = []
    Value1 = [];
    Value11 = []
    Value2 = [];
    Value21 = [];
    Value22 = [];
    Value23 = [];
    Value3 = []
    Value31 = [];
    Value32 = []
    Season = []
    tem = []
    rh = []
    RH_max = []
    RH_min = []
    Tem_max = []
    Tem_min = []

    data_time = dataSet.iloc[0].Data_Time
    year = dataSet.iloc[0].Year
    month = dataSet.iloc[0].Month
    value = 0
    value1 = 0;
    value11 = 0
    value2 = 0;
    value21 = 0;
    value22 = 0;
    value23 = 0
    value3 = 0;
    value31 = 0;
    value32 = 0
    season = dataSet.iloc[0].Season

    for index, row in dataSet.iterrows():
        # print(index)
        # print(len(dataSet))
        if month != row['Month']:
            Data_Time.append(data_time)
            Month.append(month)
            Year.append(year)
            Value.append(value)
            Value1.append(value1)
            Value11.append(value11)
            Value2.append(value2)
            Value21.append(value21)
            Value22.append(value22)
            Value23.append(value23)
            Value3.append(value3)
            Value31.append(value31)
            Value32.append(value32)
            Season.append(season)
            tem = np.array(tem)
            Tem_max.append(tem.max())
            Tem_min.append(tem.min())
            rh = np.array(rh)
            RH_max.append(rh.max())
            RH_min.append(rh.min())
            tem = []
            rh = []
            value = 0
            value1 = 0;
            value11 = 0
            value2 = 0;
            value21 = 0;
            value22 = 0;
            value23 = 0
            value3 = 0;
            value31 = 0;
            value32 = 0
            if month != row['Month']:
                month = row['Month']
            if year != row['Year']:
                year = row['Year']
            if data_time != row['Data_Time']:
                data_time = row['Data_Time']
            if season != row['Season']:
                season = row['Season']
        tem.append(row['t_10'])
        rh.append(row['rh_10'])
        if row['Equsid'] == 1:
            value11 += row['Value']
        if row['Equsid'] == 2:
            value21 += row['Value']
        if row['Equsid'] == 3:
            value22 += row['Value']
        if row['Equsid'] == 4:
            value23 += row['Value']
        if row['Equsid'] == 5:
            value31 += row['Value']
        if row['Equsid'] == 6:
            value32 += row['Value']
        value1 = value11
        value2 = value21 + value22 + value23
        value3 = value31 + value32
        value = value1 + value2 + value3
        if index == len(dataSet) - 1:
            Month.append(month)
            Year.append(year)
            Data_Time.append(data_time)
            Value.append(value)
            Value1.append(value1)
            Value11.append(value11)
            Value2.append(value2)
            Value21.append(value21)
            Value22.append(value22)
            Value23.append(value23)
            Value3.append(value3)
            Value31.append(value31)
            Value32.append(value32)
            Season.append(season)
            tem = np.array(tem)
            Tem_max.append(tem.max())
            Tem_min.append(tem.min())
            rh = np.array(rh)
            RH_max.append(rh.max())
            RH_min.append(rh.min())

    MonthLoadSet.insert(0, 'Value3', np.array(Value3))
    MonthLoadSet.insert(0, 'Value2', np.array(Value2))
    MonthLoadSet.insert(0, 'Value1', np.array(Value1))
    MonthLoadSet.insert(0, 'Value', np.array(Value))
    MonthLoadSet.insert(0, 'RH_min', np.array(RH_min))
    MonthLoadSet.insert(0, 'RH_max', np.array(RH_max))
    MonthLoadSet.insert(0, 'Tem_min', np.array(Tem_min))
    MonthLoadSet.insert(0, 'Tem_max', np.array(Tem_max))
    MonthLoadSet.insert(0, 'Season', np.array(Season))
    MonthLoadSet.insert(0, 'Value32', np.array(Value32))
    MonthLoadSet.insert(0, 'Value31', np.array(Value31))
    MonthLoadSet.insert(0, 'Value23', np.array(Value23))
    MonthLoadSet.insert(0, 'Value22', np.array(Value22))
    MonthLoadSet.insert(0, 'Value21', np.array(Value21))
    MonthLoadSet.insert(0, 'Value11', np.array(Value11))
    MonthLoadSet.insert(0, 'Month', np.array(Month))
    MonthLoadSet.insert(0, 'Year', np.array(Year))
    MonthLoadSet.insert(0, 'Data_Time', np.array(Data_Time))

    # supplementaryData_2 = pd.read_csv('Supplementary_data_2.csv')
    # for index, row in MonthLoadSet.iterrows():
    #     year = row['Year']
    #     month = row['Month']
    #     day = row['Day']
    #     a = supplementaryData_2[supplementaryData_2['Year']==year]
    #     b = a[a['Month'] == month]
    #     c = b[b['Day'] == day]
    #     dayOfWeek.append(c['dayOfWeek'].iloc[0])
    #     isHoliday.append(c['isHoliday'].iloc[0])
    # HourLoadSet.insert(8, 'dayOfWeek', np.array(dayOfWeek))
    # HourLoadSet.insert(10, 'isHoliday', np.array(isHoliday))

    MonthLoadSet.to_csv('MonthLoadSet2018.csv', index=False)

    end = time.clock()
    print(end - start)  # 45s


def combine_half(dataSet):
    """
    合并相同类型消纳的行数据, 仍以半个小时为刻度.

    :param dataSet: 数据集.
    :return:
    """

    csvFile2 = open('Count_hour2018.csv', 'w')
    csvFile2.truncate()
    csvFile2 = open('Count_hour2018.csv', 'a+', newline='')
    writer = csv.writer(csvFile2)
    # writer.writerow(
    #     ['Data_Time', 'Year', 'Month', 'Day', 'Hour', 'Half', 'Value', 'Equsid', 'F_half', 'F_day', 'F_week',
    #      'dayOfWeek', 'isHoliday', 'isWorkday', 'Season', 'rh_10', 't_10'])
    writer.writerow(
        ['Data_Time', 'Year', 'Month', 'Day', 'Hour', 'Half', 'Value', 'Equsid',
         'dayOfWeek', 'isHoliday', 'isWorkday', 'Season', 'rh_10', 't_10'])
    Val = {'1': 0.00, '2': 0.00, '3': 0.00}
    F_wee = {'1': 0.00, '2': 0.00, '3': 0.00}
    F_hal = {'1': 0.00, '2': 0.00, '3': 0.00}
    F_da = {'1': 0.00, '2': 0.00, '3': 0.00}
    Name = ['1', '2', '3']
    summ = 0
    for k in range(dataSet.shape[0]):
        summ += 1
        # Data_time, Year, Month, Day, Hour, Half, Value, Equsid, F_half, F_day, \
        # F_week, dayOfWeek, isHoliday, isWorkday, Season, rh_10, t_10 = dataSet.iloc[k, :]
        Data_time, Year, Month, Day, Hour, Half, Value, Equsid, \
        dayOfWeek, isHoliday, isWorkday, Season, rh_10, t_10 = dataSet.iloc[k, :]
        if Equsid == 1:
            Val['1'] += Value
            # F_hal['1'] += F_half
            # F_da['1'] += F_day
            # F_wee['1'] += F_week
        elif Equsid == 5 or Equsid == 6:
            Val['3'] += Value
            # F_hal['3'] += F_half
            # F_da['3'] += F_day
            # F_wee['3'] += F_week
        else:
            Val['2'] += Value
            # F_hal['2'] += F_half
            # F_da['2'] += F_day
            # F_wee['2'] += F_week
        if summ == 6:
            summ = 0
            for j in Name:
                # writer.writerow(
                #     [Data_time, Year, Month, Day, Hour, Half, Val[j], int(j), F_hal[j], F_da[j], F_wee[j], dayOfWeek,
                #      isWorkday, isHoliday, Season, rh_10, t_10])
                writer.writerow(
                    [Data_time, Year, Month, Day, Hour, Half, Val[j], int(j), dayOfWeek,
                     isWorkday, isHoliday, Season, rh_10, t_10])
                Val[j], F_da[j], F_wee[j], F_hal[j] = 0.00, 0.00, 0.00, 0.00


def plot_half_year(dataSet, eid=1):
    """
    绘制消纳的年负荷曲线, 精度为半小时.
    打印消纳数据的统计学描述.
    只支持绘制1台消纳的数据.

    :param dataSet: 数据集.
    :param eid: 消纳的编号.
    :return:
    """

    dataSet = dataSet
    data = dataSet[dataSet.Equsid == eid]
    plt.figure(figsize=[10, 10])
    plt.plot(data['Value'], label=eid)
    plt.plot([len(data) / 2, len(data) / 2], [data.Value.max() + 3, data.Value.min() - 3], ls='--')
    plt.title('The Load Curve of G {} Around Two Years'.format(eid))
    plt.xlabel('half/year')
    plt.ylabel('load')
    plt.legend()
    plt.show()
    print(data[['Value', 't_10', 'rh_10']].describe())
    pass


def plot_half_month(dataSet, month=1, eid=1):
    """
    绘制消纳的月负荷曲线, 精度为半小时.
    eid与month只能有一个为多值sequence类型.

    :param dataSet: 数据集.
    :param eid: 消纳的编号.
    :param month: 月份.
    :return:
    """

    dataSet = dataSet
    plt.figure(figsize=[10, 10])
    if type(eid) == int and type(month) == int:
        data = dataSet[(dataSet.Equsid == eid) & (dataSet.Month == month)]
        plt.plot(data['Value'], label=eid)
        plt.plot([len(data) / 2, len(data) / 2], [data.Value.max() + 3, data.Value.min() - 3], ls='--')
        plt.title('The Load Curve of G {0} Around Month {1}'.format(eid, month))
    elif type(eid) == int:
        for m in month:
            data = dataSet[(dataSet.Equsid == eid) & (dataSet.Month == m)]
            plt.plot(data['Value'], label=m)
        plt.title('The Load Curve of G {0} Around Month {1}'.format(eid, month))
    elif type(month) == int:
        for e in eid:
            data = dataSet[(dataSet.Equsid == e) & (dataSet.Month == month)]
            plt.plot(data['Value'], label=e)
        plt.title('The Load Curve of G{0} Around Month {1}'.format(eid, month))
    else:
        print('!!! eid and month can not be both sequence !!!')
    plt.xlabel('half/month')
    plt.ylabel('load')
    plt.legend()
    plt.show()
    pass


def plot_half_day(dataSet, month=4, day=22, eid=1):
    """
    绘制消纳的日负荷曲线, 精度为半小时.
    eid、month、day只能有一个为多值sequence类型.

    :param dataSet: 数据集.
    :param month: 月份.
    :param day: 哪一天.
    :param eid: 消纳的编号.
    :return:
    """

    dataSet = dataSet
    plt.figure(figsize=[10, 10])
    if type(eid) == int and type(month) == int and type(day) == int:
        data = dataSet[(dataSet.Month == month) & (dataSet.Day == day) & (dataSet.Equsid == eid)]
        plt.plot(data.Value, label=eid)
        plt.plot([len(data) / 2, len(data) / 2], [data.Value.max() + 3, data.Value.min() - 3], ls='--')
        plt.title('The Load Curve of G{} in {}.{} of Two Years'.format(eid, month, day))
    elif type(eid) != int and type(month) == int and type(day) == int:
        for e in eid:
            data = dataSet[(dataSet.Month == month) & (dataSet.Day == day) & (dataSet.Equsid == e)]
            plt.plot(data.Value, label=e)
        plt.title('The Load Curve of G{} in {}.{} of Two Years'.format(eid, month, day))
    elif type(eid) == int and type(month) != int and type(day) == int:
        for m in month:
            data = dataSet[(dataSet.Month == m) & (dataSet.Day == day) & (dataSet.Equsid == eid)]
            plt.plot(data.Value, label=m)
        plt.title('The Load Curve of G{} in month{} day{} of Two Years'.format(eid, month, day))
    elif type(eid) == int and type(month) == int and type(day) != int:
        for d in day:
            data = dataSet[(dataSet.Month == month) & (dataSet.Day == d) & (dataSet.Equsid == eid)]
            plt.plot(data.Value, label=d)
        plt.title('The Load Curve of G{} in month{} day{} of Two Years'.format(eid, month, day))
    else:
        print('!!! eid、month、day can not be all sequence !!!')
    plt.xlabel('half/day')
    plt.ylabel('load')
    plt.legend()
    plt.show()
    pass


def plot_day_year():
    """
    绘制消纳的年负荷曲线, 精度为天.
    :return:
    """

    data = pd.read_csv('DayLoadSet.csv')
    plt.figure(figsize=[10, 10])
    plt.plot(data['Value11'], marker='.', label='1')
    plt.plot(data['Value21'], marker='.', label='2')
    plt.plot(data['Value22'], marker='.', label='3')
    plt.plot(data['Value23'], marker='.', label='4')
    plt.plot(data['Value31'], marker='.', label='5')
    plt.plot(data['Value32'], marker='.', label='6')
    plt.plot(data['Value1'], marker='.', label='wind')
    plt.plot(data['Value2'], marker='.', label='light')
    plt.plot(data['Value3'], marker='.', label='big')
    plt.title('The Load Curve of Two Years')
    plt.xlabel('day/year')
    plt.ylabel('load')
    plt.legend()
    plt.show()
    pass


def plot_day_month():
    """
    绘制消纳的月负荷曲线, 精度为天.

    :return:
    """
    pass


def plot_month_year():
    """
    绘制消纳的年负荷曲线, 精度为月.

    :return:
    """

    data = pd.read_csv("MonthLoadSet.csv")
    plt.figure(figsize=[10, 10])
    plt.plot(data['Value11'], marker='.', label='1')
    plt.plot(data['Value21'], marker='.', label='2')
    plt.plot(data['Value22'], marker='.', label='3')
    plt.plot(data['Value23'], marker='.', label='4')
    plt.plot(data['Value31'], marker='.', label='5')
    plt.plot(data['Value32'], marker='.', label='6')
    plt.plot(data['Value1'], marker='.', label='wind')
    plt.plot(data['Value2'], marker='.', label='light')
    plt.plot(data['Value3'], marker='.', label='big')
    plt.title('The Load Curve of Two Years')
    plt.xlabel('month/year')
    plt.ylabel('load')
    plt.legend()
    plt.show()
    pass


def dif_half(plot, *para):
    """
    收集传入消纳类型（最多9个）相邻半小时的负荷差值绝对值.
    对差值做统计学分析.

    :param plot: bool, 是否绘制差异曲线, 绘制为1.
    :return: DataFrame
    """

    dataSet = pd.read_csv('HalfLoadSet.csv')
    data = dataSet[list(para)]
    differences = data - data.shift(1)
    differences.fillna(method='bfill', axis=0, inplace=True)
    # # 绘图
    # dif = differences.copy()
    # dif = dif.abs()
    # dif.plot(kind='box', figsize=(12, 8))
    # # differences.hist(figsize=(12, 8))
    # plt.show()
    differences.to_csv("Differences—half.csv", index=False)
    differences = differences.abs()
    if plot == 1:
        plot_dif(dataSet=differences)
    diff_des = pd.DataFrame([differences.max(), differences.mean(), differences.std(), differences.quantile(0.80),
                             differences.quantile(0.85), differences.quantile(0.90), differences.quantile(0.95),
                             differences.quantile(0.97), differences.quantile(0.99), differences.quantile(0.995),
                             differences.quantile(0.997), differences.quantile(0.998), differences.quantile(0.9985),
                             differences.quantile(0.999), differences.quantile(0.9995), differences.quantile(0.9999),
                             differences.quantile(0.99995), differences.quantile(0.99999)],
                            index=['max', 'mean', 'std', '80%', '85%', '90%', '95%', '97%', '99%',
                                   '99.5%', '99.7%', '99.8%', '99.85%', '99.9%', '99.95%', '99.99%', '99.995%',
                                   '99.999%'])
    diff_des.T.to_csv('DiffDes-Half.csv')
    print(diff_des.T)
    # print("Describe ##################")
    # print(differences.describe())
    # print("Max ##################")
    # print(differences.max())
    # print("Mean ##################")
    # print(differences.mean())
    # print("Std ##################")
    # print(differences.std())
    # print("Quantile ##################")
    # print(differences.quantile(0.8))
    return differences
    pass


def dif_day(plot, *para):
    """
    收集传入消纳类型（最多9个）相邻一天的负荷差值绝对值.
    对差值做统计学分析.

    :param plot: bool, 是否绘制差异曲线, 绘制为1.
    :return: DataFrame
    """

    dataSet = pd.read_csv('HalfLoadSet.csv')
    data = dataSet[list(para)]
    differences = data - data.shift(48)
    differences.fillna(method='bfill', axis=0, inplace=True)
    differences.to_csv("Differences-day.csv", index=False)
    differences = differences.abs()
    if plot == 1:
        plot_dif(dataSet=differences)
    diff_des = pd.DataFrame([differences.max(), differences.mean(), differences.std(), differences.quantile(0.80),
                             differences.quantile(0.85), differences.quantile(0.90), differences.quantile(0.95),
                             differences.quantile(0.97), differences.quantile(0.99), differences.quantile(0.995),
                             differences.quantile(0.997), differences.quantile(0.998), differences.quantile(0.9985),
                             differences.quantile(0.999), differences.quantile(0.9995), differences.quantile(0.9999),
                             differences.quantile(0.99995), differences.quantile(0.99999)],
                            index=['max', 'mean', 'std', '80%', '85%', '90%', '95%', '97%', '99%',
                                   '99.5%', '99.7%', '99.8%', '99.85%', '99.9%', '99.95%', '99.99%', '99.995%',
                                   '99.999%'])
    diff_des.T.to_csv('DiffDes-Day.csv')
    print(diff_des.T)
    # print("Describe ##################")
    # print(differences.describe())
    # print("Max ##################")
    # print(differences.max())
    # print("Mean ##################")
    # print(differences.mean())
    # print("Std ##################")
    # print(differences.std())
    # print("Quantile ##################")
    # print(differences.quantile(0.8))
    return differences
    pass


def dif_week(plot, *para):
    """
    收集传入消纳类型（最多9个）相邻一天的负荷差值绝对值.
    对差值做统计学分析.

    :param plot: bool, 是否绘制差异曲线, 绘制为1.
    :return: DataFrame
    """

    dataSet = pd.read_csv('HalfLoadSet.csv')
    data = dataSet[list(para)]
    differences = data - data.shift(336)
    differences.fillna(method='bfill', axis=0, inplace=True)
    differences.to_csv("Differences-week.csv", index=False)
    differences = differences.abs()
    if plot == 1:
        plot_dif(dataSet=differences)
    diff_des = pd.DataFrame([differences.max(), differences.mean(), differences.std(), differences.quantile(0.80),
                             differences.quantile(0.85), differences.quantile(0.90), differences.quantile(0.95),
                             differences.quantile(0.97), differences.quantile(0.99), differences.quantile(0.995),
                             differences.quantile(0.997), differences.quantile(0.998), differences.quantile(0.9985),
                             differences.quantile(0.999), differences.quantile(0.9995), differences.quantile(0.9999),
                             differences.quantile(0.99995), differences.quantile(0.99999)],
                            index=['max', 'mean', 'std', '80%', '85%', '90%', '95%', '97%', '99%',
                                   '99.5%', '99.7%', '99.8%', '99.85%', '99.9%', '99.95%', '99.99%', '99.995%',
                                   '99.999%'])
    diff_des.T.to_csv('DiffDes-Week.csv')
    print(diff_des.T)
    # print("Describe ##################")
    # print(differences.describe())
    # print("Max ##################")
    # print(differences.max())
    # print("Mean ##################")
    # print(differences.mean())
    # print("Std ##################")
    # print(differences.std())
    # print("Quantile ##################")
    # print(differences.quantile(0.8))
    return differences
    pass


def plot_dif(dataSet):
    """
    绘制差异曲线.

    :param data:
    :return:
    """
    columns = dataSet.columns.values[1: 4]
    plt.figure(figsize=[10, 10])
    for column in columns:
        data = dataSet.sort_values(by=[column])
        plt.plot(range(len(data)), data[column], marker='.', label=column)
    plt.title('Differences Curve')
    plt.legend()
    plt.show()


def plot_temperature(**para):
    """
    绘制温度曲线.

    :param para: 收集参数. 可选值为'year', 'month', 'day'. 键的值必须为int类型.
    :return:
    """

    data = pd.read_csv('HalfLoadSet.csv')
    if para.__contains__('year'):
        year = para['year']
        data = data[data.Year == year]
    if para.__contains__('month'):
        month = para['month']
        data = data[data.Month == month]
    if para.__contains__('day'):
        day = para['day']
        data = data[data.Day == day]
    plt.plot(range(len(data.t_10)), data.t_10)
    plt.title('Temperature Curve')
    plt.show()
    pass


def plot_humidity(**para):
    """
    绘制湿度曲线.

    :param para: 收集参数. 可选值为 'year', 'month', 'day'. 键的值必须为int类型.
    :return:
    """

    data = pd.read_csv('HalfLoadSet.csv')
    if para.__contains__('year'):
        year = para['year']
        data = data[data.Year == year]
    if para.__contains__('month'):
        month = para['month']
        data = data[data.Month == month]
    if para.__contains__('day'):
        day = para['day']
        data = data[data.Day == day]
    plt.plot(range(len(data.rh_10)), data.rh_10)
    plt.title('Humidity Curve')
    plt.show()
    pass


def detect_missing_value(dataSet, name='lose_data'):
    """
    负荷缺失值检测. 每半个小时如没有6行数据或者某消纳缺失Value数据则判定为缺失.

    :param dataSet: 数据集.
    :param name: 将缺失的数据信息保存为csv文件的文件名字.
    :return:
    """

    dataSet = dataSet
    lose_data = pd.DataFrame()
    Year = set(dataSet.Year)
    Month = set(dataSet.Month)
    HourSet = set(range(0, 24))
    HalfSet = set([0, 1])
    ESet = set(range(1, 7))
    sumDayItem = 12 * 24
    sumHourItem = 12
    sumHalfItem = 6

    countDay = 0  # the number of day lack of data.
    countHour = 0  # the number of hour lack of data, including lack of total hour or lack of half.
    countHalf = 0  # the number of half lack of data, including lack of total half or lack of columns.
    count = 0
    for year in Year:
        for month in Month:
            df_month = dataSet[(dataSet.Year == year) & (dataSet.Month == month)]
            Day = set(df_month['Day'])
            for day in Day:
                df_day = df_month[df_month.Day == day]
                if sumDayItem == (df_day.Value.notnull() == True).sum():
                    continue
                else:
                    countDay += 1
                    Hour = set(df_day.Hour)
                    # print(year, month, day)
                    for hour in HourSet:
                        if hour not in Hour:
                            countHour += 1
                            lose_data = lose_data.append(
                                pd.DataFrame({'year': year, 'month': month, 'day': day, 'hour': hour, 'half': 0, 'equsid': ESet}), ignore_index=True)
                            lose_data = lose_data.append(
                                pd.DataFrame({'year': year, 'month': month, 'day': day, 'hour': hour, 'half': 1, 'equsid': ESet}), ignore_index=True)
                            print(year, month, day, hour, 'not in')
                            pass
                        else:
                            df_hour = df_day[df_day.Hour == hour]
                            if sumHourItem == (df_hour.Value.notnull() == True).sum():
                                continue
                            else:
                                Half = set(df_hour.Half)
                                # dis = set(df_hour.Equsid[df_hour.Value.isnull() == True])
                                # if genre in dis:
                                # print(year, month, day, hour, dis)
                                for half in HalfSet:
                                    if half not in Half:
                                        count += 6
                                        lose_data = lose_data.append(
                                            pd.DataFrame({'year': year, 'month': month, 'day': day, 'hour': hour, 'half': half,
                                             'equsid': ESet}), ignore_index=True)
                                        print(year, month, day, hour, half, 'not in')
                                        pass
                                    else:
                                        df_half = df_hour[df_hour.Half == half]
                                        if sumHalfItem == (df_half.Value.notnull() == True).sum():
                                            continue
                                        else:
                                            dis = ESet - set(df_half.Equsid[df_half.Value.notnull() == True])
                                            countHalf += 1
                                            lose_data = lose_data.append(
                                                pd.DataFrame({'year': year, 'month': month, 'day': day, 'hour': hour, 'half': half,
                                                 'equsid': dis}), ignore_index=True)
                                            print(year, month, day, hour, half, dis, 'in')
                                            # if genre in dis:
                                            #     print(year, month, day, hour, half, dis)
                                            count += len(dis)
            # print("###", count, "is already down", "###")
    lose_data.to_csv('{}.csv'.format(name), index=False)
    print(countDay)
    print(countHour)
    print(countHalf)
    print(count)


def cluster_analysis(dataSet):
    """
    聚类分析.

    :param dataSet:
    :return:
    """

    # X = dataSet[['Value', 'Tem_max', 'RH_min']].values
    X = dataSet[['F_day1', 'Tem_max', 'RH_min']].values
    scaler = preprocessing.StandardScaler().fit(X)
    X = scaler.transform(X)
    # SSE = []  # 存放每次结果的误差平方和
    # for k in range(1, 9):
    #     estimator = KMeans(n_clusters=k)  # 构造聚类器
    #     estimator.fit(dataSet[['Value', 'Tem_max']])
    #     SSE.append(estimator.inertia_)
    # plt.plot(SSE)
    kmeans = KMeans(n_clusters=3).fit(X)
    joblib.dump(kmeans, 'kmeans.m')
    y_pred = kmeans.predict(X)
    pd.DataFrame({'kmeans': y_pred}).to_csv('kmeans.csv', index=False)
    # plt.scatter(X[:, 0], X[:, 1], c=y_pred)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y_pred)
    ax.set_xlabel('F_day1')
    ax.set_ylabel('Tem_max')
    ax.set_zlabel('RH_min')
    plt.show()
    return kmeans, scaler
    pass


def correlation_coefficient(dataSet):
    """
    统计学分析之相关系数.
    pearson相关系数/spearman秩相关/Kendall Tau相关系数.

    :param dataSet:
    :return:
    """

    print('-------------------------相关系数.\n')
    data = dataSet[['Value', 'Tem_max', 'Tem_min', 'RH_max', 'RH_min', 'Tag', 'Fix', 'kmeans']]
    # pearson相关系数.
    # for e in range(1, 7):
    pearson = data[['Value', 'Tem_max', 'Tem_min', 'RH_max', 'RH_min', 'Tag', 'Fix', 'kmeans']].corr()
    print('### pearson correlation coefficient of Equsid {} ###\n'.format('all'), pearson.round(2))
        # figure = plt.figure(figsize=(12, 8))
        # ax = figure.add_subplot(111)
        # cax = ax.matshow(pearson, vmin=-1, vmax=1)
        # figure.colorbar(cax)
        # plt.show()
    data = dataSet[['Value', 'Tem_max', 'Tem_min', 'RH_max', 'RH_min', 'Tag', 'Fix', 'kmeans']]
    # spearman秩相关.
    # for e in range(1, 7):
    spearman = data[['Value', 'Tem_max', 'Tem_min', 'RH_max', 'RH_min', 'Tag', 'Fix', 'kmeans']].corr('spearman')
    print('### spearman correlation coefficient of Equsid {} ###\n'.format('all'), spearman.round(2))
    # Kendall Tau相关系数.
    data = dataSet[['Day', 'Value', 'dayOfWeek', 'isWorkday', 'isHoliday', 'Season',  'Tag', 'Fix', 'kmeans']]
    # for e in range(1, 7):
    kendall = data[['Value', 'Day', 'dayOfWeek', 'isWorkday', 'isHoliday', 'Season',  'Tag', 'Fix', 'kmeans']].corr('kendall')
    print('### kendall correlation coefficient of Equsid {} ###\n'.format('all'), kendall.round(2))
    pass


def plot_distribution(dataSet, feature='Value'):
    """
    统计学分析之数据分布探索.

    :param dataSet:
    :param eid: 消纳的编号.
    :param feature: 绘图的特征.
    :return:
    """

    # data = dataSet
    # data = dataSet[dataSet.Equsid == eid]
    # 箱型图.
    # dataList = []
    # for h in [0, 1]:
    #     data = dataSet[dataSet.isWorkday == h]
    #     dataList.append(data.Value)
    plt.title('Value of Day Box Graph')
    # plt.text(1, 0, 'not holiday')
    # plt.text(2, 0, 'holiday1')
    # plt.text(3, 0, 'holiday2')
    # plt.boxplot(dataList)
    # 密度图.
    # dataSet['Value'].plot(alpha=0.6, kind='density')
    # 直方图.
    # data[feature].hist(bins=10, normed=True)
    # plt.xlim(0, 1500)
    sns.distplot(dataSet['Value'])
    plt.grid(True)
    # plt.plot(dataSet[feature], marker='.')
    plt.show()
    pass


def extreme_value(dataSet):
    """
    极端值分析.

    :param dataSet:
    :return:
    """
    data = dataSet[['Day', 'Hour', 'Value', 'rh_10', 't_10', 'dayOfWeek', 'isWorkday', 'isHoliday']]
    # pearson = data[data.Value > 800][['Value','Day', 'Hour', 'dayOfWeek', 'isWorkday', 'isHoliday', 'rh_10', 't_10']].corr()
    # print('### pearson correlation coefficient of extreme value ###\n', pearson.round(2))
    # figure = plt.figure(figsize=(12, 8))
    # ax = figure.add_subplot(111)
    # cax = ax.matshow(pearson, vmin=-1, vmax=1)
    # figure.colorbar(cax)
    data = data[data.Value > 800][['Day', 'Hour', 'dayOfWeek', 'isWorkday', 'isHoliday']]
    data.plot(kind='density', subplots=True, figsize=(12, 8))
    # sns.distplot(data)
    plt.show()
    pass


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    start = time.clock()

    # 对不同的原始文件可以用的函数未必一样.
    # dataSet = pd.read_csv('dataSet7.0.csv')
    # dataSet = pd.read_csv('Count_hour.csv')
    # dataSet = pd.read_csv('test_Data2018.csv')
    # dataSet = pd.read_csv('HalfLoadSet.csv')
    # dataSet = pd.read_csv('HalfLoadSet2018.csv')
    dataSet = pd.read_csv('DayLoadSet.csv')

    # -----------------------------生成数据集.
    # createHalfLoadSet(dataSet)
    # createHourLoadSet(dataSet)
    # createDayLoadSet(dataSet)
    # createMonthLoadSet(dataSet)
    # combine_half(dataSet)
    # combine_day(dataSet)
    # -----------------------------绘图精度为半小时的负荷曲线.
    # plot_half_year(dataSet, eid=1)
    # plot_half_month(dataSet, month=1, eid=1)
    # plot_half_week(dataSet, month=1, day=1, eid=1)
    # plot_half_day(dataSet, month=4, day=22, eid=1)
    # -----------------------------绘图精度为半小时的负荷曲线.
    # plot_hour_year(dataSet)
    # plot_hour_month(dataSet)
    # plot_hour_week(dataSet)
    # plot_hour_day(dataSet)
    # -----------------------------绘图精度为一天的负荷曲线.
    # plot_day_year(dataSet)
    # plot_day_month(dataSet)
    # -----------------------------绘图精度为一个月的负荷曲线.
    # plot_month_year(dataSet)
    # -----------------------------绘图精度为半小时的节假日数据.
    # plot_holiday(dataSet)
    # -----------------------------同时刻的负荷差异对比.
    # dif_half(1, 'Value11', 'Value21', 'Value22', 'Value23', 'Value31',
    #                 'Value32', 'Value1', 'Value2', 'Value3', 't_10', 'rh_10')
    # dif_day(1, 'Value11', 'Value21', 'Value22', 'Value23', 'Value31',
    #                 'Value32', 'Value1', 'Value2', 'Value3', 't_10', 'rh_10')
    # dif_week(1, 'Value11', 'Value21', 'Value22', 'Value23', 'Value31',
    #                 'Value32', 'Value1', 'Value2', 'Value3', 't_10', 'rh_10')
    # -----------------------------绘制气候数据图.
    # plot_temperature(year=2016, month=2, day=22)
    # plot_humidity(year=2016, month=2, day=22)
    # accTem_effect(dataSet)
    # -----------------------------负荷缺失值检测.
    # dataSet = pd.read_csv('test_Data2018.csv')
    # detect_missing_value(dataSet, genre=2)
    # -----------------------------聚类分析.
    # dataSet = pd.read_csv('DataSet7.0.csv')
    # kmeans, scaler = cluster_analysis(dataSet)
    # DayLoadSet2018 = pd.read_csv('DayLoadSet2018.csv')
    # X = DayLoadSet2018[['Value', 'Tem_max', 'Tem_min', 'RH_max', 'RH_min']]
    # print(X.shape)
    # X = scaler.transform(X)
    # pre = kmeans.predict(X)
    # data = pd.DataFrame({'pre': pre})
    # print(len(pre))
    # data.to_csv('kmeans2018.csv', index=False)
    # -----------------------------统计学分析.
    # dataSet = pd.read_csv('DayLoadSet.csv')
    # print(dataSet.Value.describe())
    correlation_coefficient(dataSet)
    # print(dataSet.Value.describe())
    # plot_distribution(dataSet, feature=['Value', 'dayOfWeek', 'isHoliday', 'isWorkday'])
    # extreme_value(dataSet)
    end = time.clock()
    print(end - start)
