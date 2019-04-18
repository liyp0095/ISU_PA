import numpy as np
import keras
from DataStructure import DataStructure
import RandomForest
import AdaboostClassifier
import NeuralNetwork, KNN, LogisticRegression, DecisionTree, LogisticRegression, NaiveBayes, DecisionTree
import MajorityVote

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
    print("===================== TASK 1 ========================")
    # (RF) random forest
    # RFShow(DS)
    RF_parameter = {"n_estimators": 68,
                    "max_depth": 4,
                    "random_state": 0,
                    "min_samples_leaf": 6}
    rf_model = RandomForest.random_forest_model(DS.train_set, RF_parameter)
    rf_acc = rf_model.score(DS.test_set.feature, DS.test_set.label)
    print("Random Forest accuracy: %.4f" % rf_acc)
    pre = rf_model.predict(DS.test_set.feature)
    print("confusion matrix:")
    print(confusion_matrix(DS.test_set.label, pre))
    print("parameter:")
    print(rf_model.get_params())
    print()

    # (ABC) adaboost classifier
    ABCShow(DS)
    ABC_parameter = {"max_depth": 2,
                     "min_samples_leaf": 20,
                     "n_estimators": 70,
                     "random_state": 0,
                     "learning_rate": 0.1,
                     "algorithm": "SAMME.R"}
    abc_model = AdaboostClassifier.adaboost_classifier_model(DS.train_set, ABC_parameter)
    abc_acc = abc_model.score(DS.test_set.feature, DS.test_set.label)
    print("Adaboost Classifier accuracy: %.4f" % abc_acc)
    pre = abc_model.predict(DS.test_set.feature)
    print("confusion matrix:")
    print(confusion_matrix(DS.test_set.label, pre))
    print("parameter:")
    print(abc_model.get_params())
    print()


def run_task2(DS):
    print("===================== TASK 2 ========================")
    # NeuralNetwork
    parameter = {"hidden_layer": 3,
                 "hidden_unit": 9,
                 'batch_size': 128,
                 'epochs': 100,
                 "activation": "tanh",
                 "loss": "binary_crossentropy",
                 "dropout": 0.2,
                 "learn_rate": 0.1,
                 "momentum": 0.5}
    nn_model = NeuralNetwork.neural_network_train(DS.train_set, parameter)
    nn_acc = NeuralNetwork.model_accuracy(DS.test_set, nn_model)


    # knn
    # KNN.KNNShow(DS)
    parameter = {"n_neighbors": 5}
    knn_model = KNN.knn_model(parameter)
    knn_model.fit(DS.train_set.feature, DS.train_set.label)
    knn_acc = knn_model.score(DS.test_set.feature, DS.test_set.label)

    # Logistic Regression
    lr_model = LogisticRegression.LR_model(DS.train_set)
    lr_acc = lr_model.score(DS.test_set.feature, DS.test_set.label)

    # Naive Bayes
    nb_model = NaiveBayes.NB_model(DS.train_set)
    nb_acc = NaiveBayes.model_accuracy(DS.test_set, nb_model)
    # print(nb_acc)

    # Decision Tree
    parameter = {"max_depth": 9,
                 "min_sample_leaf": 10}
    dt_model = DecisionTree.DT_model(DS.train_set, parameter)
    dt_acc = dt_model.score(DS.test_set.feature, DS.test_set.label)

    print("Neural Network accuracy: %.4f" % nn_acc)
    print("KNN accuracy: %.4f" % knn_acc)
    print("Logistic Regression accuracy: %.4f" % lr_acc)
    print("Naive Bayes accuracy: %.4f" % nb_acc)
    print("Decision Tree accuracy: %.4f" % dt_acc)
    print()

    # Majority Vote
    umv_acc = MajorityVote.unweighted_model_predict([nn_model, knn_model, lr_model, nb_model, dt_model],
                                                    [nn_acc, knn_acc, lr_acc, nb_acc, dt_acc], DS.test_set)
    wmv_acc = MajorityVote.weighted_model_predict([nn_model, knn_model, lr_model, nb_model, dt_model],
                                                    [nn_acc, knn_acc, lr_acc, nb_acc, dt_acc], DS.test_set)
    print("Unweighted Majority Vote accuracy: %.4f" % umv_acc)
    print("Weighted Majority Vote accuracy: %.4f" % wmv_acc)
    print()


