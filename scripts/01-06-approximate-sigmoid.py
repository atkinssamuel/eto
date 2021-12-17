from models.model_implementations.sigmoid_approx import SigApprox
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
    "mu": 0.01,
    "batch_size": 1028,
    "n_epochs": 50,
    "plot_losses": True,
}

test_model_implementation(SigApprox(**training_params), **class_params)
