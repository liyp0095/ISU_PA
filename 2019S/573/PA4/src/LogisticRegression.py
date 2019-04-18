from sklearn.linear_model import LogisticRegression


def LR_model(data):
    model = LogisticRegression(solver="lbfgs")
    model.fit(data.feature, data.label)
    return model


def main():
    pass


if __name__ == "__main__":
    main()
