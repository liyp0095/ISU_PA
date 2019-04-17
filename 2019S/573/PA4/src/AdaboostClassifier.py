from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier


def adaboost_classifier(DS, parameter, train_score, test_score):
    abc = AdaBoostClassifier(DecisionTreeClassifier(max_depth=parameter["max_depth"],
                                                    min_samples_leaf=parameter["min_samples_leaf"]),
                             n_estimators=parameter["n_estimators"],
                             random_state=parameter["random_state"],
                             learning_rate=parameter["learning_rate"],
                             algorithm=parameter["algorithm"])
    abc.fit(DS.train_set.feature, DS.train_set.label)
    test_score.extend(list(abc.staged_score(DS.test_set.feature, DS.test_set.label)))
    train_score.extend(list(abc.staged_score(DS.train_set.feature, DS.train_set.label)))


def adaboost_classifier_model(data, parameter):
    abc = AdaBoostClassifier(DecisionTreeClassifier(max_depth=parameter["max_depth"],
                                                    min_samples_leaf=parameter["min_samples_leaf"]),
                             n_estimators=parameter["n_estimators"],
                             random_state=parameter["random_state"],
                             learning_rate=parameter["learning_rate"],
                             algorithm=parameter["algorithm"])
    abc.fit(data.feature, data.label)
    return abc


def main():
    pass


if __name__ == "__main__":
    main()
