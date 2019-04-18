from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

import matplotlib.pyplot as plt


def knn_model(parameter):
    model = KNeighborsClassifier(n_neighbors=parameter["n_neighbors"])
    return model


def KNNShow(DS):
    parameter = {"n_neighbors": 1}
    fig = plt.figure()
    ax = fig.add_subplot(111)
    score = []
    for i in range(30):
        parameter["n_neighbors"] = i + 1
        model = knn_model(parameter)
        model.fit(DS.train_set.feature, DS.train_set.label)
        score.append(model.score(DS.test_set.feature, DS.test_set.label))
    ax.plot([i+1 for i in range(30)], score)
    ax.set_xlabel('n_estimators')
    ax.set_ylabel('accurate')
    plt.show()


def tune_with_grid(data, parameter_scale):
    knn = KNeighborsClassifier(n_neighbors=5)
    grid = GridSearchCV(knn, param_grid=parameter_scale, n_jobs=-1, cv=5)
    rst = grid.fit(data.feature, data.label)
    return rst.best_estimator_


def main():
    pass


if __name__ == "__main__":
    main()
