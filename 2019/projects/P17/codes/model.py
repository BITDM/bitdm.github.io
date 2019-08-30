# -- coding:utf-8 --

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor, RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import r2_score
from sklearn import preprocessing
import tensorflow as tf
from sklearn.externals import joblib
import time as time
import warnings


############# 功能说明 #############
直接运行此文件，将会输出R²、total MAPE、mean MAPE。

# -----------------------------基础函数.
#   load_train_data(dataSet)
#   load_test_data(dataSet)
#   day_MAPE(model, X_test, y_true)
#   normorlization(X)
# -----------------------------机器学习模型.
#   generate_model(model, trainSet, testSet, norm=1, name='linear')

def load_train_data(dataSet):
    """
    加载用于训练的数据集, 返回(X_train, y_train).

    :return: (X_train, y_train)
    X_train: type of DataFrame.
    y_train: type of Series.

    """

    # dataSet = pd.read_csv('DataSet7.0.csv')
    # data = dataSet[dataSet.Equsid == 3]
    # data = dataSet
    # X = data[['isHoliday', 'isWorkday', 'dayOfWeek', 'Season',
    #           'Tem_max', 'Tem_min', 'Tem_mean', 'Tem_std', 'RH_max', 'RH_min', 'RH_mean',
    #           'RH_std', 'Precipitation']]
    # X_train = data[['Month', 'Day', 'Hour', 'Half', 'Equsid', 'F_half', 'F_day', 'F_week', 'dayOfWeek',
    #                 'isHoliday', 'isWorkday', 'Season', 't_10', 'rh_10']]
    # y_train = data['Value']
    # X_train = data[['Month', 'Day', 'Hour', 'Half', 'Equsid', 'dayOfWeek',
    #                 'isHoliday', 'isWorkday', 'Season', 't_10', 'rh_10']]
    # y_train = data['Value']
    X_train = dataSet[['Month', 'Day', 'F_day1', 'F_day2', 'F_day3', 'F_week', 'dayOfWeek',
                    'isHoliday', 'isWorkday', 'Tem_max', 'Tem_min', 'RH_max', 'RH_min', 'Tag']]
    y_train = dataSet['Value']

    return X_train, y_train


def load_test_data(dataSet):
    """
    加载用于测试的数据集, 返回(X_test, y_test, dataSet).

    :return: (X_test, y_test, dataSet)
    X_test: type of DataFrame.
    y_test: type of array.
    dataSet: type of DataFrame.

    """

    X_test = dataSet[['Month', 'Day', 'F_day1', 'F_day2', 'F_day3', 'F_week', 'dayOfWeek',
                    'isHoliday', 'isWorkday', 'Tem_max', 'Tem_min', 'RH_max', 'RH_min', 'Tag']]
    y_true = dataSet['Value']

    return X_test, y_true, dataSet


def day_MAPE(y_pre, y_true, name):
    """
    一个用于评价模型的MAPE计算函数.
    计算每天的MAPE, 月MAPE, 日MAPE绝对值的均值.

    :param y_pre: 预测值.
    :param y_true: 真实值.
    :param name: 模型的名字. 可选择为'adaboost', 'rf', 'gbdt'.
    :return: Mape: 月MAPE
            mape_mean: 日MAPE绝对值的均值.
    """

    mape = (y_pre - y_true) / y_true
    Mape = (y_pre - y_true).sum() / y_true.sum()
    mape_mean = (abs((y_pre - y_true)) / y_true).mean()

    # m1 = (y_pre[:31] - y_true[:31]).sum() / y_true[:31].sum()
    # m2 = (y_pre[31:59] - y_true[31:59]).sum() / y_true[31:59].sum()
    # m3 = (y_pre[59:90] - y_true[59:90]).sum() / y_true[59:90].sum()
    # m4 = (y_pre[90:120] - y_true[90:120]).sum() / y_true[90:120].sum()
    # m5 = (y_pre[120:151] - y_true[120:151]).sum() / y_true[120:151].sum()
    # plt.figure()
    # plt.plot(mape, marker='.')
    # plt.plot(range(len(mape)), len(mape)*[Mape], ls='--', label='total: {}'.format(Mape))
    # plt.plot(range(0,31), 31 * [m1], ls='--', label='1: {:.4f}'.format(m1))
    # plt.plot(range(31,59), 28 * [m2], ls='--', label='2: {:.4f}'.format(m2))
    # plt.plot(range(59,90), 31 * [m3], ls='--', label='3: {:.4f}'.format(m3))
    # plt.plot(range(90,120), 30 * [m4], ls='--', label='4: {:.4f}'.format(m4))
    # plt.plot(range(120,151), 31 * [m5], ls='--', label='5: {:.4f}'.format(m5))
    # plt.title('The MAPE Curve of {0} days from {1} model'.format(151, name))
    # plt.legend()
    # plt.grid(True)
    # plt.show()
    # setpath = './graph/' + name + '.png'
    # plt.savefig(setpath)
    print('mmm', mape_mean)
    return Mape, mape_mean


