from models.model_implementations.lr import LR
from shared.eval import test_model_implementation

class_params = {
            "n_samples": 10000,
            "n_features": 20,
            "n_classes": 2,
            "class_sep": 8,
            "random_state": 88
}

training_params = {
    "lr": 0.001,
    "batch_size": 512,
    "n_epochs": 500,
    "plot_losses": True
}

test_model_implementation(LR(**training_params), **class_params)

