from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


def NB_model(data):
    model = GaussianNB()
    model.fit(data.feature, data.label)
    return model


def model_accuracy(data, model):
    pre = model.predict(data.feature)
    return accuracy_score(data.label, pre)


def main():
    pass


if __name__ == "__main__":
    main()
