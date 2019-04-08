import keras

from NNParameter import NNParameter
from CNNParameter import CNNParameter
from sklearn.metrics import classification_report, confusion_matrix

import util
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.optimizers import SGD
from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint
from keras.models import load_model

from keras.layers import Conv2D, MaxPooling2D


def load_data(filename):
    train = []
    label = []
    for i in util.read_csv_file(filename):
        tra = i[0:-1]
        lab = i[-1]
        train.append(tra)
        label.append(lab)
    return np.array(train).astype(float), np.array(label)


def nn_model(hidden_layer, hidden_unit, dropout, activation, loss, learn_rate, momentum):
    model = Sequential()
    for i in range(hidden_layer):
        model.add(Dense(hidden_unit, activation=activation, input_dim=64))
        model.add(Dropout(dropout))
    model.add(Dense(10, activation="softmax"))

    sgd = SGD(lr=learn_rate, momentum=momentum)
    model.compile(loss=loss,
                  optimizer=sgd,
                  metrics=['accuracy'])
    return model


def cnn_model(hidden_layer, hidden_unit, dropout, activation, loss, learn_rate, momentum, kernel_size, pool_size):
    model = Sequential()

    model.add(Conv2D(hidden_unit, kernel_size=kernel_size, activation=activation))
    model.add(MaxPooling2D(pool_size=pool_size))
    model.add(Dropout(dropout))

    model.add(Flatten())
    for i in range(hidden_layer):
        model.add(Dense(hidden_unit, activation=activation))
    model.add(Dense(10, activation='softmax'))
    sgd = SGD(lr=learn_rate, momentum=momentum)
    model.compile(loss=loss,
                  optimizer=sgd,
                  metrics=['accuracy'])
    return model


def split_validation(x_train, y_train, ratio):
    sample_number = len(x_train)
    n_train = int(ratio * sample_number)
    return x_train[:n_train, :], x_train[n_train:, :], y_train[:n_train, :], y_train[n_train:, :]


def def_early_stop(monitor, mode, patience, save_model_name):
    es = EarlyStopping(monitor=monitor, mode=mode, verbose=1, patience=patience)
    mc = ModelCheckpoint(save_model_name, monitor=monitor, mode=mode, verbose=1, save_best_only=True)
    return es, mc


def run_nn_model(x_train, y_train, x_valid, y_valid, parameters):
    model = nn_model(hidden_layer=parameters.hidden_layer,
                     hidden_unit=parameters.hidden_unit,
                     dropout=parameters.dropout,
                     activation=parameters.activation,
                     loss=parameters.loss,
                     learn_rate=parameters.learn_rate,
                     momentum=parameters.learn_rate)
    es, mc = def_early_stop(monitor=parameters.monitor,
                            mode=parameters.mode,
                            patience=parameters.patience,
                            save_model_name=parameters.model_name)
    model.fit(x_train, y_train, validation_data=(x_valid, y_valid), epochs=500, verbose=0, callbacks=[es, mc])


def run_cnn_model(x_train, y_train, x_valid, y_valid, parameters):
    c_model = cnn_model(hidden_layer=parameters.hidden_layer,
                        hidden_unit=parameters.hidden_unit,
                        dropout=parameters.dropout,
                        activation=parameters.activation,
                        loss=parameters.loss,
                        learn_rate=parameters.learn_rate,
                        momentum=parameters.learn_rate,
                        kernel_size=parameters.kerner_size,
                        pool_size=parameters.pool_size)
    es, mc = def_early_stop(monitor=parameters.monitor,
                            mode=parameters.mode,
                            patience=parameters.patience,
                            save_model_name=parameters.model_name)
    c_model.fit(x_train, y_train, validation_data=(x_valid, y_valid), epochs=500, verbose=0, callbacks=[es, mc])



def print_class_accuracy(data):
    print("Class accuracies: ")
    sum = 0.0
    for index,i in enumerate(data):
        for j in i:
            sum += j
        print("Accuracy of class %d : %.5f" % (index, data[index, index] / sum))
        sum = 0.0


