from models.model_implementations.multi_layer_nn import NN
from shared.eval import test_model_implementation

class_params = {
    "n_samples": 10000,
    "n_features": 20,
    "n_classes": 2,
    "class_sep": 8,
    "random_state": 88,
}

training_params = {
    "lr": 0.01,
    "momentum": 0.01,
    "batch_size": 512,
    "n_epochs": 50,
    "plot_losses": True,
}

test_model_implementation(NN(**training_params), **class_params)
