class CNNParameter:
    hidden_layer = 1
    hidden_unit = 64
    dropout = 0.0
    activation = 'relu'
    loss = "mean_squared_error"
    learn_rate = 0.01
    momentum = 0.8
    monitor = 'val_acc'
    mode = 'max'
    patience = 10
    kerner_size = (3, 3)
    pool_size = (2, 2)
    model_name = 'convolutional_networks.m1'

    def __init__(self):
        pass