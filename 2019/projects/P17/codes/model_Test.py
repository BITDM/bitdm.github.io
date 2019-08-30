# -- coding:utf-8 --

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor, RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet, HuberRegressor
from sklearn.neighbors import KNeighborsRegressor, RadiusNeighborsRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn import preprocessing
import warnings

############# 功能说明 #############

# -----------------------------基础函数.
#   loadData()
#   monthScore(model, X_test, y_true)
#   normorlization(X)
# -----------------------------机器学习模型.
#   linearModel(norm=0)
#   knnModel(norm=1)
#   svmModel(norm=1)
#   ensembleModel(norm=0)

def loadData():
    """
    加载数据集, 返回用于交叉验证的(X, Y).

    :return: (X, Y)
    """

    dataSet = pd.read_csv('DayLoadSet.csv')
    # data = dataSet[dataSet.Equsid == 3]
    data = dataSet
    # X = data[['isHoliday', 'isWorkday', 'dayOfWeek', 'Season',
    #           'Tem_max', 'Tem_min', 'Tem_mean', 'Tem_std', 'RH_max', 'RH_min', 'RH_mean',
    #           'RH_std', 'Precipitation']]
    X = data[['F_day1', 'F_day2', 'F_day3', 'F_week', 'dayOfWeek',
                    'isHoliday', 'isWorkday','Tem_max', 'Tem_min', 'RH_max', 'RH_min', 'Tag']]
    Y = data['Value']

    return X, Y

def monthScore(model, X_test, y_true):
    """
    一个用于评价模型的MAPE计算函数.
    是对整体求和的单值MAPE, 而非MAPE的平均值.

    :param model:
    :param X_test:
    :param y_true:
    :return: MAPE
    """
    y_pre = np.array(model.predict(X_test)).ravel()
    y_true = np.array(y_true).ravel()
    return abs(y_pre.sum() - y_true.sum())/y_true.sum()

def normorlization(X):
    """
    归一化函数. 返回归一化的特征数组及归一化模型.
    这里只执行Z-score归一化.

    :param X: 特征数组. array or DataFrame.
    :return: (X. scaler)
    """

    scaler = preprocessing.StandardScaler()
    scaler.fit(X)
    X = scaler.transform(X)

    return X, scaler
    pass

