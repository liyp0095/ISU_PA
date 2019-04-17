from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix


def random_forest(DS, parameter, train_score, test_score):
    clf = RandomForestClassifier(n_estimators=parameter["n_estimators"],
                                 max_depth=parameter["max_depth"],
                                 min_samples_leaf=parameter["min_samples_leaf"],
                                 random_state=parameter["random_state"])
    clf.fit(DS.train_set.feature, DS.train_set.label)
    train_score.append(clf.score(DS.train_set.feature, DS.train_set.label))
    test_score.append(clf.score(DS.test_set.feature, DS.test_set.label))


def random_forest_model(data, parameter):
    clf = RandomForestClassifier(n_estimators=parameter["n_estimators"],
                                 max_depth=parameter["max_depth"],
                                 min_samples_leaf=parameter["min_samples_leaf"],
                                 random_state=parameter["random_state"])
    clf.fit(data.feature, data.label)
    return clf


def confusion_matrix(clf, data):
    pre = clf.predict(data.feature)
    print(pre)
    print(data.label)
    return confusion_matrix(pre, data.label)


def main():
    pass


if __name__ == "__main__":
    main()