def normalization(X):
    """
    归一化函数. 返回归一化的特征数组及归一化模型.
    这里只执行Z-score归一化.

    :param X: 特征数组. array or DataFrame.
    :return: (X. scaler)
    """

    scalar = preprocessing.StandardScaler()
    scalar.fit(X)
    X = scalar.transform(X)

    return X, scalar


def generate_model(model, trainSet, testSet, norm=1, name='linear'):
    """
    训练模型.

    :param model: 用于训练的模型.
    :param trainSet: 训练集.
    :param testSet: 测试集.
    :param norm: 是否需归一化处理. 归一化为1, 否则为0.
    :param name: 模型的名字. 可选择为'linear', 'knn', 'svr', 'adaboost', 'rf', 'gbdt'.
    :return: y_pre: 模型的预测值.
    """

    print('\n！！！ Welcome to Verify Model discovery hall ！！！\n')
    # 加载数据.
    X_train, y_train = load_train_data(trainSet)
    X_test, y_true, testSet = load_test_data(testSet)
    print('The features used are :')
    print(X_train.columns.values)
    # 训练集特征归一化.
    if norm == 1:
        X_train, scalar = normalization(X_train)
    # 遍历预测.
    length = len(trainSet)
    data = trainSet.loc[length - 7:]
    data = data.append(testSet, ignore_index=True)
    start = time.clock()
    model.fit(X_train, y_train)
    end = time.clock()
    print('Time of {} model for fitting: '.format(name), end - start)
    # 保存模型.
    start = time.clock()
    setpath = name + ".m"
    joblib.dump(model, setpath)
    for index in range(len(X_test)):
        # 填充4列特征.
        data.F_day1.iloc[index + 7] = data.Value.iloc[index + 7 - 1]
        data.F_day2.iloc[index + 7] = data.Value.iloc[index + 7 - 2]
        data.F_day3.iloc[index + 7] = data.Value.iloc[index + 7 - 3]
        data.F_week.iloc[index + 7] = data.Value.iloc[index]
        X_test.F_day1.iloc[index] = data.Value.iloc[index + 7 - 1]
        X_test.F_day2.iloc[index] = data.Value.iloc[index + 7 - 2]
        X_test.F_day3.iloc[index] = data.Value.iloc[index + 7 - 3]
        X_test.F_week.iloc[index] = data.Value.iloc[index]
        # 归一化
        if norm == 1:
            X = scalar.transform(X_test.iloc[index].values.reshape(1, -1))
        else:
            X = X_test.iloc[index].values.reshape(1, -1)
        # 预测
        y = model.predict(X)
        data.Value.iloc[index + 7] = y
        # if index > 0 and index % 288 == 0:
        #     print("{} day has already finished".format(index / 288))
    end = time.clock()
    print('Time of {} model for predicting: '.format(name), end - start)
    # 装载预测结果.
    y_pre = data.Value.iloc[7:].values
    # 保存误差数据, 用于后续分析.
    data = pd.DataFrame({'y_true': y_true, 'y_pre': y_pre})
    data.to_csv('{}.csv'.format(name), index=False)
    # 打印结果.
    print('\n######### The result of {} model #########'.format(name))
    print("The parameters are: ", model.get_params())
    print("Optimized Score R2: ", r2_score(y_true, y_pre))
    print("Optimized Score Total MAPE: ", day_MAPE(y_pre, y_true, name)[0])
    print("Optimized Score Mean MAPE: ", day_MAPE(y_pre, y_true, name)[1])
    if name == 'linear' or name == 'ElasticNet':
        print("Linear model coefficient: ", model.coef_)
    if name == 'knn':
        pass
    if name == 'svr':
        print('Support vectors are: ', model.support_vectors_)
    if name == 'adaboost' or name == 'rf' or name == 'gbdt':
        print("Ensemble model features selection: ", model.feature_importances_)

    return y_pre


def model_merge(pre_ada, pre_rf, pre_gbdt, pre_lstm):
    """
    模型融合.

    :param pre_ada: Adaboost算法的输出值.
    :param pre_rf: RF算法的输出值.
    :param pre_gbdt: GBDT算法的输出值.
    :param pre_lstm: LSTM算法的输出值.
    :return:
    """

    return ((-0.025) * pre_ada + 0.31 * pre_rf + 0.88 * pre_gbdt + (-0.12) * pre_lstm)


