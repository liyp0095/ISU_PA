from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV


def knn_model():
    model = KNeighborsClassifier(n_neighbors=21)
    return model


def tune_with_grid(data, parameter_scale):
    knn = KNeighborsClassifier(n_neighbors=5)
    grid = GridSearchCV(knn, param_grid=parameter_scale, n_jobs=-1, cv=5)
    rst = grid.fit(data.feature, data.label)
    return rst.best_estimator_


def main():
    pass


if __name__ == "__main__":
    main()
