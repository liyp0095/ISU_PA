import numpy as np
from sklearn.metrics import accuracy_score


def unweighted_model_predict(model_list, model_acc, data):
    rst = [0.0] * len(data.label)
    for index, model in enumerate(model_list):
        pre = model.predict(data.feature)
        if len(pre.shape) > 1:
            data_feature = data.feature / data.feature.max(axis=0)
            pre = model.predict(data_feature)
            pre = np.argmax(pre, axis=-1)
        rst = rst + pre
    rst = rst / 5
    rst = np.array(rst).round()
    return accuracy_score(data.label, rst)


def weighted_model_predict(model_list, model_acc, data):
    rst = [0.0] * len(data.label)
    for index, model in enumerate(model_list):
        pre = model.predict(data.feature)
        if len(pre.shape) > 1:
            data_feature = data.feature / data.feature.max(axis=0)
            pre = model.predict(data_feature)
            pre = np.argmax(pre, axis=-1)
        rst = rst + pre * model_acc[index]
    rst = rst / sum(model_acc)
    rst = np.array(rst).round()
    return accuracy_score(data.label, rst)


def main():
    pass


if __name__ == "__main__":
    main()