def get_train_data(batch_size, time_step, data_train):
    batch_index = []
    # data_train=data[train_begin:train_end]
    normalized_train_data = (data_train - np.mean(data_train, axis=0)) / np.std(data_train, axis=0)
    train_x, train_y = [], []
    for i in range(len(normalized_train_data) - time_step):
        if i % batch_size == 0:
            batch_index.append(i)
        x = normalized_train_data[i:i + time_step, :10]
        # print(x)
        y = normalized_train_data[i:i + time_step, 10, np.newaxis]
        # print(y)
        train_x.append(x.tolist())
        train_y.append(y.tolist())
    batch_index.append((len(normalized_train_data) - time_step))
    return batch_index, train_x, train_y


# 获取测试集
def get_test_data(time_step, data_test):
    mean = np.mean(data_test, axis=0)
    std = np.std(data_test, axis=0)
    normalized_test_data = (data_test - mean) / std
    size = (len(normalized_test_data) + time_step - 1) // time_step  # 有size个sample
    test_x, test_y = [], []
    for i in range(size - 1):
        x = normalized_test_data[i * time_step:(i + 1) * time_step, :10]
        y = normalized_test_data[i * time_step:(i + 1) * time_step, 10]
        test_x.append(x.tolist())
        test_y.extend(y)
    return mean, std, test_x, test_y


# ——————————————————定义神经网络变量——————————————————
def lstm(X):
    # ——————————————————定义神经网络变量——————————————————
    # 输入层、输出层权重、偏置
    weights = {
        'in': tf.Variable(tf.random_normal([input_size, rnn_unit])),
        'out': tf.Variable(tf.random_normal([rnn_unit, 1]))
    }
    biases = {
        'in': tf.Variable(tf.constant(0.1, shape=[rnn_unit, ])),
        'out': tf.Variable(tf.constant(0.1, shape=[1, ]))
    }
    batch_size = tf.shape(X)[0]
    time_step = tf.shape(X)[1]
    w_in = weights['in']
    b_in = biases['in']
    input = tf.reshape(X, [-1, input_size])
    input_rnn = tf.matmul(input, w_in) + b_in
    input_rnn = tf.reshape(input_rnn, [-1, time_step, rnn_unit])
    cell = tf.nn.rnn_cell.BasicLSTMCell(rnn_unit)
    cell = tf.nn.rnn_cell.DropoutWrapper(cell, output_keep_prob=0.8)
    init_state = cell.zero_state(batch_size, dtype=tf.float32)
    output_rnn, final_states = tf.nn.dynamic_rnn(cell, input_rnn, initial_state=init_state, dtype=tf.float32)
    output = tf.reshape(output_rnn, [-1, rnn_unit])
    w_out = weights['out']
    b_out = biases['out']
    pred = tf.matmul(output, w_out) + b_out
    return pred, final_states


# ——————————————————训练模型——————————————————
def train_lstm(batch_size, time_step, train_data_):  # batch_size=60,time_step=15
    X = tf.placeholder(tf.float32, shape=[None, time_step, input_size])
    Y = tf.placeholder(tf.float32, shape=[None, time_step, output_size])
    batch_index, train_x, train_y = get_train_data(batch_size, time_step, train_data_)
    pred, _ = lstm(X)
    # loss = tf.sqrt(tf.losses.mean_squared_error(tf.reshape(pred,[-1]),tf.reshape(Y, [-1]))) # rmse
    loss = tf.losses.mean_squared_error(tf.reshape(pred, [-1]), tf.reshape(Y, [-1]))  # mse
    train_op = tf.train.AdamOptimizer(lr).minimize(loss)
    saver = tf.train.Saver(tf.global_variables(), max_to_keep=15)  # 保存最近的15个模型
    # module_file = tf.train.latest_checkpoint()
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        # saver.restore(sess, module_file)
        minn = 1000
        for i in range(201):
            for step in range(len(batch_index) - 1):
                _, loss_ = sess.run([train_op, loss], feed_dict={X: train_x[batch_index[step]:batch_index[step + 1]],
                                                                 Y: train_y[batch_index[step]:batch_index[step + 1]]})
            print(i, loss_, minn)
            if min(loss_, minn) == loss_:
                print("保存模型：", saver.save(sess, 'model_file5' + os.sep + '/stock2.model', global_step=i))
            if min(loss_, minn) < 0.02:
                print("保存模型：", saver.save(sess, 'model_file_1' + os.sep + '/stock2.model', global_step=i))
            minn = min(loss_, minn)


