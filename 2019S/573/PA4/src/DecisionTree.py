from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier


def DT_model(data, parameter):
    model = DecisionTreeClassifier(max_depth=parameter["max_depth"],
                                   min_samples_leaf=parameter["min_sample_leaf"])
    model.fit(data.feature, data.label)
    return model


def model_accuracy(data, model):
    pre = model.predict(data.feature)
    return accuracy_score(data.label, pre)


def main():
    pass


if __name__ == "__main__":
    main()