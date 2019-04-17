import numpy as np
from DataStructure import DataStructure
import RandomForest
import AdaboostClassifier
import NeuralNetwork, KNN, LogisticRegression, DecisionTree

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier

from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

import matplotlib.pyplot as plt
from sklearn.metrics import zero_one_loss

from sklearn.metrics import confusion_matrix


rng = np.random.RandomState()


def RFShow(DS):
    n_estimators = 100
    RF_parameter = {"n_estimators": 10,
                    "max_depth": 2,
                    "random_state": 0,
                    "min_samples_leaf": 5}
    fig = plt.figure()
    ax = fig.add_subplot(211)
    for md in [2, 3, 4, 5]:
        train_score = []
        test_score = []
        RF_parameter["max_depth"] = md
        for i in range(n_estimators):
            RF_parameter["n_estimators"] = i + 1
            RandomForest.random_forest(DS, RF_parameter, train_score, test_score)
        ax.plot(train_score, label="train score, max_depth="+str(md), color=(0.0, 0.1 + md*0.15, 0.0))
        ax.plot(test_score, label="test score, max_depth="+str(md), color=(1.0, 0.1 + md*0.15, 1.0))
    # ax.set_ylim((0.0, 0.5))
    ax.set_xlabel('n_estimators')
    ax.set_ylabel('accurate')
    leg = ax.legend(loc='upper right', fancybox=True)
    leg.get_frame().set_alpha(0.7)

    ax = fig.add_subplot(212)
    RF_parameter["max_depth"] = 4
    for msl in [2, 4, 6, 8, 10]:
        train_score = []
        test_score = []
        RF_parameter["min_samples_leaf"] = msl
        for i in range(n_estimators):
            RF_parameter["n_estimators"] = i + 1
            RandomForest.random_forest(DS, RF_parameter, train_score, test_score)
        ax.plot(train_score, label="train score, min_samples_leaf="+str(msl), color=(0.0, msl*0.1-0.2, 0.0))
        ax.plot(test_score, label="test score, min_samples_leaf="+str(msl), color=(1.0, msl*0.1-0.2, 1.0))
    # ax.set_ylim((0.0, 0.5))
    ax.set_xlabel('n_estimators')
    ax.set_ylabel('accurate')
    leg = ax.legend(loc='upper right', fancybox=True)
    leg.get_frame().set_alpha(0.7)

    plt.show()


def ABCShow(DS):
    ABC_parameter = {"max_depth": 2,
                     "min_samples_leaf": 20,
                     "n_estimators": 200,
                     "random_state": 0,
                     "learning_rate": 0.1,
                     "algorithm": "SAMME.R"}
    fig = plt.figure()
    ax = fig.add_subplot(311)
    for md in [1, 2, 3, 4, 5]:
        train_score = []
        test_score = []
        ABC_parameter["max_depth"] = md
        AdaboostClassifier.adaboost_classifier(DS, ABC_parameter, train_score, test_score)
        ax.plot(train_score, label="train score, max_depth=" + str(md), color=(0.0, -0.1 + md * 0.2, 0.0))
        ax.plot(test_score, label="test score, max_depth=" + str(md), color=(1.0, -0.1 + md * 0.2, 1.0))
    # ax.set_ylim((0.0, 0.5))
    ax.set_xlabel('n_estimators')
    ax.set_ylabel('accurate')
    leg = ax.legend(loc='upper right', fancybox=True)
    leg.get_frame().set_alpha(0.7)

    ax = fig.add_subplot(312)
    ABC_parameter["max_depth"] = 2
    for msl in [10, 20, 30, 40]:
        train_score = []
        test_score = []
        ABC_parameter["min_samples_leaf"] = msl
        AdaboostClassifier.adaboost_classifier(DS, ABC_parameter, train_score, test_score)
        ax.plot(train_score, label="train score, min_samples_leaf=" + str(msl), color=(0.0, msl * 0.025 - 0.2, 0.0))
        ax.plot(test_score, label="test score, min_samples_leaf=" + str(msl), color=(1.0, msl * 0.025 - 0.2, 1.0))
    # ax.set_ylim((0.0, 0.5))
    ax.set_xlabel('n_estimators')
    ax.set_ylabel('accurate')
    leg = ax.legend(loc='upper right', fancybox=True)
    leg.get_frame().set_alpha(0.7)

    ax = fig.add_subplot(313)
    ABC_parameter["max_depth"] = 2
    ABC_parameter["min_samples_leaf"] = 20
    for lr in [0.1, 0.2, 0.3, 0.4]:
        train_score = []
        test_score = []
        ABC_parameter["learning_rate"] = lr
        AdaboostClassifier.adaboost_classifier(DS, ABC_parameter, train_score, test_score)
        ax.plot(train_score, label="train score, learning_rate=" + str(lr), color=(0.0, lr * 2 - 0.2, 0.0))
        ax.plot(test_score, label="test score, learning_rate=" + str(lr), color=(1.0, lr * 2 - 0.2, 1.0))
    # ax.set_ylim((0.0, 0.5))
    ax.set_xlabel('n_estimators')
    ax.set_ylabel('accurate')
    leg = ax.legend(loc='upper right', fancybox=True)
    leg.get_frame().set_alpha(0.7)

    plt.show()


