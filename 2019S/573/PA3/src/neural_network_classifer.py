import keras

import util
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD


def load_data():
    train = []
    label = []
    for i in util.read_csv_file("../data/optdigits.tra"):
        tra = i[0:-1]
        lab = i[-1]
        train.append(tra)
        label.append(lab)
    return train, label


def nn_model():
    model = Sequential()
    model.add(Dense(64, activation='relu', input_dim=64))
    model.add(Dropout(0.25))
    model.add(Dense(64, activation="relu"))
    model.add(Dropout(0.25))
    model.add(Dense(10, activation="softmax"))

    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy',
                  optimizer=sgd,
                  metrics=['accuracy'])

    return model


def main():
    x_train, y_train = load_data()
    y_train = keras.utils.to_categorical(y_train)
    model = nn_model()
    model.fit(np.array(x_train), y_train, epochs=20, batch_size=64)


if __name__ == "__main__":
    main()