# ————————————————预测模型————————————————————
def prediction(time_step, data_test):
    # def prediction(time_step=36):
    X = tf.placeholder(tf.float32, shape=[None, time_step, input_size])
    # Y=tf.placeholder(tf.float32, shape=[None,time_step,output_size])
    mean, std, test_x, test_y = get_test_data(time_step, data_test)
    pred, _ = lstm(X)
    saver = tf.train.Saver(tf.global_variables())
    with tf.Session() as sess:
        # 参数恢复
        module_file = tf.train.latest_checkpoint('model_file5' + os.sep)
        saver.restore(sess, module_file)
        test_predict = []
        for step in range(len(test_x)):
            prob = sess.run(pred, feed_dict={X: [test_x[step]]})
            predict = prob.reshape((-1))
            test_predict.extend(predict)
        test_y = np.array(test_y) * std[10] + mean[10]
        test_predict = np.abs(np.array(test_predict) * std[10] + mean[10])
        test_day = []
        test_pre = []
        for i in range(len(test_y) // 48):
            test_day.append(np.sum(test_y[i * 48:(i + 1) * 48]))
        for i in range(len(test_y) // 48):
            test_pre.append(np.sum(test_predict[i * 48:(i + 1) * 48]))
        datafra = pd.DataFrame({'value': test_pre})
        # 将DataFrame存储为csv,index表示是否显示行名，default=True
        datafra.to_csv(csv_name, index=False, sep=',')

        plt.plot(list(range(len(test_predict))), test_predict, label='prediction', linewidth=1.5, marker='o',
                 markersize=5, color='r')
        plt.plot(list(range(len(test_y))), test_y, label='true', linewidth=1.5, marker='*', markersize=5, color='c')
        plt.xlabel('day')
        plt.ylabel('value')
        plt.title('prediction of days')
        plt.legend()
        plt.show()

        # 输出每天的MAPE
        MAPE = []
        for i in range(len(test_y) // 48):
            MAPE.append(
                np.abs(np.sum(test_y[i * 48:(i + 1) * 48]) - np.sum(test_predict[i * 48:(i + 1) * 48])) / np.sum(
                    test_y[i * 48:(i + 1) * 48]) * 100)
        MAPE_meanday = np.mean(MAPE)
        print("MAPE:", MAPE_meanday, "%")
        print("sum_test", np.sum(test_y))
        print("sum_pred", np.sum(test_predict))

        return test_pre


def train(train_data_, data_test):
    with tf.variable_scope('train'):
        train_lstm(60, 15, train_data_)

    with tf.variable_scope('train', reuse=True):
        return prediction(1, data_test)


if __name__ == "__main__":
    warnings.filterwarnings('ignore')

    df = pd.read_csv("./Finaday.csv")
    data=df.iloc[:35088,1:].values
    data_test=df.iloc[35087:,1:].values
    global rnn_unit,input_size,output_size,lrcsv_name
    tf.reset_default_graph()
    rnn_unit= 12
    input_size=10
    output_size=1
    lr=0.0006
    csv_name='lstm.csv'
    pre_lstm = train(data,data_test)

    trainSet = pd.read_csv('DayLoadSet.csv')
    testSet = pd.read_csv('DayLoadSet2018.csv')
    true = testSet.Value.values.reshape(1, -1)

    model = AdaBoostRegressor(DecisionTreeRegressor(max_features='sqrt'), n_estimators=260, learning_rate=0.8,
                              loss='exponential')
    pre_ada = generate_model(model=model, trainSet=trainSet.copy(), testSet=testSet.copy(), norm=0, name='adaboost')

    model = RandomForestRegressor(n_estimators=240, max_features='sqrt')
    pre_rf = generate_model(model=model, trainSet=trainSet.copy(), testSet=testSet.copy(), norm=0, name='rf')

    model = GradientBoostingRegressor(alpha=0.9, n_estimators=80, learning_rate=0.2, loss='lad')
    pre_gbdt = generate_model(model=model, trainSet=trainSet.copy(), testSet=testSet.copy(), norm=0, name='gbdt')

    pre = model_merge(pre_ada, pre_rf, pre_gbdt, pre_lstm)
    print("Optimized Score R2: ", r2_score(true, pre))
    print("Optimized Score Total MAPE: ", day_MAPE(pre, true, 'final model')[0])
    print("Optimized Score Mean MAPE: ", day_MAPE(pre, true, 'final model')[1])