def run_task1(DS):
    # (RF) random forest
    # RFShow(DS)
    # RF_parameter = {"n_estimators": 68,
    #                 "max_depth": 4,
    #                 "random_state": 0,
    #                 "min_samples_leaf": 6}
    # model = RandomForest.random_forest_model(DS.train_set, RF_parameter)
    # print(model.score(DS.test_set.feature, DS.test_set.label))
    # pre = model.predict(DS.test_set.feature)
    # print(confusion_matrix(DS.test_set.label, pre))

    # (ABC) adaboost classifier
    # ABCShow(DS)
    # ABC_parameter = {"max_depth": 2,
    #                  "min_samples_leaf": 20,
    #                  "n_estimators": 70,
    #                  "random_state": 0,
    #                  "learning_rate": 0.1,
    #                  "algorithm": "SAMME.R"}
    # model = AdaboostClassifier.adaboost_classifier_model(DS.train_set, ABC_parameter)
    # print(model.score(DS.test_set.feature, DS.test_set.label))
    # pre = model.predict(DS.test_set.feature)
    # print(confusion_matrix(DS.test_set.label, pre))
    pass


def test(DS):
    n_estimators = 400
    # A learning rate of 1. may not be optimal for both SAMME and SAMME.R
    learning_rate = 0.1

    X_test = DS.test_set.feature
    y_test = DS.test_set.label
    X_train = DS.train_set.feature
    y_train = DS.train_set.label

    dt_stump = DecisionTreeClassifier(max_depth=2, min_samples_leaf=20)
    dt_stump.fit(X_train, y_train)
    dt_stump_err = 1.0 - dt_stump.score(X_test, y_test)

    dt = DecisionTreeClassifier(max_depth=9, min_samples_leaf=10)
    dt.fit(X_train, y_train)
    dt_err = 1.0 - dt.score(X_test, y_test)

    ada_discrete = AdaBoostClassifier(
        base_estimator=dt_stump,
        learning_rate=learning_rate,
        n_estimators=n_estimators,
        random_state=rng,
        algorithm="SAMME")
    ada_discrete.fit(X_train, y_train)

    ada_real = AdaBoostClassifier(
        base_estimator=dt_stump,
        learning_rate=learning_rate,
        n_estimators=n_estimators,
        random_state=rng,
        algorithm="SAMME.R")
    ada_real.fit(X_train, y_train)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot([1, n_estimators], [dt_stump_err] * 2, 'k-',
            label='Decision Stump Error')
    ax.plot([1, n_estimators], [dt_err] * 2, 'k--',
            label='Decision Tree Error')

    ada_discrete_err = np.zeros((n_estimators,))
    for i, y_pred in enumerate(ada_discrete.staged_predict(X_test)):
        ada_discrete_err[i] = zero_one_loss(y_pred, y_test)

    ada_discrete_err_train = np.zeros((n_estimators,))
    for i, y_pred in enumerate(ada_discrete.staged_predict(X_train)):
        ada_discrete_err_train[i] = zero_one_loss(y_pred, y_train)

    ada_real_err = np.zeros((n_estimators,))
    for i, y_pred in enumerate(ada_real.staged_predict(X_test)):
        ada_real_err[i] = zero_one_loss(y_pred, y_test)

    ada_real_err_train = np.zeros((n_estimators,))
    for i, y_pred in enumerate(ada_real.staged_predict(X_train)):
        ada_real_err_train[i] = zero_one_loss(y_pred, y_train)

    ax.plot(np.arange(n_estimators) + 1, ada_discrete_err,
            label='Discrete AdaBoost Test Error',
            color='red')
    ax.plot(np.arange(n_estimators) + 1, ada_discrete_err_train,
            label='Discrete AdaBoost Train Error',
            color='blue')
    ax.plot(np.arange(n_estimators) + 1, ada_real_err,
            label='Real AdaBoost Test Error',
            color='orange')
    ax.plot(np.arange(n_estimators) + 1, ada_real_err_train,
            label='Real AdaBoost Train Error',
            color='green')

    # ax.set_ylim((0.0, 0.5))
    ax.set_xlabel('n_estimators')
    ax.set_ylabel('accurate')

    leg = ax.legend(loc='upper right', fancybox=True)
    leg.get_frame().set_alpha(0.7)

    plt.show()


def run_task2(DS):
    # print(DS.train_set.feature)
    # parameter_scale = {"hidden_layer": [2, 3],
    #                    "hidden_unit": [4, 8],
    #                    'batch_size': [50, 100],
    #                    'epochs': [10, 20, 50],
    #                    "activation": ["relu", "tanh"],
    #                    "loss": ["mean_absolute_error", "hinge"]}
    # nn_model = NeuralNetwork.tune_with_grid(DS.train_set, parameter_scale)
    # print(nn_model.predi)
    # print(nn_model.predict(np.array([[0,0,0,0],[1,1,1,1]])))

    # knn
    # model = KNN.knn_model(DS)
    # print(model.score(DS.test_set.feature, DS.test_set.label))
    parameter_scale = {"n_neighbors": }
    model = KNN.tune_with_grid(DS.train_set, parameter_scale)
    print(model.score(DS.test_set.feature, DS.test_set.label))
    pass


def main():
    DS = DataStructure(train_file_name="../data/lab4-train.csv",
                       test_file_name="../data/lab4-test.csv")
    # print(DS.train_set.feature / DS.train_set.feature.max(axis=0))
    # DS.train_set.feature = DS.train_set.feature / DS.train_set.feature.max(axis=0)

    # test(DS)

    # task 1
    # run_task1(DS)

    # task 2
    run_task2(DS)

    # task 3
    pass


if __name__ == "__main__":
    main()
