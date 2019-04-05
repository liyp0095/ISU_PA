import keras

import util
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.optimizers import SGD
from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint

from keras.layers import Conv2D, MaxPooling2D


def load_data():
    train = []
    label = []
    for i in util.read_csv_file("../data/optdigits.tra"):
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


def cnn_model():
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3),
                     activation='relu',
                     input_shape=(8, 8, 1)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(10, activation='softmax'))
    model.compile(loss=keras.losses.categorical_crossentropy,
                  optimizer=keras.optimizers.Adadelta(),
                  metrics=['accuracy'])
    return model


def split_validation(x_train, y_train, ratio):
    sample_number = len(x_train)
    n_train = int(ratio * sample_number)
    return x_train[:n_train, :], x_train[n_train:, :], y_train[:n_train, :], y_train[n_train:, :]


def main():
    x_train, y_train = load_data()
    x_train = x_train / 16
    y_train = keras.utils.to_categorical(y_train)
    x_train, x_valid, y_train, y_valid = split_validation(x_train, y_train, 0.8)

    x_train_reshape = x_train.reshape(x_train.shape[0], 8, 8, 1)
    x_valid_reshape = x_valid.reshape(x_valid.shape[0], 8, 8, 1)

    print(x_train_reshape.shape)
    print(y_train.shape)
    print(x_valid_reshape.shape)
    print(y_valid.shape)

    c_model = cnn_model()
    es = EarlyStopping(monitor='val_acc', mode='max', verbose=1, patience=10)
    mc = ModelCheckpoint('best_model.h5', monitor='val_acc', mode='max', verbose=1, save_best_only=True)
    c_model.fit(x_train_reshape, y_train, validation_data=(x_valid_reshape, y_valid), epochs=100, verbose=0, callbacks=[es, mc])

    # model = nn_model(loss='categorical_crossentropy')
#    model = nn_model(hidden_layer=2, hidden_unit=128, dropout=0.0, activation='relu', loss="mean_squared_error",
#                     learn_rate=0.02, momentum=0.5)
#    es = EarlyStopping(monitor='val_acc', mode='max', verbose=1, patience=10)
#    mc = ModelCheckpoint('best_model.h5', monitor='val_acc', mode='max', verbose=1, save_best_only=true)
#    history = model.fit(x_train, y_train, validation_data=(x_valid, y_valid), epochs=100, verbose=0, callbacks=[es, mc])

#    model = nn_model()
#    model.fit(np.array(x_train), y_train, epochs=20, batch_size=64)


if __name__ == "__main__":
    main()
