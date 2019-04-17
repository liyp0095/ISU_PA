import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.optimizers import SGD
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV


def nn_model(hidden_layer=1,
             hidden_unit=2,
             dropout=0.2,
             activation="relu",
             loss="categorical_crossentropy",
             learn_rate=0.1,
             momentum=0.8,
             class_num=2,
             input_dim=4):
    model = Sequential()
    for i in range(hidden_layer):
        model.add(Dense(hidden_unit, activation=activation, input_dim=input_dim))
        model.add(Dropout(dropout))
    model.add(Dense(class_num, activation="softmax"))

    sgd = SGD(lr=learn_rate, momentum=momentum)
    model.compile(loss=loss,
                  optimizer=sgd,
                  metrics=['accuracy'])
    return model


def tune_with_grid(data, parameter_scale):
    model = KerasClassifier(build_fn=nn_model, verbose=0, shuffle=True)
    grid = GridSearchCV(estimator=model, param_grid=parameter_scale, n_jobs=-1, cv=5, return_train_score=True)
    output_category = keras.utils.to_categorical(data.label, num_classes=None)
    grid_result = grid.fit(data.feature, output_category)
    print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
    means = grid_result.cv_results_['mean_test_score']
    stds = grid_result.cv_results_['std_test_score']
    params = grid_result.cv_results_['params']
    for mean, stdev, param in zip(means, stds, params):
        print("%f (%f) with: %r" % (mean, stdev, param))
    return grid_result.best_estimator_


def neural_network_model(data, parameter):
    model = nn_model(hidden_layer=parameter["hidden_layer"],
                     hidden_unit=parameter["hidden_unit"],
                     dropout=parameter["dropout"],
                     activation=parameter["activation"],
                     loss=parameter["loss"],
                     learn_rate=parameter["learn_rate"],
                     momentum=parameter["momentum"],
                     class_num=2)


def main():
    pass


if __name__ == "__main__":
    main()