def run_task3(DS):
    print("===================== TASK 3 ========================")
    # (RF) random forest
    RF_parameter = {"n_estimators": 68,
                    "max_depth": 4,
                    "random_state": 0,
                    "min_samples_leaf": 6}
    rf_model = RandomForest.random_forest_model(DS.train_set, RF_parameter)
    rf_acc = rf_model.score(DS.test_set.feature, DS.test_set.label)

    # (ABC) adaboost classifier
    ABC_parameter = {"max_depth": 2,
                     "min_samples_leaf": 20,
                     "n_estimators": 70,
                     "random_state": 0,
                     "learning_rate": 0.1,
                     "algorithm": "SAMME.R"}
    abc_model = AdaboostClassifier.adaboost_classifier_model(DS.train_set, ABC_parameter)
    abc_acc = abc_model.score(DS.test_set.feature, DS.test_set.label)

    # NeuralNetwork
    parameter = {"hidden_layer": 3,
                 "hidden_unit": 9,
                 'batch_size': 128,
                 'epochs': 100,
                 "activation": "tanh",
                 "loss": "binary_crossentropy",
                 "dropout": 0.2,
                 "learn_rate": 0.1,
                 "momentum": 0.5}
    nn_model = NeuralNetwork.neural_network_train(DS.train_set, parameter)
    nn_acc = NeuralNetwork.model_accuracy(DS.test_set, nn_model)

    # knn
    parameter = {"n_neighbors": 5}
    knn_model = KNN.knn_model(parameter)
    knn_model.fit(DS.train_set.feature, DS.train_set.label)
    knn_acc = knn_model.score(DS.test_set.feature, DS.test_set.label)

    # Logistic Regression
    lr_model = LogisticRegression.LR_model(DS.train_set)
    lr_acc = lr_model.score(DS.test_set.feature, DS.test_set.label)

    # Naive Bayes
    nb_model = NaiveBayes.NB_model(DS.train_set)
    nb_acc = NaiveBayes.model_accuracy(DS.test_set, nb_model)

    # Decision Tree
    parameter = {"max_depth": 9,
                 "min_sample_leaf": 10}
    dt_model = DecisionTree.DT_model(DS.train_set, parameter)
    dt_acc = dt_model.score(DS.test_set.feature, DS.test_set.label)

    umv_acc = MajorityVote.unweighted_model_predict([rf_model, abc_model, nn_model, knn_model, lr_model, nb_model, dt_model],
                                                    [rf_acc, abc_acc, nn_acc, knn_acc, lr_acc, nb_acc, dt_acc],
                                                    DS.test_set)
    wmv_acc = MajorityVote.weighted_model_predict([rf_model, abc_model, nn_model, knn_model, lr_model, nb_model, dt_model],
                                                  [rf_acc, abc_acc, nn_acc, knn_acc, lr_acc, nb_acc, dt_acc],
                                                  DS.test_set)

    print("Random Forest accuracy: %.4f" % rf_acc)
    print("Adaboost Classifier accuracy: %.4f" % abc_acc)
    print("Neural Network accuracy: %.4f" % nn_acc)
    print("KNN accuracy: %.4f" % knn_acc)
    print("Logistic Regression accuracy: %.4f" % lr_acc)
    print("Naive Bayes accuracy: %.4f" % nb_acc)
    print("Decision Tree accuracy: %.4f" % dt_acc)
    print()

    print("Unweighted Majority Vote accuracy: %.4f" % umv_acc)
    print("Weighted Majority Vote accuracy: %.4f" % wmv_acc)
    print()
    pass


def main():
    DS = DataStructure(train_file_name="../data/lab4-train.csv",
                       test_file_name="../data/lab4-test.csv")
    # print(DS.train_set.feature / DS.train_set.feature.max(axis=0))
    # DS.train_set.feature = DS.train_set.feature / DS.train_set.feature.max(axis=0)
    # DS.test_set.feature = DS.test_set.feature / DS.test_set.feature.max(axis=0)
    # test(DS)

    # task 1
    run_task1(DS)

    # task 2
    run_task2(DS)

    # task 3
    run_task3(DS)
    pass


if __name__ == "__main__":
    main()
