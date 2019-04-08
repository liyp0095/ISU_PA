class NNParameter:
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
    model_name = 'fully-connected_feed-forward_neural_networks.m1'

    def __init__(self):
        pass