def linearModel(norm=1):
    """
    线性模型. 包括了线性回归、Lasso回归和岭回归.

    :param norm: 是否需归一化处理. 归一化为1, 否则为0.
    :return:
    """

    print('\n！！！ Welcome to Linear Model discovery hall ！！！\n')
    X, y = loadData()
    print('The features used are :')
    print(X.columns.values)
    if norm == 1:
        X, scaler = normorlization(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    Linear_parameters = {'normalize': [True, False]}
    clf = GridSearchCV(LinearRegression(), Linear_parameters, scoring='r2', cv=10)
    clf.fit(X_train, y_train)
    print('\n######### The result of Linear regression #########')
    print("Best parameters set found:", clf.best_params_)
    print("Best score found: ", clf.best_score_)
    print("Optimized Score R2:", clf.score(X_test, y_test))
    print("Optimized Score MAPE:", monthScore(clf, X_test, y_test))
    print("Best linear model parameter:", clf.best_estimator_.coef_)
    # plt.plot(range(len(y_test[0: 288])), clf.predict(X_test)[0: 288], label='pre')
    # plt.plot(range(len(y_test[0: 288])), y_test[0: 288], label='true')
    # plt.legend()
    # plt.show()

    # Lasso_parameters = {'normalize': [True, False], 'alpha': [0.01, 0.05, 0.1, 0.2, 0.4, 0.8, 1]}
    # clf = GridSearchCV(Lasso(), Lasso_parameters, scoring='r2', cv=10)
    # clf.fit(X_train, y_train)
    # print('\n######### The result of Lasso regression #########')
    # print("Best parameters set found:", clf.best_params_)
    # print("Best score found: ", clf.best_score_)
    # print("Optimized Score R2:", clf.score(X_test, y_test))
    # print("Optimized Score MAPE:", monthScore(clf, X_test, y_test))
    # print("Best linear model parameter:", clf.best_estimator_.coef_)
    # print('Actual number of iterations:', clf.best_estimator_.n_iter_)

    # Ridge_parameters = {'normalize': [True, False], 'alpha': [0.01, 0.05, 0.1, 0.2, 0.4, 0.8, 1]}
    # clf = GridSearchCV(Ridge(), Ridge_parameters, scoring='r2', cv=10)
    # clf.fit(X_train, y_train)
    # print('\n######### The result of Ridge regression #########')
    # print("Best parameters set found:", clf.best_params_)
    # print("Best score found: ", clf.best_score_)
    # print("Optimized Score R2:", clf.score(X_test, y_test))
    # print("Optimized Score MAPE:", monthScore(clf, X_test, y_test))
    # print("Best linear model parameter:", clf.best_estimator_.coef_)
    # print('Actual number of iterations:', clf.best_estimator_.n_iter_)

    ElasticNet_parameters = {'normalize': [True, False], 'alpha': [0.01, 0.05, 0.1, 0.2, 0.4, 0.8, 1],
                             'l1_ratio': [0.1, 0.2, 0.4, 0.6, 0.8, 0.9]}
    clf = GridSearchCV(ElasticNet(), ElasticNet_parameters, scoring='r2', cv=10)
    clf.fit(X_train, y_train)
    print('\n######### The result of ElasticNet regression #########')
    print("Best parameters set found:", clf.best_params_)
    print("Best score found: ", clf.best_score_)
    print("Optimized Score R2:", clf.score(X_test, y_test))
    print("Optimized Score MAPE:", monthScore(clf, X_test, y_test))
    print("Best linear model parameter:", clf.best_estimator_.coef_)
    print('Actual number of iterations:', clf.best_estimator_.n_iter_)

    # Huber_parameters = {'alpha': [0.01, 0.05, 0.1, 0.2, 0.4, 0.8, 1],
    #                              'epsilon': [1.1, 1.2, 1.35, 1.5, 1.8, 2, 2.5, 3]}
    # clf = GridSearchCV(HuberRegressor(), Huber_parameters, scoring='r2', cv=10)
    # clf.fit(X_train, y_train)
    # print('\n######### The result of Huber regression #########')
    # print("Best parameters set found:", clf.best_params_)
    # print("Best score found: ", clf.best_score_)
    # print("Optimized Score R2:", clf.score(X_test, y_test))
    # print("Optimized Score MAPE:", monthScore(clf, X_test, y_test))
    # print("Best linear model parameter:", clf.best_estimator_.coef_)
    # print('Actual number of iterations:', clf.best_estimator_.n_iter_)

def knnModel(norm=1):
    """
    KNN模型. 包括了限定邻居数的最近邻回归与限定半径的最近邻回归.

    :param norm: 是否需归一化处理. 归一化为1, 否则为0.
    :return:
    """

    print('\n！！！ Welcome to KNN Model discovery hall ！！！\n')
    X, y = loadData()
    print('The features used are :')
    print(X.columns.values)
    if norm == 1:
        X, scaler = normorlization(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    KNN_parameter = {'n_neighbors': [25, 30, 40, 10, 15, 45, 50, 80], 'weights': ['uniform', 'distance'],
                    'p': [1, 2]}
    clf = GridSearchCV(KNeighborsRegressor(), KNN_parameter, scoring='r2', cv=6)
    clf.fit(X_train, y_train)
    print('\n######### The result of KNN regression #########')
    print("Best parameters set found:", clf.best_params_)
    print("Best score found: ", clf.best_score_)
    print("Optimized Score R2:", clf.score(X_test, y_test))
    print("Optimized Score MAPE:", monthScore(clf, X_test, y_test))

    # RN_parameter = {'radius': [0.1, 1.5, 1.2, 0.2, 0.4, 0.8, 1], 'weights': ['uniform', 'distance'],
    #                  'p': [1, 2]}
    # clf = GridSearchCV(RadiusNeighborsRegressor(), RN_parameter, scoring='r2', cv=6)
    # clf.fit(X_train, y_train)
    # print('\n######### The result of RN regression #########')
    # print("Best parameters set found:", clf.best_params_)
    # print("Best score found: ", clf.best_score_)
    # print("Optimized Score R2:", clf.score(X_test, y_test))
    # print("Optimized Score MAPE:", monthScore(clf, X_test, y_test))

def svmModel(norm=1):
    """
     SVM模型. 包括了SVR.

     :param norm: 是否需归一化处理. 归一化为1, 否则为0.
     :return:
     """

    print('\n！！！ Welcome to SVM model discovery hall ！！！\n')
    X, y = loadData()
    print('The features used are :')
    print(X.columns.values)
    if norm == 1:
        X, scaler = normorlization(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    SVR_parameter = {'kernel': ['linear', 'poly', 'rbf', 'sigmoid', 'precomputed'],
                     'degree': [1, 2, 3, 4, 5], 'C': [0.8, 1, 1.2, 1.5, 2, 2.5, 3]}
    clf = GridSearchCV(SVR(), SVR_parameter, scoring='r2', cv=6)
    clf.fit(X_train, y_train)
    print('\n######### The result of SVR regression #########')
    print("Best parameters set found:", clf.best_params_)
    print("Best score found: ", clf.best_score_)
    print("Optimized Score R2:", clf.score(X_test, y_test))
    print("Optimized Score MAPE:", monthScore(clf, X_test, y_test))
    print('Support vectors:', clf.best_estimator_.support_vectors_)

def ensembleModel(norm=0):

    print('\n！！！ Welcome to Ensemble Model discovery hall ！！！\n')
    X, y = loadData()
    print('The features used are :')
    print(X.columns.values)
    if norm == 1:
        X, scaler = normorlization(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    Ada_parameter = {'n_estimators': [250, 260, 270, 280, 290], 'loss': ['linear', 'square', 'exponential'],
                     'learning_rate': [0.01, 0.1, 0.2, 0.4, 0.8, 1]}
    clf = GridSearchCV(AdaBoostRegressor(DecisionTreeRegressor(max_features='sqrt')), Ada_parameter, scoring='r2', cv=6)
    clf.fit(X_train, y_train)
    print('\n######### The result of Adaboost regression #########')
    print("Best parameters set found:", clf.best_params_)
    print("Best score found: ", clf.best_score_)
    print("Optimized Score R2:", clf.score(X_test, y_test))
    print("Optimized Score MAPE:", monthScore(clf, X_test, y_test))
    print("Best adaboost model parameter :", clf.best_estimator_.feature_importances_)

    RF_parameter = {'n_estimators': [225, 230, 240, 250, 265, 275]}
    clf = GridSearchCV(RandomForestRegressor(DecisionTreeRegressor(), max_features='sqrt'), RF_parameter, scoring='r2', cv=6)
    clf.fit(X_train, y_train)
    print('\n######### The result of Random Forest regression #########')
    print("Best parameters set found:", clf.best_params_)
    print("Best score found: ", clf.best_score_)
    print("Optimized Score R2:", clf.score(X_test, y_test))
    print("Optimized Score MAPE:", monthScore(clf, X_test, y_test))
    print("Best RF model parameter :", clf.best_estimator_.feature_importances_)

    GBDT_parameter = {'loss': ['ls', 'lad', 'huber', 'quantile'], 'n_estimators': [45, 50, 55, 60, 65, 70, 80],
                      'learning_rate': [0.01, 0.1, 0.2, 0.4, 0.8, 1]}
    clf = GridSearchCV(GradientBoostingRegressor(DecisionTreeRegressor(), max_features='sqrt'), GBDT_parameter, scoring='r2', cv=6)
    clf.fit(X_train, y_train)
    print('\n######### The result of GBDT regression #########')
    print("Best parameters set found:", clf.best_params_)
    print("Best score found: ", clf.best_score_)
    print("Optimized Score R2:", clf.score(X_test, y_test))
    print("Optimized Score MAPE:", monthScore(clf, X_test, y_test))
    print("Best GBDT model parameter :", clf.best_estimator_.feature_importances_)


if __name__ == "__main__":
    warnings.filterwarnings('ignore')

    # linearModel(norm=1)
    # knnModel(norm=1)
    # svmModel(norm=1)
    ensembleModel(norm=0)

