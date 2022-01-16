from shared.eval import test_model_implementation
from components.layers.sigmoid_layer import SigmoidLayer
from components.layers.linear_layer import LinearLayer
from components.loss_functions.bce_loss import BCELoss
from components.model import Model


class LR(Model):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def init_layers(self, X):
        self.layers.append(
            LinearLayer(input_dim=X.shape[1], output_dim=1, lr=self.lr, mu=self.mu)
        )
        self.layers.append(SigmoidLayer())
        self.loss_fn = BCELoss()


class_params = {
    "n_samples": 10000,
    "n_features": 20,
    "n_classes": 2,
    "class_sep": 8,
    "random_state": 88,
}

training_params = {"lr": 0.001, "batch_size": 512, "n_epochs": 500, "plot_losses": True}

test_model_implementation(LR(**training_params), **class_params)