def main():
    # load train data and test data
    x_train_ori, y_train_ori = load_data("../data/optdigits.tra")
    x_test_ori, y_test_ori = load_data("../data/optdigits.tes")

    # format and scale train and test data
    x_train = x_train_ori / 16
    y_train = keras.utils.to_categorical(y_train_ori)
    x_test = x_test_ori / 16
    y_test = keras.utils.to_categorical(y_test_ori)

    # split train to train and validation set
    x_train, x_valid, y_train, y_valid = split_validation(x_train, y_train, 0.8)

    # # task 1 (a) and (b) fully-connected feed-forward neural networks / sum of square error
    # parameter = NNParameter()
    # parameter.activation = 'tanh'
    # parameter.loss = "categorical_crossentropy"
    # run_nn_model(x_train, y_train, x_valid, y_valid, parameter)

    # parameter = NNParameter()
    # parameter.activation = 'tanh'
    # parameter.loss = "categorical_crossentropy"
    # parameter.hidden_layer = 3
    # parameter.model_name = "fully-connected_feed-forward_neural_networks.m2"
    # run_nn_model(x_train, y_train, x_valid, y_valid, parameter)

    # parameter = NNParameter()
    # parameter.activation = 'tanh'
    # parameter.loss = "categorical_crossentropy"
    # parameter.hidden_layer = 3
    # parameter.hidden_unit = 256
    # parameter.learn_rate = 0.05
    # parameter.model_name = "fully-connected_feed-forward_neural_networks.m3"
    # run_nn_model(x_train, y_train, x_valid, y_valid, parameter)

    # parameter = NNParameter()
    # parameter.activation = 'tanh'
    # parameter.loss = "categorical_crossentropy"
    # parameter.hidden_layer = 3
    # parameter.hidden_unit = 128
    # parameter.learn_rate = 0.05
    # parameter.momentum = 0.3
    # parameter.model_name = "fully-connected_feed-forward_neural_networks.m4"
    # run_nn_model(x_train, y_train, x_valid, y_valid, parameter)

    # parameter = NNParameter()
    # parameter.activation = 'tanh'
    # parameter.loss = "categorical_crossentropy"
    # parameter.hidden_layer = 3
    # parameter.hidden_unit = 128
    # parameter.learn_rate = 0.05
    # parameter.momentum = 0.3
    # parameter.dropout = 0.2
    # parameter.model_name = "fully-connected_feed-forward_neural_networks.m5"
    # run_nn_model(x_train, y_train, x_valid, y_valid, parameter)

    # model = load_model("fully-connected_feed-forward_neural_networks.m3")
    # train_loss, train_acc = model.evaluate(x_train, y_train, verbose=0)
    # test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
    # print('Train: %.5f, %.5f \n Test: %.5f, %.5f' % (train_loss,
    #                                                  train_acc,
    #                                                  test_loss,
    #                                                  test_acc))
    #
    # yp = np.argmax(model.predict(x_train_ori/16), axis=1)
    # train_cm = confusion_matrix(y_train_ori.astype(int), yp)
    # print("confusion matrix of trainset")
    # print(train_cm)
    # yp = np.argmax(model.predict(x_test_ori / 16), axis=1)
    # test_cm = confusion_matrix(y_test_ori.astype(int), yp)
    # print("confusion matrix of testset")
    # print(test_cm)
    #
    # print_class_accuracy(train_cm)
    # print_class_accuracy(test_cm)

    # task 2 convolutional networks
    x_train_reshape = x_train.reshape(x_train.shape[0], 8, 8, 1)
    x_valid_reshape = x_valid.reshape(x_valid.shape[0], 8, 8, 1)
    x_test_reshape = x_test.reshape(x_test.shape[0], 8, 8, 1)

    # parameter = CNNParameter()
    # parameter.loss = "categorical_crossentropy"
    # run_cnn_model(x_train_reshape, y_train, x_valid_reshape, y_valid, parameter)

    # parameter = CNNParameter()
    # parameter.loss = "categorical_crossentropy"
    # parameter.hidden_layer = 3
    # parameter.model_name = "convolutional_networks.m2"
    # run_cnn_model(x_train_reshape, y_train, x_valid_reshape, y_valid, parameter)

    # parameter = CNNParameter()
    # parameter.loss = "categorical_crossentropy"
    # parameter.hidden_layer = 3
    # parameter.learn_rate = 0.05
    # parameter.kernel_size = (5, 5)
    # parameter.model_name = "convolutional_networks.m3"
    # run_cnn_model(x_train_reshape, y_train, x_valid_reshape, y_valid, parameter)

    # parameter = CNNParameter()
    # parameter.loss = "categorical_crossentropy"
    # parameter.hidden_layer = 3
    # parameter.hidden_unit = 128
    # parameter.learn_rate = 0.1
    # parameter.kernel_size = (5, 5)
    # parameter.momentum = 0.0
    # parameter.model_name = "convolutional_networks.m4"
    # run_cnn_model(x_train_reshape, y_train, x_valid_reshape, y_valid, parameter)

    # parameter = CNNParameter()
    # parameter.loss = "categorical_crossentropy"
    # parameter.hidden_layer = 3
    # parameter.hidden_unit = 128
    # parameter.learn_rate = 0.1
    # parameter.momentum = 0.0
    # parameter.kernel_size = (5, 5)
    # parameter.pool_size = (4, 4)
    # parameter.model_name = "convolutional_networks.m5"
    # run_cnn_model(x_train_reshape, y_train, x_valid_reshape, y_valid, parameter)

    model = load_model("convolutional_networks.m4")
    train_loss, train_acc = model.evaluate(x_train_reshape, y_train, verbose=0)
    test_loss, test_acc = model.evaluate(x_test_reshape, y_test, verbose=0)
    print('Train: %.5f, %.5f \n Test: %.5f, %.5f' % (train_loss,
                                                     train_acc,
                                                     test_loss,
                                                     test_acc))

    yp = np.argmax(model.predict((x_train_ori/16).reshape(x_train_ori.shape[0], 8, 8, 1)), axis=1)
    train_cm = confusion_matrix(y_train_ori.astype(int), yp)
    print("confusion matrix of trainset")
    print(train_cm)
    yp = np.argmax(model.predict((x_test_ori / 16).reshape(x_test_ori.shape[0], 8, 8, 1)), axis=1)
    test_cm = confusion_matrix(y_test_ori.astype(int), yp)
    print("confusion matrix of testset")
    print(test_cm)

    print_class_accuracy(train_cm)
    print_class_accuracy(test_cm)



if __name__ == "__main__":
    main()
